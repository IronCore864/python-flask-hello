#!/bin/bash
docker build -t ironcore864/python-hello-flask .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push ironcore864/python-hello-flask
