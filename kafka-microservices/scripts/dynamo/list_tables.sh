#!/bin/bash



if [[ $1 == 'aws' ]]
then
    aws dynamodb list-tables
elif [[ $1 == 'local' ]]
then
  aws dynamodb list-tables --endpoint-url http://localhost:4566
else
    echo "choose either local or aws"
fi