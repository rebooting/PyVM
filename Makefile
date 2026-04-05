.PHONY: run


run:
	python3 -m pyvm.main

test:
	python3 -m unittest discover -s tests