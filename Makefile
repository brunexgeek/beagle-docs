# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Beagle
SOURCEDIR     = $(shell pwd)
BUILDDIR      = $(shell pwd)/_build
SCSS          = $(SOURCEDIR)/_theme/beagle/scss/beagle.scss
CSS           = $(SOURCEDIR)/_theme/beagle/static/beagle.css

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html: $(CSS) Makefile
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(CSS): $(SCSS)
	scss -t expanded $(SCSS) $(CSS)
	cp $(CSS) $(BUILDDIR)/html/_static

.PHONY: help Makefile html

