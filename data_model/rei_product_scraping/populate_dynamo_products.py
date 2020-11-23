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


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
table = dynamodb.Table('Products')

CSV_DIRECTORY = 'products'
csv_files = []
for file in os.listdir(CSV_DIRECTORY):
    file_path = 'products/{}'.format(file)
    if file_path.split('.')[-1] =='csv':
        csv_files.append(file_path)
        print(file_path)

for file in csv_files:
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_product(row)
