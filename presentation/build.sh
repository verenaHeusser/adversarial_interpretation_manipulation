#!/usr/bin/sh

DATE_COVER=$(date "+%d %B %Y")

SOURCE_FORMAT="markdown"

# pandoc -s --dpi=300 --slide-level 2 --toc --listings --shift-heading-level=0 --columns=50 --template default.latex --pdf-engine xelatex -f "$SOURCE_FORMAT" -M date="$DATE_COVER" -V classoption:aspectratio=169 -V lang=en-US -t beamer presentation.md -o presentation.pdf

pandoc -t beamer presentation.md -M date="$DATE_COVER" --slide-level=2 -o presentation.pdf