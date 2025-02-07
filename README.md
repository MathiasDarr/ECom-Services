### Data Analytics & Engineering ###

This repository contains demonstrations of data engineering 

### This repository contains ###
* Processing with AWS Kinesis Streams, Kinesis Firehose & Lambda
    * [process kinesis stream with lambda](src/data_lach/process_kinesis_lambda/README.md)
        - SAM serverless application template deploys kinesis stream, lambda function & necessary roles
* Demonstration of Hive
    - Hive deployed w/ docker-compose, 
        - Load data into a Hive table & demonstate queries
* Demonstration of moving data into redshift
    - CloudFormation templates for deploying VPC & Redshift cluster
         - Deploy VPC w/ two public & two private subnets
         - Deploy redshift cluster in the VPC    
    - Installed SQL Workbench/J

* Scripts
    - Wrappers for AWS CLI

* Docker compose files
    - Hive
    - AWS local stack
