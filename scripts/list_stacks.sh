#!/bin/bash



if [[ $1 == 'aws' ]]
then
  aws cloudformation list-stacks
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 cloudformation list-stacks
else
    echo "choose either local or aws"
fi
