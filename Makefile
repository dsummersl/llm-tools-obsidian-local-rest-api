ruff-lint:
	ruff check .

ruff-fix:
	ruff check . --fix

test:
	pytest

ci: ruff-lint test
	@echo "Linting and tests completed."
