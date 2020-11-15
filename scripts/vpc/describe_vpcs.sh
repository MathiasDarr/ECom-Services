#!/bin/bash


if [[ $1 == 'aws' ]]
then
    aws ec2 describe-vpcs

elif [[ $1 == 'local' ]]
then
    aws --endpoint-url=http://localhost:4566 ec2 describe-vpcs
else
    echo "choose either local or aws"
fi



