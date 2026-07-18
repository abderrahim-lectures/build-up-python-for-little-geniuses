.PHONY: pdf clean

pdf:
	cd .. && latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=build/pdf build-up.tex

clean:
	cd .. && latexmk -C -output-directory=build/pdf build-up.tex
