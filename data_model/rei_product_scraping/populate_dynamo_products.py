"""
This script reads the csv files written by the script scrape_rei_products.py and inserts the products into the Products
dynamoDB table.
"""
# !/usr/bin/env python3

import csv
import os
import boto3
from boto3.dynamodb.types import Decimal


def insert_product(product):
    return table.put_item(
        Item={
            'vendor': product['vendor'],
            'productName': product['name'],
            'colors': product['colors'],
            'price': Decimal(product['price']),
            'category': product['category'],
            'image_url': product['image_url']
        }
    )

def create_products_table():
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


# dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:4566")
dynamodb = boto3.resource('dynamodb')  # ,endpoint_url="http://localhost:8000")
# create_products_table()
table = dynamodb.Table('Products')

CSV_DIRECTORY = 'products'
csv_files = []
for file in os.listdir(CSV_DIRECTORY):
    file_path = 'products/{}'.format(file)
    if file_path.split('.')[-1] == 'csv':
        csv_files.append(file_path)

for file in csv_files:
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_product(row)
