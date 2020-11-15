#!/bin/bash
if [[ $1 == 'aws' ]]
then
  aws cloudformation describe-stack-events --stack-name $2
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 cloudformation describe-stack-events --stack-name $2
else
    echo "choose either local or aws"
fi



