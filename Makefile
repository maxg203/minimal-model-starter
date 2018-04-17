up:
	docker-compose up -d --build

test:
	docker exec -it website pytest -vv

test_watch:
	docker exec -it website ptw

test_coverage:
	docker exec -it website pytest --cov=.

shell:
	docker exec -it website bash

badge:
	docker exec -it website pytest --cov=.
	docker exec -it website coverage-badge -o coverage.svg -f
