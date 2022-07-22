.PHONY: all
all:

.PHONY: dev
dev:
	poetry run uvicorn dayflower.main:api --reload

.PHONY: test
test:
	poetry run pytest
