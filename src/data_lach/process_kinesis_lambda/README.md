### Processing Kinesis Stream With Lambda Function ###

The SAM application defined in this directory defines the following resources
* Kinesis Stream
* Lambda function 
    - reads the kinesis payload
    - logs the payload
* Eventstream mapping 

docker-compose -f localstack-compose.yaml up --build 

## How to deploy the application? ## 
#### Run localstack environment (from the root directory) ####
* docker-compose -f localstack-compose.yaml up --build

### package & build the SAM template to local ###
* bash deploy.sh local


### Write to kinesis stream using boto3, triggering lambda function ###
* python3 write_to_kinesis_stream.py 

### Accessing lambda logs from CLI  ###
* bash scripts/get_most_recent_logstream.sh local 

