import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'OrdersStream'

kinesis_client = boto3.client('kinesis', endpoint_url='http://localhost:4566')

property_value = random.randint(40, 120)
property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
thing_id = 'aa-bb'


payload = {
    'prop': str(property_value),
    'timestamp': str(property_timestamp),
    'thing_id': thing_id
}

print(payload)

put_response = kinesis_client.put_record(
    StreamName=my_stream_name,
    Data=json.dumps(payload),
    PartitionKey=thing_id)

print(put_response)