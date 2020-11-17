import json
import base64
import boto3
import os
# import requests

HOST = "http://71.212.158.210"
# Get the service resource
# To production it's not necessary inform the "endpoint_url" and "region_name"
s3 = boto3.resource('s3', endpoint_url= HOST + ":4566", region_name="us-west-2")



def write_data_to_s3():
    try:
        # if os.getenv('deployment') == 'localstack':
        #     s3 = boto3.resource('s3', endpoint_url='http://localhost:4566')
        # else:
        #     s3 = boto3.resource('s3')

        s3object = s3.Object('dakobed-lach-orders', 'first_data.json')
        s3object.put(
            Body=(bytes(json.dumps({"first": 1}).encode('UTF-8')))
        )
        print("Write data to s3.")
    except Exception as e:
        print(e)

def lambda_handler(event, context):
    """Sample pure Lambda function

s3 = boto3.resource('s3')
# s3object = s3.Object('dakobed-lach-orders', 'your_file.json')
# s3object.put(Body=(bytes(json.dumps({'data':1}).encode('UTF-8'))))


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



    write_data_to_s3()

    # print("CONTEXT")
    # print(str(context))
    #
    # for record in event["Records"]:
    #     decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
    #
    #
    # try:
    #     if os.getenv('deployment') == 'localstack':
    #         s3 = boto3.resource('s3', endpoint_url='http://localhost:4566')
    #     else:
    #         s3 = boto3.resource('s3')
    #
    #     s3object = s3.Object('dakobed-lach-orders', 'first_data.json')
    #     s3object.put(
    #         Body=(bytes(json.dumps({"first": 1}).encode('UTF-8')))
    #     )
    #     print("Write data to s3.")
    # except Exception as e:
    #     print(e)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
