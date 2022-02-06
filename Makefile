source := ${wildcard ./jsonfeed/*.py}
tests := ${wildcard tests/*.py}

.PHONY: all lint test audit docs clean

all: lint test docs

lint: $(source) $(tests)
	flake8 . --count --max-complexity=10 --statistics

test: $(source) $(tests)
	pytest

audit:
	python -m pip_audit --strict --requirement requirements.txt

docs: docs/index.html
docs/index.html: $(source) README.md
	pdoc --docformat "restructuredtext" ./jsonfeed/main.py -o docs
	mv docs/jsonfeed/main.html docs/index.html
	rmdir docs/jsonfeed
	rm docs/search.json

clean:
	rm -rf build dist
	rm -rf __pycache__ **/__pycache__
	rm -rf *.pyc **/*.pyc
	rm -rf jsonfeed.egg-info