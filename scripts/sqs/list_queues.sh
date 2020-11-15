#!/bin/bash

if [[ $1 == 'aws' ]]
then
  aws sqs list-queues
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 sqs list-queues
else
    echo "choose either local or aws"
fi