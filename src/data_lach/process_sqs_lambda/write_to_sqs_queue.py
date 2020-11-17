"""
This script will write a message to the SQS queue defined in the template


"""
# !/usr/bin/env python3

import boto3
import json

# Create SQS client


def write_message_to_queue(sqs_client, queue_name):
    queue_url = sqs_client.get_queue_url(QueueName=queue_name)['QueueUrl']

    # Send message to SQS queue
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )

    print(response['MessageId'])

if __name__ == '__main__':
    # sqs_client = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-west-2')
    sqs_client = boto3.client('sqs', region_name='us-west-2')
    write_message_to_queue(sqs_client, 'TransformQueue')