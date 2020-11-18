import boto3
import json
client = boto3.client('kinesis', endpoint_url='http://localhost:4566')
#client = boto3.client('kinesis')
response = client.describe_stream(StreamName='OrdersStream')

## Writing to kinesis stream
## What does the partition key do?

stream_name = 'OrdersStream'
client.put_record(StreamName='OrdersStream', Data = json.dumps({'first':1}), PartitionKey='first1')




response = client.describe_stream(StreamName=stream_name)
shard_id = response['StreamDescription']['Shards'][0]['ShardId']
shard_iterator_response = client.get_shard_iterator(StreamName=stream_name, ShardId=shard_id, ShardIteratorType='TRIM_HORIZON')

shard_iterator = shard_iterator_response['ShardIterator']
records = client.get_records(ShardIterator=shard_iterator, Limit = 1)


## Reading records from the kinesis stream


# my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']