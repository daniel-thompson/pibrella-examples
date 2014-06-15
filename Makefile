NOTEBOOKS = $(wildcard *.ipynb five_liners/*.ipynb)
PYS = $(NOTEBOOKS:.ipynb=.py)
RSTS = $(NOTEBOOKS:.ipynb=.rst)
PDFS = $(NOTEBOOKS:.ipynb=.pdf)

all : $(PDFS) $(PYS)

clean :
	$(RM) $(PDFS) $(RSTS)

pristine : clean
	$(RM) $(PYS)

.SUFFIXES : .ipynb .pdf .rst .py

%.pdf : %.rst
	rst2pdf -o $@ $<

%.rst : %.ipynb
	ipython nbconvert --to rst --output $(@:.rst=) $<

%.py : %.ipynb
	ipython nbconvert --to python --output $(@:.py=) $<
