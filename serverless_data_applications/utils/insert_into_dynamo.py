import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")

table = dynamodb.Table('Orders')
response = table.put_item(
    Item={
        'year': year,
        'title': title,
    }
)