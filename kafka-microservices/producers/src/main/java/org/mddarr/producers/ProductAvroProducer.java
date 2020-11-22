package org.mddarr.producers;

import com.amazonaws.auth.DefaultAWSCredentialsProviderChain;
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

    static AmazonDynamoDB client = amazonDynamoDB();
    static DynamoDB dynamoDB = new DynamoDB(client);
    static String tableName = "Products";

    public static void main(String[] args) {
        scanProductsTable();
    }

    public static AmazonDynamoDB amazonDynamoDB() {
        /*
        This method returns an instance of the class AmazonDynamoDB with a configuration pointing to the local dynamoDB endpoint
         */
        return  AmazonDynamoDBClientBuilder.standard()
                .withEndpointConfiguration(
                        new AwsClientBuilder.EndpointConfiguration("http://localhost:4566","us-west-"))
                .withCredentials(new DefaultAWSCredentialsProviderChain())
                .build();
    }


    private static void scanProductsTable() {
        /*
        This method scans the dynamodb products table.
         */

        DefaultKafkaProducerFactory<String, AvroProduct> pf1 = getKafkaProducerFactory();
        KafkaTemplate<String, AvroProduct> template1 = new KafkaTemplate<>(pf1, true);
        template1.setDefaultTopic("Products-Kafka-Topic");

        Table table = dynamoDB.getTable(tableName);
        ItemCollection<ScanOutcome> items = table.scan();
        System.out.println("Scan of " + tableName );




        for (Item item : items) {
            AvroProduct product = new AvroProduct(item.getString("vendor"),item.getString("productName"), item.getDouble("price"),0L);
            template1.sendDefault(null, product);
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

    public static void populateProductsKafkaTopic(){

    }
}
