import json
import base64
import boto3

# import requests


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

    print("decoded data")

    for record in event["Records"]:
        decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        print(decoded_data)



    # s3 = boto3.resource('s3')
    # s3object = s3.Object('dakobed-lach-orders', 'your_file.json')
    # s3object.put(
    #     Body=(bytes(json.dumps({'data':1}).encode('UTF-8')))
    # )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
