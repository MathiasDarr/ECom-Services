package org.mddarr.producers;

import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.*;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.ScanRequest;
import com.amazonaws.services.dynamodbv2.model.ScanResult;
import io.confluent.kafka.serializers.AbstractKafkaAvroSerDeConfig;
import io.confluent.kafka.serializers.KafkaAvroSerializer;
import io.confluent.kafka.streams.serdes.avro.SpecificAvroSerializer;
import org.apache.kafka.clients.producer.ProducerConfig;

import org.mddarr.products.AvroProduct;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;

import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.util.*;

public class ProductAvroProducer {

    static AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
    static DynamoDB dynamoDB = new DynamoDB(client);
    static String tableName = "Products";

    public static void main(String[] args) {
        populateProductsKafkaTopic();
    }


    private static void scanProductsTable() {

        Table table = dynamoDB.getTable(tableName);

//        Map<String, Object> expressionAttributeValues = new HashMap<String, Object>();
//        expressionAttributeValues.put(":pr", 100);

        ItemCollection<ScanOutcome> items = table.scan(); //"price < 200", // FilterExpression
//                "Id, Title, ProductCategory, Price", // ProjectionExpression
//                null, // ExpressionAttributeNames - not used in this example
//                expressionAttributeValues);

        System.out.println("Scan of " + tableName );

        for (Item item : items) {
            System.out.println(item.toJSONPretty());
        }

    }

    public static DefaultKafkaProducerFactory<String, AvroProduct> getKafkaProducerFactory(){
        /*
        Kafka configuration
         */

        final Map<String, String> serdeConfig = Collections.singletonMap(
                AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");

        final SpecificAvroSerializer<AvroProduct> productSerializer = new SpecificAvroSerializer<>();
        productSerializer.configure(serdeConfig, false);

        Map<String, Object> props = new HashMap<>();
        props.put(AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.RETRIES_CONFIG, 0);
        props.put(ProducerConfig.BATCH_SIZE_CONFIG, 16384);
        props.put(ProducerConfig.LINGER_MS_CONFIG, 1);
        props.put(ProducerConfig.BUFFER_MEMORY_CONFIG, 33554432);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, productSerializer.getClass());

        DefaultKafkaProducerFactory<String, AvroProduct> pf1 = new DefaultKafkaProducerFactory<>(props);
        return pf1;
    }

    public static DynamoDB getDynamoDB(){
        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
                .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("http://localhost:4566", "us-west-2"))
                .build();
        return new DynamoDB(client);
    }

    public static void populateProductsKafkaTopic(){

        DefaultKafkaProducerFactory<String, AvroProduct> pf1 = getKafkaProducerFactory();
        KafkaTemplate<String, AvroProduct> template1 = new KafkaTemplate<>(pf1, true);
        template1.setDefaultTopic("Products-Kafka-Topic");

        scanProductsTable();

//        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
//
//        ScanRequest scanRequest = new ScanRequest()
//                .withTableName("Reply");
//
//        ScanResult result = client.scan(scanRequest);
//        for (Map<String, AttributeValue> item : result.getItems()){
//            printItem(item);
//        }



    }
}
