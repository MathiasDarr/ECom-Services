"""
This script writes two records to Kinesis, triggering the Lambda function

"""
# !/usr/bin/env python3

import boto3
import json
import time

my_stream_name = 'OrdersStream'
# kinesis_client = boto3.client('kinesis', region_name='us-west-2')
kinesis_client = boto3.client('kinesis', endpoint_url='http://localhost:4566')


payload = {
    'prop': str(5),
    'timestamp': str(time.time()),
    'thing_id': 1
}

payload2 = {
    'prop': str(2),
    'timestamp': str(time.time()),
    'thing_id': 232
}

put_response = kinesis_client.put_record(
    StreamName=my_stream_name,
    Data=json.dumps(payload),
    PartitionKey=str(5))
print(put_response)

put_response2 = kinesis_client.put_record(
    StreamName=my_stream_name,
    Data=json.dumps(payload2),
    PartitionKey=str(2))
print(put_response2)
