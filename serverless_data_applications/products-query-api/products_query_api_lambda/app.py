import json
import os
import boto3


# import requests

# dynamodb = boto3.resource('dynamodb') if os.getenv('deployment') != 'localstack' else \
#     boto3.resource('dynamodb', endpoint_url= 'http://{}:4566'.format('localhost'))

# dynamodb = boto3.resource('dynamodb') if os.getenv('deployment') != 'localstack' else \
#     boto3.resource('dynamodb', endpoint_url= 'http://localhost:4566') .format(os.getenv('LOCALSTACK_HOSTNAME')))
LOCALSTACK_HOSTNAME = '172.17.0.2'
# dynamodb = boto3.client('dynamodb', endpoint_url='http://dynamo-local:8000') #.format(LOCALSTACK_HOSTNAME))


def scan_products_table():
    dynamodb.list_tables()
    # table = dynamodb.Table('Products')
    # scan_results = table.scan()
    # return scan_results['Items']


def lambda_handler(event, context):
    """Sample pure Lambda function

    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    # items = scan_products_table()
    # dynamodb = boto3.client('dynamodb', endpoint_url='http://dynamo-local:8000')
    return {
        "statusCode": 200,
        "body": 'hello'
    }
