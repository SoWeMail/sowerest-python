.PHONY: venv install test-install test clean nopyc

venv:
	@python --version || (echo "Python is not installed, please install Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install -r install-requirements.pip

test:
	. venv/bin/activate; pip install -r test-requirements.pip; python -m unittest discover -v

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
