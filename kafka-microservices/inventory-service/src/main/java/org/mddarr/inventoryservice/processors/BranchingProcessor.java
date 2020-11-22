package org.mddarr.inventoryservice.processors;

import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.Materialized;
import org.apache.kafka.streams.kstream.Predicate;
import org.apache.kafka.streams.kstream.TimeWindows;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.cloud.stream.annotation.EnableBinding;
import org.springframework.cloud.stream.annotation.Input;
import org.springframework.cloud.stream.annotation.Output;
import org.springframework.cloud.stream.annotation.StreamListener;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.Arrays;
import java.util.Date;
@Service
public class BranchingProcessor {
//    @EnableBinding({WordBranches.class})
//    @EnableAutoConfiguration
    public static class WordCountProcessorApplication {
        @StreamListener("words")
        @SendTo({"english", "french", "spanish"})
        @SuppressWarnings("unchecked")
        public KStream<?, WordCount>[]process(KStream < Object, String>input) {

            Predicate<Object, WordCount> isEnglish = (k, v) -> v.word.equals("english");
            Predicate<Object, WordCount> isFrench = (k, v) -> v.word.equals("french");
            Predicate<Object, WordCount> isSpanish = (k, v) -> v.word.equals("spanish");

            return input
                    .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))
                    .groupBy((key, value) -> value)
                    .windowedBy(TimeWindows.of(Duration.ofSeconds(6)))
                    .count(Materialized.as("WordCounts-1"))
                    .toStream()
                    .map((key, value) -> new KeyValue<>(null, new WordCount(key.key(), value, new Date(key.window().start()), new Date(key.window().end()))))
                    .branch(isEnglish, isFrench, isSpanish);
        }
    }

//    interface WordBranches {
//        @Input("words")
//        KStream<?, ?> input();
//        @Output("english")
//        KStream<?, ?> output1();
//        @Output("french")
//        KStream<?, ?> output2();
//        @Output("spanish")
//        KStream<?, ?> output3();
//    }




    static class WordCount {
        private String word;
        private long count;
        private Date start;
        private Date end;
        WordCount(String word, long count, Date start, Date end) {
            this.word = word;
            this.count = count;
            this.start = start;
            this.end = end;
        }
        public String getWord() {
            return word;
        }
        public void setWord(String word) {
            this.word = word;
        }
        public long getCount() {
            return count;
        }
        public void setCount(long count) {
            this.count = count;
        }
        public Date getStart() {
            return start;
        }
        public void setStart(Date start) {
            this.start = start;
        }
        public Date getEnd() {
            return end;
        }
        public void setEnd(Date end) {
            this.end = end;
        }
    }

}
