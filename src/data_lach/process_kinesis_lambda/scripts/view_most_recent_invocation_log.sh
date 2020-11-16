#!/bin/bash

bash scripts/describe_log_stream.sh local | grep logStreamName  | awk -F'"' '$0=$4'  #> lognames.txt

#awslocal logs get-log-events --log-group-name /aws/lambda/ProcessKinesisFunction --log-stream-name 2020/11/16/[LATEST]9c0173e0
