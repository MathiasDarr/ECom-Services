#!/bin/bash

if [[ $1 == 'aws' ]]
then
  aws logs describe-log-groups
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 logs describe-log-groups
else
    echo "choose either local or aws"
fi
