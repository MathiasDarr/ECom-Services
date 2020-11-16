#!/bin/bash


if [[ $1 == 'aws' ]]
then
  aws cloudformation delete-stack --stack-name  ${stackname}
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 logs get-log-events --log-group-name ProcessKinesisFunction
else
    echo "choose either local or aws"
fi
