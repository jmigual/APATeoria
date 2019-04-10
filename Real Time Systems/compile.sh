#!/usr/bin/env bash

files=$(ls lesson_*.md | sort)

echo Compiling pandoc
pandoc -t html \
    --standalone \
    --self-contained \
    --toc --toc-depth=2 \
    --number-sections \
    --mathjax="" \
    --template ../pandoc/template \
    --css ../pandoc/pandoc.css \
    --verbose \
    $files -o RTS.html

echo Compilation finished
if [[ $? == 0 ]]; then
    xdg-open RTS.html > /dev/null 2>&1
fi




