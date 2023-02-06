.PHONY: install format lint test sec

install:
	@poetry install
format:
	@isort .
	@blue .
lint:
	@blue . --check
	@isort . --check
test:
	@pytest -v
sec:
	@pip-audit