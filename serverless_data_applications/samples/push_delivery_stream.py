import boto3
import json

# Create a boto client to use firehose service with specified endpoint
client = boto3.client("firehose")

# Just some data
data = {"name":"ruhshan", "attributes":["lazy", "crazy"]}

# Put record on the stream we created
client.put_record(Record={"Data":json.dumps(data)}, DeliveryStreamName="deliverystream")

