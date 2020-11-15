#!/bin/bash

if [[ $1 == 'aws' ]]
then
  aws cloudformation deploy --template stacks/aws/vpc/vpc_template.yml --stack-name vpc-stack
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 cloudformation deploy \
       --template stacks/aws/vpc/vpc_template.yml \
       --stack-name vpc-stack
else
    echo "choose either local or aws"
fi

