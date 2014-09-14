# You want latexmk to *always* run, because make does not have all the info.
.PHONY: pdf

# First rule should always be the default "all" rule, so both "make all" and
# "make" will invoke it.
all: pdf

# MAIN LATEXMK RULE
# -pdf tells latexmk to generate PDF directly (instead of DVI).
# -pdflatex="" tells latexmk to call a specific backend with specific options.
# -use-make tells latexmk to call make for generating missing files.
# -interactive=nonstopmode keeps the pdflatex backend from stopping at a
# missing file reference and interactively asking you for an alternative.

pdf: raghava-resume.tex
#	latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make raghava-resume.tex
#
	cd gen; latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make raghava-resume.tex

clean:
	latexmk -C

# Use this with latexmk to simplify the job of generating pdfs from tex sources. 
# A simple 'make all' would do the job!
