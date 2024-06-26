#!/bin/bash

docker tag planet-facts-service:latest 533266979424.dkr.ecr.us-east-1.amazonaws.com/planet-facts-service:latest
docker push 533266979424.dkr.ecr.us-east-1.amazonaws.com/planet-facts-service:latest
