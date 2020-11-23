"""
This script creates the dynamoDB products table

"""
# !/usr/bin/env python3


import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')
try:
    resp = dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "vendor",
                "AttributeType": "S"
            },
            {
                "AttributeName": "productName",
                "AttributeType": "S"
            },
            {
                "AttributeName": "category",
                "AttributeType": "S"
            },
        ],
        TableName="Products",
        KeySchema=[
            {
                "AttributeName": "vendor",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "productName",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        },
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'categoryGSI',
                'KeySchema': [
                    {
                        'AttributeName': 'category',
                        'KeyType': 'HASH',
                    },
                ],
                'Projection': {
                    'ProjectionType': 'KEYS_ONLY',
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1,
                }
            },
        ],

    )

except Exception as e:
    print(e)

