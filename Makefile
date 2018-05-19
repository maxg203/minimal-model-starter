restart:
	docker-compose down
	docker-compose up -d

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

redis:
	docker exec -it redis bash

worker:
	docker exec -it worker bash

badge:
	docker exec -it website pytest --cov=.
	docker exec -it website coverage-badge -o coverage.svg -f
