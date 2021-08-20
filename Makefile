SOURCE_GLOB=$(wildcard bin/*.py src/**/*.py tests/**/*.py)
IGNORE_PEP=E203,E221,E241,E272,E501,F811

export PYTHONPATH=src/

.PHONY: all
all : clean lint

.PHONY: clean
clean:
	rm -fr dist/*

.PHONY: lint
lint: pylint pycodestyle flake8 mypy pytype

.PHONY: pylint
pylint:
	pylint \
		--load-plugins pylint_quotes \
		--disable W0511,C0302 \
		$(SOURCE_GLOB)

.PHONY: pycodestyle
pycodestyle:
	pycodestyle \
		--statistics \
		--count \
		--ignore="${IGNORE_PEP}" \
		$(SOURCE_GLOB)

.PHONY: flake8
flake8:
	flake8 \
		--ignore="${IGNORE_PEP}" \
		$(SOURCE_GLOB)

.PHONY: install
install:
	pip3 install -r requirements.txt
	pip3 install -r requirements-dev.txt
	# install pre-commit related hook scripts
	$(MAKE) install-git-hook

.PHONY: pytest
pytest:
	pytest src/ tests/

.PHONY: test-unit
test-unit: pytest

.PHONY: test
test: lint pytest

code:
	code .

.PHONY: run
run:
	python3 src/main.py
