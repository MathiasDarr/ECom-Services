### Kinesis-Firehose-S3 ###


This serverless application makes use of the following components
The Cloud formation tempalate deploys a stack with the following resources
    - Lambda function
    - Kinesis firehose delivery stream  to


CAPABILITY_NAMED_IAM vs CAPABILITY_IAM

s3 = boto3.resource('s3') if os.getenv('deployment') != 'localstack' else \
    boto3.resource('s3', endpoint_url= 'http://{}:4566'.format(os.getenv('LOCALSTACK_HOSTNAME')))