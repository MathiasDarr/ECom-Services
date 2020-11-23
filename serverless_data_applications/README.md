### Serverless Applications ###


### Connecting to local dynamodb running ing localstack ###
* create a network docker
    - network create local-api-network


* This directory contains serverless applications 

sam init --runtime python3.7 --app-template hello-world --name products-query-api

sam init --runtime python3.7 --app-template hello-world --name query-api


RUN DYNAMO LOCALLY
docker network create local-api-network
docker run -d -p 8000:8000 --network=local-api-network --name dynamo-local amazon/dynamodb-local

aws dynamodb list-tables --endpoint-url http://localhost:8000