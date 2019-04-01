#!/usr/bin/env bash

files=$(ls lesson_*.md | sort)

echo Compiling pandoc
pandoc -t html \
    --standalone \
    --toc --toc-depth=1 \
    --number-sections \
    --mathjax \
    --css ../pandoc/pandoc.css \
    $files -o RTS.html

echo Compilation finished
if [[ $? == 0 ]]; then
    xdg-open RTS.html > /dev/null 2>&1
fi




