.PHONY: setup_docs build_docs docs

install:
	pip install .

reinstall:
	pip uninstall tc-shortener -y
	pip install .

setup:
	@pip install -e .[tests]

setup_docs:
	pip install -r docs/requirements.txt

build_docs:
	cd docs && make html

docs: setup_docs build_docs
	python -mwebbrowser file:///`pwd`/docs/_build/html/index.html

pyvows_run:
	@pyvows -vvv --profile --cover --cover-package=tc_shortener --cover-omit=tc_shortener/storages/redis_storage.py vows/
