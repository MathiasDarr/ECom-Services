#!/bin/bash

logstreamname=$(bash scripts/describe_log_stream.sh local | grep logStreamName  | awk -F'"' '$0=$4' | tail -n 1)
echo ${logstreamname}

if [[ $1 == 'aws' ]]
then
  aws logs get-log-events --log-group-name /aws/lambda/ProcessKinesisFunction --log-stream-name ${logstreamname}
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 logs get-log-events --log-group-name /aws/lambda/ProcessKinesisFunction --log-stream-name ${logstreamname}
else
    echo "choose either local or aws"
fi