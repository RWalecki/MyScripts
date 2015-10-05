BUILDTEX=pdflatex \
		 -halt-on-error \
		--output-directory tests/build \
		-aux-directory=tests/build \
		tests/main.tex

prog:
	python tests/tests.py
	$(BUILDTEX)
	open /Applications/Preview.app
	open /Applications/Utilities/Terminal.app
