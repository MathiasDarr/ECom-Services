import boto3

client = boto3.client('kinesis', endpoint_url='http://localhost:4567')
client.list_streams()