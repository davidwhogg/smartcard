.SUFFIXES: .tex .dvi .ps .pdf .mp .eps
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: summary.pdf description.pdf facilities.pdf biosketch_hogg.pdf \
	biosketch_dfm.pdf

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
