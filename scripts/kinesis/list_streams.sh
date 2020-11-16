#!/bin/bash

if [[ $1 == 'aws' ]]
then
    aws kinesis list-streams
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 kinesis list-streams
else
    echo "choose either local or aws"
fi
