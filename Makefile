check:
	pytest tests --co
	ruff check .
	ruff format . --check

format:
	ruff format .
	ruff check . --fix --unsafe-fixes