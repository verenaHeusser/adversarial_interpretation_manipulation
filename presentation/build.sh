#!/usr/bin/sh

DATE_COVER=$(date "+%d %B %Y")

SOURCE_FORMAT="markdown_strict\
+pipe_tables\
+backtick_code_blocks\
+auto_identifiers\
+strikeout\
+yaml_metadata_block\
+implicit_figures\
+all_symbols_escapable\
+link_attributes\
+smart\
+fenced_divs"

# pandoc -s --dpi=300 --slide-level 2 --toc --listings --shift-heading-level=0 --columns=50 --template default.latex --pdf-engine xelatex -f "$SOURCE_FORMAT" -M date="$DATE_COVER" -V classoption:aspectratio=169 -V lang=en-US -t beamer presentation.md -o presentation.pdf

pandoc -t beamer presentation.md -V aspectratio=169 -V theme:metropolis -M date="$DATE_COVER" -o presentation.pdf