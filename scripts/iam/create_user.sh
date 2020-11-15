#!/bin/bash

if [[ -z $2 ]]
then
  username=iam-user
else
  username=$2
fi


if [[ $1 == 'aws' ]]
then
  aws iam create-user --user-name $username
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 iam create-user --user-name $username
else
    echo "choose either local or aws"
fi

