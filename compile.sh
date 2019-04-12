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

SELECTED_DIR=$(realpath "$1")

echo Script path: \""$SCRIPT_PATH"\"

files=("$SELECTED_DIR"/lesson*.md)
IFS=$'\n' files=($(sort <(printf "%s\n" "${files[@]}")))
IFS=$'\n' file_names=($(basename -a "${files[@]}"))

echo Files:
printf '%s\n' "${file_names[@]}" | column -c 80

# echo Compiling pandoc
# pandoc -t html \
#     --toc --toc-depth=2 \
#     --number-sections \
#     --katex="" \
#     --verbose \
#     "${files[@]}" -o RTS.html
#     # --css ../pandoc/pandoc.css \
#     # --standalone \
#     # --template ../pandoc/template \
#     # --self-contained \
#     # --mathjax \

echo Compiling webpack
npx webpack --config $SCRIPT_PATH/webpack/webpack.config.babel.js

# echo Compilation finished
# if [[ $? == 0 ]]; then
#     xdg-open RTS.html > /dev/null 2>&1
# fi




