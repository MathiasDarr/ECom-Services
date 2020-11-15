#!/bin/bash

if [[ $1 == 'aws' ]]
then
  aws lambda list-functions
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 lambda list-functions
else
    echo "choose either local or aws"
fi
