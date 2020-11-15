#!/bin/bash

if [[ -z $2 ]]
then
  stackname=data=process-stack
else
  stackname=$2
fi


if [[ $1 == 'aws' ]]
then
  aws cloudformation list-stack-resources --stack-name ${stackname}
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 cloudformation list-stack-resources --stack-name ${stackname}
else
    echo "choose either local or aws"
fi



