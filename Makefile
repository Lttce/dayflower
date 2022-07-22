.PHONY: all
all:

.PHONY: dev
dev:
	poetry run uvicorn app.main:api --reload

.PHONY: test
test:
	poetry run pytest
