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
            'category': product['category']
        }
    )


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
table = dynamodb.Table('Products')

csv_directory = 'data'
product_csv_files = ['{}/{}'.format(csv_directory, file) for file in os.listdir(csv_directory)]
keys = ['name', 'vendor', 'colors', 'price', 'url', 'category']

for file in product_csv_files:
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_product(row)
