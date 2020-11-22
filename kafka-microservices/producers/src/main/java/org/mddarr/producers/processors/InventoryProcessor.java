package org.mddarr.producers.processors;

import org.apache.kafka.common.serialization.Deserializer;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serializer;
import org.mddarr.products.PurchaseCount;
import org.springframework.stereotype.Service;

import java.io.*;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.TreeSet;

@Service
public class InventoryProcessor {

    public static final String PURCHASE_EVENTS = "purchase-events";
    public static final String PRODUCT_FEED = "product-feed";
    public static final String TOP_FIVE_KEY = "all";
    public static final String TOP_FIVE_PRODUCTS_STORE = "top-five-products";
    public static final String ALL_PRODUCTS = "all-products";
    private static final String PRODUCT_PLAY_COUNT_STORE = "product-play-count";
    static final String TOP_FIVE_PRODUCTS_BY_BRAND_STORE = "top-five-products-by-brand";


//    @Bean
//    public BiConsumer<KStream<String, PurchaseEvent>, KTable<String, Product>> process() {
//
//        return (purchaseStream, productTable) -> {
//            // create and configure the SpecificAvroSerdes required in this example
//            final Map<String, String> serdeConfig = Collections.singletonMap(
//                    AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");
//
//            final SpecificAvroSerde<PurchaseEvent> purchaseEventSerde = new SpecificAvroSerde<>();
//            purchaseEventSerde.configure(serdeConfig, false);
//
//            final SpecificAvroSerde<Product> keyProductSerde = new SpecificAvroSerde<>();
//            keyProductSerde.configure(serdeConfig, true);
//
//            final SpecificAvroSerde<Product> valueProductSerde = new SpecificAvroSerde<>();
//            valueProductSerde.configure(serdeConfig, false);
//
//            final SpecificAvroSerde<PurchaseCount> productPurchaseCountSerde = new SpecificAvroSerde<>();
//            productPurchaseCountSerde.configure(serdeConfig, false);
//
//            final KStream<String, PurchaseEvent> purchasesByProductId =
//                    purchaseStream.map((key, value) -> KeyValue.pair(value.getProductId(), value));
//
//            // join the purchases with product as we will use it later for charting
//            final KStream<String, Product> productPurchases = purchasesByProductId
//                    .leftJoin(productTable, (value1, product) -> product,
//                    Joined.with(Serdes.String(), purchaseEventSerde, valueProductSerde));
//
//            // create a state store to track product purchase counts
//            final KTable<Product, Long> productPurchaseCounts = productPurchases.groupBy((productId, product) -> product,
//                    Grouped.with(keyProductSerde, valueProductSerde))
//                    .count(Materialized.<Product, Long, KeyValueStore<Bytes, byte[]>>as(PRODUCT_PLAY_COUNT_STORE)
//                            .withKeySerde(valueProductSerde)
//                            .withValueSerde(Serdes.Long()));
//
//            final TopFiveSerde topFiveSerde = new TopFiveSerde();
//
//            // Compute the top five charts for each brand. The results of this computation will continuously update the state
//            // store "top-five-products-by-genre", and this state store can then be queried interactively via a REST API (cf.
//            // MusicPlaysRestService) for the latest charts per genre.
//            productPurchaseCounts.groupBy((product, purchase_count) ->
//								KeyValue.pair(product.getBrand().toLowerCase(),
//										new PurchaseCount(product.getId(), purchase_count)),
//						Grouped.with(Serdes.String(), productPurchaseCountSerde))
//						// aggregate into a TopFiveSongs instance that will keep track
//						// of the current top five for each genre. The data will be available in the
//						// top-five-songs-genre store
//						.aggregate(TopFiveProducts::new,
//								(aggKey, value, aggregate) -> {
//									aggregate.add(value);
//									return aggregate;
//								},
//								(aggKey, value, aggregate) -> {
//									aggregate.remove(value);
//									return aggregate;
//								},
//								Materialized.<String, TopFiveProducts, KeyValueStore<Bytes, byte[]>>as(TOP_FIVE_PRODUCTS_BY_BRAND_STORE)
//										.withKeySerde(Serdes.String())
//										.withValueSerde(topFiveSerde)
//                        );
////
////				// Compute the top five chart. The results of this computation will continuously update the state
////				// store "top-five-songs", and this state store can then be queried interactively via a REST API (cf.
////				// MusicPlaysRestService) for the latest charts per genre.
//            productPurchaseCounts.groupBy((product, purchase_count) ->
//								KeyValue.pair(TOP_FIVE_KEY,
//										new PurchaseCount(product.getId(), purchase_count)),
//						Grouped.with(Serdes.String(), productPurchaseCountSerde))
//						.aggregate(TopFiveProducts::new,
//								(aggKey, value, aggregate) -> {
//									aggregate.add(value);
//									return aggregate;
//								},
//								(aggKey, value, aggregate) -> {
//									aggregate.remove(value);
//									return aggregate;
//								},
//								Materialized.<String, TopFiveProducts, KeyValueStore<Bytes, byte[]>>as(TOP_FIVE_PRODUCTS_STORE)
//										.withKeySerde(Serdes.String())
//										.withValueSerde(topFiveSerde)
//						);
//        };
//
//    }


    public static class TopFiveProducts implements Iterable<PurchaseCount> {
        private final Map<String, PurchaseCount> currentProducts = new HashMap<>();
        private final TreeSet<PurchaseCount> topFive = new TreeSet<>((o1, o2) -> {
            final int result = o2.getCount().compareTo(o1.getCount());
            if (result != 0) {
                return result;
            }
            return o1.getProductId().compareTo(o2.getProductId());
        });

        public void add(final PurchaseCount productPurchaseCount) {
            if(currentProducts.containsKey(productPurchaseCount.getProductId())) {
                topFive.remove(currentProducts.remove(productPurchaseCount.getProductId()));
            }
            topFive.add(productPurchaseCount);
            currentProducts.put(productPurchaseCount.getProductId(), productPurchaseCount);
            if (topFive.size() > 5) {
                final PurchaseCount last = topFive.last();
                currentProducts.remove(last.getProductId());
                topFive.remove(last);
            }
        }

        void remove(final PurchaseCount value) {
            topFive.remove(value);
            currentProducts.remove(value.getProductId());
        }

        @Override
        public Iterator<PurchaseCount> iterator() {
            return topFive.iterator();
        }

    }

    private static class TopFiveSerde implements Serde<TopFiveProducts> {

        @Override
        public Serializer<TopFiveProducts> serializer() {

            return new Serializer<TopFiveProducts>() {
                @Override
                public void configure(final Map<String, ?> map, final boolean b) {
                }
                @Override
                public byte[] serialize(final String s, final TopFiveProducts topFiveProducts) {

                    final ByteArrayOutputStream out = new ByteArrayOutputStream();
                    final DataOutputStream
                            dataOutputStream =
                            new DataOutputStream(out);
                    try {
                        for (PurchaseCount purchaseCount : topFiveProducts) {
                            dataOutputStream.writeUTF(purchaseCount.getProductId());
                            dataOutputStream.writeLong(purchaseCount.getCount());
                        }
                        dataOutputStream.flush();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                    return out.toByteArray();
                }
            };
        }

        @Override
        public Deserializer<TopFiveProducts> deserializer() {

            return (s, bytes) -> {
                if (bytes == null || bytes.length == 0) {
                    return null;
                }
                final TopFiveProducts result = new TopFiveProducts();

                final DataInputStream
                        dataInputStream =
                        new DataInputStream(new ByteArrayInputStream(bytes));

                try {
                    while(dataInputStream.available() > 0) {
                        result.add(new PurchaseCount(dataInputStream.readUTF(),
                                dataInputStream.readLong()));
                    }
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                return result;
            };
        }
    }


}
