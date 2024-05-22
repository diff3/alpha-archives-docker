# Well documented Makefiles

ifeq (${COMPOSE_FILE},)
    COMPOSE_FILE := docker-compose.yaml
endif

DEFAULT_GOAL := help

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_\.%-]+:.*?##/ { printf "  \033[36m%-40s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ [Docker Compose]
start: ## Spin up the containers
	docker compose --file ${COMPOSE_FILE} up -d

build-start: ## Build and spin up the containers
	docker compose --file ${COMPOSE_FILE} up -d --build 

stop: ## Shut down the containers, default all but can be specified with "make stop ARGS=SERVICE"
	docker compose --file ${COMPOSE_FILE} down

restart: ## Restart all the containers
	docker compose --file ${COMPOSE_FILE} restart

logs: ## Docker logs
	docker compose --file ${COMPOSE_FILE} logs --follow

logs.%: %.dockerfile ## Docker logs for a running container associated with a dockerfile
	echo $< | sed 's;\.dockerfile;;' | xargs -o docker compose --file ${COMPOSE_FILE} logs --follow

build-all: ## Build all docker images
	docker compose --file ${COMPOSE_FILE} build

##@ [Docker]
log: ## Docker log, specified with "make log ARGS=CONTAINER
ifeq (${ARGS},)
	echo Usage: make logs ARGS=CONTAINER
else
	docker logs --follow $(ARGS)
endif

connect.%: %.dockerfile ## Connect to a running container associated with a dockerfile, "make connect.php"
	echo $< /bin/sh | sed 's;\.dockerfile;;' | xargs -o docker compose --file ${COMPOSE_FILE} exec -it

connect: ## Connect to a running container, "make connect ARGS=CONTAINER"
ifeq (${ARGS},)
	echo Usage: make connect ARGS=CONTAINER
else
	docker exec -it $(ARGS) /bin/sh
endif