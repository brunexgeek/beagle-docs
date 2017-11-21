# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Beagle
SOURCEDIR     = $(shell pwd)
BUILDDIR      = $(shell pwd)/_build
SCSS          = $(SOURCEDIR)/_theme/beagle/scss/beagle.scss
CSS           = $(SOURCEDIR)/_theme/beagle/static/beagle.css
GSRC          = $(SOURCEDIR)/language/grammar.txt
GDST          = $(SOURCEDIR)/language/grammar.rst

html: $(CSS) $(GDST) Makefile
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(CSS): $(SCSS)
	scss -t expanded $(SCSS) $(CSS)
	cp $(CSS) $(BUILDDIR)/html/_static

$(GDST): $(GSRC)
	./grammar2rst.py

.PHONY: help Makefile html

