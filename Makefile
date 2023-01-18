include .env
export

shell:
	poetry shell

prepare:
	poetry install || true

run:
	poetry run uvicorn api.__main__:app --host 0.0.0.0 --port ${FASTAPI_PORT} --log-level critical

build:
	docker build -t myna-labs-character-api --no-cache .

down:
	docker kill myna-labs-character-api

run-docker:
	docker container rm myna-labs-character-api || true
	docker run --name myna-labs-character-api -p ${FASTAPI_PORT}:${FASTAPI_PORT} --network many-labs-network myna-labs-character-api