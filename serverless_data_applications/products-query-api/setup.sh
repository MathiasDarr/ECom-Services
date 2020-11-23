#!/bin/bash

API_NAME=ProductsAPI
REGION=us-east-1
STAGE=test

#function fail() {
#    echo $2
#    exit $1
#}
#
#[ $? == 0 ] || fail 1 "Failed: AWS / lambda / create-function"



LAMBDA_FUNCTION=ProductsQueryFunction
LAMBDA_ARN=$(awslocal lambda list-functions --query "Functions[?FunctionName==\`${LAMBDA_FUNCTION}\`].FunctionArn" --output text --region ${REGION})

#echo ${LAMBDA_ARN}



#
API_ID=$(awslocal apigateway get-rest-apis --query "items[?name==\`${API_NAME}\`].id" --output text --region ${REGION})
#echo ${API_ID}

RESOURCE_ID=$(awslocal apigateway get-resources --rest-api-id ${API_ID})
#echo ${RESOURCE_ID}
PARENT_RESOURCE_ID=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/hello`].id' --output text --region ${REGION})
##
echo ${PARENT_RESOURCE_ID}


ENDPOINT_URL=$(awslocal cloudformation describe-stacks --stack-name products-api-stack-2 --query "Stacks[0].Outputs[?OutputKey=='ProductsApi'].OutputValue" --output text)
echo "THE ENDPOINT URL IS"
echo ${ENDPOINT_URL}