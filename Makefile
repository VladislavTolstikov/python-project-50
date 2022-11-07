gendiff-help:
	poetry run gendiff -h

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

yaml:
	poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yml

coverage:
	poetry run pytest --cov --cov-report xml

build:
	poetry build

install:
	python3 -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall