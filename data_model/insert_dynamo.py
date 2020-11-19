import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")

table = dynamodb.Table('Products')


def insert_product(product):
    return table.put_item(
        Item={
            'vendor': 'osprey',
            'croductName': 'df',
            'colors':  ['red','blue']

        }
    )
