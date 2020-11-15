#!/bin/bash

aws cloudformation deploy --template redshift_template.yml \
  --stack-name redshift-stack \
  --parameter-overrides DataBucketName=dakobed-redshift-cluster \
  --capabilities CAPABILITY_IAM
