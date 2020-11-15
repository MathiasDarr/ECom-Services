#!/bin/bash

if [[ -z $2 ]]
then
  stackname=orders-bucket-stack
else
  stackname=$2
fi

echo ${stackname}


if [[ $1 == 'aws' ]]
then
    aws cloudformation deploy \
      --template-file template.yaml \
      --stack-name ${stackname} \
      --capabilities CAPABILITY_NAMED_IAM

elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 cloudformation deploy \
      --template-file template.yaml \
      --stack-name ${stackname} \
      --capabilities CAPABILITY_NAMED_IAM
else
    echo "choose either local or aws"
fi
