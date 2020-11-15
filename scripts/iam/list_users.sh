#!/bin/bash


if [[ $1 == 'aws' ]]
then
  aws iam list-users
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 iam list-users
else
    echo "choose either local or aws"
fi
