run:
	python3 example.py

lint:
	black --check --diff .
	flake8 .
	mypy --strict .
	pytype .
