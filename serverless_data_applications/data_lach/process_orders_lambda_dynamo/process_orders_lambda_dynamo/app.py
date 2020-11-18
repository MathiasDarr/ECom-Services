import json
import base64
import boto3
import os


s3 = boto3.resource('s3') if os.getenv('deployment') != 'localstack' else \
    boto3.resource('s3', endpoint_url= 'http://{}:4566'.format(os.getenv('LOCALSTACK_HOSTNAME')))


# def write_order_to_dynamoDB(data):
#     for record in data:


def lambda_handler(event, context):
    """Lambda function processes
    Parameters
    ----------
    event: dict, required
        Kinesis event
    context: object, required
        Lambda Context runtime methods and attributes
    Returns
    ------
    """

    data = [base64.b64decode(record["kinesis"]["data"]).decode("utf-8") for record in event["Records"]]
    # write_order_to_dynamoDB(data)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
