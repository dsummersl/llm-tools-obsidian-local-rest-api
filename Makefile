ruff-lint:
	ruff check .

ruff-fix:
	ruff check . --fix

test:
	pytest

lint-test: ruff-lint test
	@echo "Linting and tests completed."
