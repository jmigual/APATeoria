#!/usr/bin/env bash
# set -x
set -o pipefail
shopt -s nullglob
start=$(date +%s.%N)

SCRIPT_NAME=$(basename "$0")

# Use getopt to get the options
eval set -- $(getopt -o "s" -l "server,no-clean,no-show" -n "$SCRIPT_NAME" -- "$@")

# Parse given options
SERVER=false
CLEAN=true
SHOW=true
while true; do
    case "$1" in
        -s | --server ) SERVER=true; shift ;;
        --no-clean ) CLEAN=false; shift ;;
        --no-show ) SHOW=false; shift ;;
        -- ) shift; break ;;
        * ) break ;;
    esac
done

# Check for proper number of arguments
if [ "$#" -lt 1 ]; then
    echo Usage: $SCRIPT_NAME [OPTIONS] directory
    echo 
    echo Processes the directory that contains Markdown '*.md' files
    echo
    echo OPTIONS:
    echo '-s, --server'
    exit 0
fi

SCRIPT_DIR=$(dirname "$0")
SCRIPT_PATH=$(realpath "$SCRIPT_DIR")
OUT_PATH="$SCRIPT_PATH/dist"

SELECTED_DIR=$(realpath "$1")
SELECTED_NAME=$(basename "$SELECTED_DIR")
PATH_IMAGES="$SELECTED_DIR/images"

echo Script path: \""$SCRIPT_PATH"\"

files=("$SELECTED_DIR"/*.md)
IFS=$'\n' files=($(sort <(printf "%s\n" "${files[@]}")))
IFS=$'\n' file_names=($(basename -a "${files[@]}"))

echo Files:
printf '%s\n' "${file_names[@]}" | column -c 80

# Check if output directory exists
if [ -d "$OUT_PATH" ]; then
    rm -r "$OUT_PATH"
fi

mkdir "$OUT_PATH"

compile_pandoc() {
    echo Compiling pandoc
    local PANDOC=$(pandoc \
        --from "markdown+emoji" \
        --to html \
        --standalone \
        --toc --toc-depth=2 \
        --number-sections \
        --filter mermaid-filter \
        --verbose \
        --mathjax="" \
        --metadata=title:$SELECTED_NAME \
        --metadata=lang:en \
        "${files[@]}")

    PANDOC="${PANDOC#*<body>}"
    PANDOC="${PANDOC%</body>*}"
    cat << EOF > "$OUT_PATH/pandoc.html"
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content= "width=device-width, initial-scale=1.0"> 
    <title>$SELECTED_NAME</title>
  </head>
  <body>
  $PANDOC
  </body>
</html>
EOF
}

process_image() {
    local PATH_IM_REL=$(realpath --relative-to="$PATH_IMAGES" "$1")
    local PATH_IM_OUT="$OUT_PATH/images/$PATH_IM_REL"
    mkdir -p $(dirname "$PATH_IM_OUT")
    npx imagemin $1 > "$PATH_IM_OUT"
}

if [ -d $PATH_IMAGES ]; then
    compile_pandoc &
    echo Copying images from "$PATH_IMAGES"
    IMAGES=$(find "$PATH_IMAGES" -regextype posix-extended -regex ".*/.*\.(png|jpe?g)")
    for image in $IMAGES; do
        echo Image: $image
        process_image $image &
    done
    wait
else
    compile_pandoc
fi

WEBPACK_COMMAND=webpack
if $SERVER; then
    WEBPACK_COMMAND=(webpack-dev-server --color)
fi

echo Compiling webpack
npx "${WEBPACK_COMMAND[@]}" \
    -p \
    --progress \
    --config $SCRIPT_PATH/webpack/webpack.config.babel.js \
    --display normal
#    --display errors-only \
RESULT=$?

if $CLEAN; then
    echo Cleaning up
    if [ -d "$OUT_PATH/images" ]; then
        rm -r "$OUT_PATH/images"
    fi
    rm "$OUT_PATH/pandoc.html" "$OUT_PATH"/*.js* "$OUT_PATH"/*.css
fi

echo Compilation finished
ls -lh $OUT_PATH

end=$(date +%s.%N)
echo Time: $(echo "$end - $start" | bc)

if [[ $RESULT != 0 ]]; then
    echo Error occurred during Compilation
fi

if [[ $RESULT == 0 ]] && ! $SERVER && $SHOW; then
    xdg-open "$OUT_PATH"/index.html > /dev/null 2>&1
fi




