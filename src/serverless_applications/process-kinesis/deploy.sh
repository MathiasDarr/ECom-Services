#!/bin/bash

if [[ -z $2 ]]
then
  stackname=data=process-stack
else
  stackname=$2
fi

echo ${stackname}

sam package \
  --template-file template.yaml \
  --s3-bucket "dakobed-serverless-apis" \
  --output-template-file package.yaml

if [[ $1 == 'aws' ]]
then
    aws cloudformation deploy \
      --template-file package.yaml \
      --stack-name ${stackname} \
      --capabilities CAPABILITY_NAMED_IAM

elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 cloudformation deploy \
      --template-file package.yaml \
      --stack-name ${stackname} \
      --capabilities CAPABILITY_NAMED_IAM
else
    echo "choose either local or aws"
fi
