#!/usr/bin/env bash
# set -x
set -o pipefail
shopt -s nullglob

SCRIPT_NAME=$(basename "$0")

# Use getopt to get the options
eval set -- $(getopt -o "s" -l "server" -n "$SCRIPT_NAME" -- "$@")

# Parse given options
SERVER=false
while true; do
    case "$1" in
        -s | --server ) SERVER=true; shift ;;
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

echo Script path: \""$SCRIPT_PATH"\"

files=("$SELECTED_DIR"/lesson*.md)
IFS=$'\n' files=($(sort <(printf "%s\n" "${files[@]}")))
IFS=$'\n' file_names=($(basename -a "${files[@]}"))

echo Files:
printf '%s\n' "${file_names[@]}" | column -c 80

# Check if output directory exists
if [ -d "$OUT_PATH" ]; then
    rm -r "$OUT_PATH"
fi

mkdir "$OUT_PATH"

cd "$SELECTED_DIR"

echo Compiling pandoc
pandoc -t html \
    --toc --toc-depth=2 \
    --number-sections \
    --verbose \
    --katex="" \
    "${files[@]}" -o "$OUT_PATH/pandoc.html"
    # --self-contained \
    # --standalone \
    # --katex="" \
    # --css ../pandoc/pandoc.css \
    # --template ../pandoc/template \
    # --mathjax \

cd "$OLDPWD"

if [ -d "$SELECTED_DIR/images" ]; then
    cp -R "$SELECTED_DIR/images" "$OUT_PATH"
fi

WEBPACK_COMMAND=webpack
if [ $SERVER ]; then
    WEBPACK_COMMAND=(webpack-dev-server --color)
fi


echo Compiling webpack
npx "${WEBPACK_COMMAND[@]}" \
    --config $SCRIPT_PATH/webpack/webpack.config.babel.js \
    --display errors-only \
    --env.title="$SELECTED_NAME"

# Clean up
echo Cleaning up
if [ -d "$OUT_PATH/images" ]; then
    rm -r "$OUT_PATH/images"
fi
rm "$OUT_PATH/pandoc.html" "$OUT_PATH"/*.js*

echo Compilation finished
if [[ $? == 0 ]]; then
    xdg-open "$OUT_PATH"/index.html > /dev/null 2>&1
fi




