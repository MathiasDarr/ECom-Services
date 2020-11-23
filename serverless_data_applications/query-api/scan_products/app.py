import json
import boto3
# import requests

dynamodb = boto3.client('dynamodb', endpoint_url='http://dynamo-local:8000')
dynamo_resource = boto3.resource('dynamodb', endpoint_url='http://dynamo-local:8000')

def scan_products():
    table = dynamo_resource.Table('Products')
    scan_results = table.scan()
    return scan_results['Items']


def lambda_handler(event, context):
    """

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
    products = scan_products()
    for product in products:
        product['price'] = float(product['price'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": products
            # "location": ip.text.replace("\n", "")
        }),
    }
