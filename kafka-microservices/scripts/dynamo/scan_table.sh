#!/bin/bash

if [[ $1 == 'aws' ]]
then
    aws dynamodb scan --table-name $2
elif [[ $1 == 'local' ]]
then
  aws dynamodb scan --table-name $2 --endpoint-url http://localhost:4566
else
    echo "choose either local or aws"
fi

