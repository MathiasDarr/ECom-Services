#!/bin/bash


if [[ $1 == 'aws' ]]
then
    aws cloudformation deploy \
     --template stacks/aws/redshift/redshift_template.yaml \
     --stack-name redshift-stack \
     --parameter-overrides DataBucketName=dakobed-redshift-cluster \
     --capabilities CAPABILITY_IAM

elif [[ $1 == 'local' ]]
then
    echo "Localstack doesn't currently work for redshift queries ! "


#    aws  --endpoint-url=http://localhost:4566  cloudformation  deploy \
#      --template aws/redshift/redshift_template.yml \
#      --parameter-overrides DataBucketName=dakobed-redshift-cluster \
#      --stack-name redshift-stack  \
#      --capabilities CAPABILITY_IAM
#     --parameter-overrides DataBucketName=dakobed-redshift-cluster \
else
    echo "choose either local or aws"
fi
