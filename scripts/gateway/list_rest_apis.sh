#!/bin/bash

if [[ $1 == 'aws' ]]
then
  aws  apigateway get-rest-apis

elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 apigateway get-rest-apis
else
    echo "choose either local or aws"
fi
