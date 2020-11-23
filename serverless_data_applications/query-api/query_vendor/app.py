import json
import boto3
from boto3.dynamodb.conditions import Key


dynamo_resource = boto3.resource('dynamodb')  # , endpoint_url='http://dynamo-local:8000')
TABLE_NAME = 'Products'
table = dynamo_resource.Table(TABLE_NAME)


def query_products_by_vendor(vendor):
    products = table.query(
        KeyConditionExpression=Key('vendor').eq(vendor)
    )
    products = products['Items']
    for product in products:
        product['price'] = float(product['price'])
    return products


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

    vendor = event['pathParameters']['vendor_id']
    products = query_products_by_vendor(vendor)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "products": str(products),
            # "type": str(event.keys())
            # "location": ip.text.replace("\n", "")
        }),
    }
