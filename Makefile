gendiff-help:
	poetry run gendiff -h

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

go:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

coverage:
	poetry run pytest --cov