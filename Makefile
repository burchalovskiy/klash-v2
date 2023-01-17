-include docker.env

IMAGE_PATH := $(DOCKER_REGISTRY)/klash-app
DOCKERFILE := ./docker/build/Dockerfile

TAG_NAME ?= $(shell git rev-parse --abbrev-ref HEAD | cut -d/ -f2)
VCS_REF = $(shell git rev-parse --short HEAD)
BUILD_DATE = $(shell date -u +"%Y-%m-%dT%H:%M:%SZ")

.login:
	${INFO} "Logging in to Registry..."
	@docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
	${INFO} "Logged in"

.PHONY: build
build: .login
	${INFO} "Building app"
	@DOCKER_BUILDKIT=1 docker buildx build  --platform=linux/amd64 -f "${DOCKERFILE}" -t "${IMAGE_PATH}:${TAG_NAME}" --progress=plain --build-arg TAG_NAME="${TAG_NAME}" --build-arg VCS_REF="${VCS_REF}" --build-arg BUILD_DATE="${BUILD_DATE}" --target runtime-image .
	${INFO} "Built"
	${INFO} "Pushing app to docker registry..."
	@docker push "${IMAGE_PATH}:${TAG_NAME}"
	${INFO} "Pushed"


YELLOW := "\e[1;33m"
NC := "\e[0m"

INFO := @sh -c '\
    printf $(YELLOW); \
    echo "=> $$1"; \
    printf $(NC)' VALUE
