### ECommerce MicroServices ###

##### This directory contains a Spring Boot microservices project. #####
## The microservices are implemented using the following technologies ##
* Spring Boot
* Kafka, spring cloud Kafka binder, avro serialization
* DynamoDB & Java AWS SDK
* Ehcache
* Jmeter for performance testing 

### Microservices ###

* producers 
   - This module contains classes with main methods that populate the Kafka-topics.
* orders-service
    - expose endpoints for placing orders
* inventory-service
    - expose endpoints for querying the product catalog
* DynamoDB backend


### Project Dependencies ###
* a local dynamoDB environment or AWS account
* Java 11 & maven (if compiling & running natively instead of through Docker)
* docker-compose

### How to run the project ###
* Ensure that the DynamoDB products table has been populated.  This can be done following the instructions in the data_model/products directory. 
* Launch zookeeper, kafka broker & schema registry in docker
    * docker-compose -f kafka-compose.yaml up 
* Compile 
    * mvn clean packge
* Populate the products kafka topic
    * java -jar producers/target/producers-1.0-SNAPSHOT.jar
     
     
     