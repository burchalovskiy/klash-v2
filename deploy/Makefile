PROJECT_NAME := vin_wiki
COMPOSE_FILE := docker-compose.yml
DOCKER_REGISTRY := harbor.b2bpolis.ru
DOCKER_USER :=
DOCKER_PASSWORD :=


.PHONY: login logout pull start status stop logs reload_web

login:
	${INFO} "Logging into Docker registry $(DOCKER_REGISTRY)..."
	@ docker login -u $(DOCKER_USER) -p $(DOCKER_PASSWORD)
	${INFO} "Logged into Docker registry $(DOCKER_REGISTRY)"

logout:
	${INFO} "Logging out of Docker registry $(DOCKER_REGISTRY)..."
	@ docker logout $(DOCKER_REGISTRY)
	${INFO} "Logged out of Docker registry $(DOCKER_REGISTRY)"

pull: login
	${INFO} "Pulling project..."
	@ docker-compose -p $(PROJECT_NAME) -f $(COMPOSE_FILE) pull
	${INFO} "Done pulling project"

start:
	${INFO} "Running project..."
	@ docker-compose -p $(PROJECT_NAME) -f $(COMPOSE_FILE) up -d

reload_web:
	@ /usr/local/bin/docker-compose -p $(PROJECT_NAME) -f $(COMPOSE_FILE) exec web bash -c 'nginx -t && service nginx reload'

status:
	@ docker-compose -p $(PROJECT_NAME) -f $(COMPOSE_FILE) ps

stop:
	${INFO} "Stopping project..."
	@ docker-compose -p $(PROJECT_NAME) -f $(COMPOSE_FILE) down

logs:
	${INFO} "Logging project..."
	@ docker-compose -p $(PROJECT_NAME) -f $(COMPOSE_FILE) logs -f --tail=32


YELLOW := "\e[1;33m"
NC := "\e[0m"

INFO := @bash -c '\
    printf $(YELLOW); \
    echo "=> $$1"; \
    printf $(NC)' VALUE