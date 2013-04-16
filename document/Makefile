.SUFFIXES: .tex .dvi .ps .pdf .mp .eps
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: description.pdf

%.aux: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
