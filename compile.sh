#!/usr/bin/env bash

# set -x
shopt -s nullglob

if [ "$#" -ne 1 ]; then
    echo Usage: $(basename "$0") directory
    echo 
    echo Processes the directory that contains Markdown '*.md' files
    exit 0
fi

SCRIPT_DIR=$(dirname "$0")
SCRIPT_PATH=$(realpath "$SCRIPT_DIR")
OUT_PATH="$SCRIPT_PATH/dist"

SELECTED_DIR=$(realpath "$1")

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
    "${files[@]}" -o "$OUT_PATH/pandoc.html"
    # --self-contained \
    # --standalone \
    # --katex="" \
    # --css ../pandoc/pandoc.css \
    # --template ../pandoc/template \
    # --mathjax \

cd "$OLDPWD"

# mv "$OUT_PATH/pandoc.html" "$OUT_PATH/pandoc.htx"

if [ -d "$SELECTED_DIR/images" ]; then
    cp -R "$SELECTED_DIR/images" "$OUT_PATH"
fi

echo Compiling webpack
npx -n "--max_old_space_size=8192" webpack --config $SCRIPT_PATH/webpack/webpack.config.babel.js --display errors-only

# Clean up

echo Cleaning up
if [ -d "$OUT_PATH/images" ]; then
    rm -r "$OUT_PATH/images"
fi
rm "$OUT_PATH/pandoc.html" "$OUT_PATH"/*.js*

# echo Compilation finished
# if [[ $? == 0 ]]; then
#     xdg-open RTS.html > /dev/null 2>&1
# fi




