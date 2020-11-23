import json
import os
import boto3


# import requests

dynamodb = boto3.resource('dynamodb') if os.getenv('deployment') != 'localstack' else \
    boto3.resource('dynamodb', endpoint_url= 'http://{}:4566'.format('localhost'))

# dynamodb = boto3.resource('dynamodb') if os.getenv('deployment') != 'localstack' else \
#     boto3.resource('dynamodb', endpoint_url= 'http://localhost:4566') .format(os.getenv('LOCALSTACK_HOSTNAME')))


def scan_products_table():
    table = dynamodb.Table('Products')
    scan_results = table.scan()
    return scan_results['Items']


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    items = scan_products_table()

    return {
        "statusCode": 200,
        "body": items
    }
