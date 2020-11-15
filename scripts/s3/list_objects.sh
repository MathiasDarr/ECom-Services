#!/bin/bash

s3-firehose

if [[ -z $2 ]]

then
 aws  --endpoint-url=http://localhost:4566 s3 ls s3://s3-firehose
else


if [[ $1 == 'aws' ]]
then
  aws s3 mb s3://$2
elif [[ $1 == 'local' ]]
then
  aws  --endpoint-url=http://localhost:4566 s3 ls
else
    echo "choose either local or aws"
fi
