#!/bin/bash

if [[ $1 == 'aws' ]]
then
  aws logs describe-log-streams --log-group-name /aws/lambda/ProcessKinesisFunction
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 logs describe-log-streams --log-group-name /aws/lambda/ProcessKinesisFunction
else
    echo "choose either local or aws"
fi



