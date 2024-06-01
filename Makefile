PROJECT_NAME=nginx-influx-relay
COMPOSE_FILE=docker-compose.yml

include env.local

docker-run:
	docker-compose -f ${COMPOSE_FILE} up -d

docker-up:
	docker-compose -f ${COMPOSE_FILE} up -d

docker-down:
	docker-compose -f docker-compose.yml down

docker-clean:
	docker-compose -f ${COMPOSE_FILE} down --rmi all