### Hive ###

Load data into hive
docker exec -it hive_hive-server_1 bash
/opt/hive/bin/beeline -u jdbc:hive2://localhost:10000

CREATE TABLE transactions (id INT, amount DOUBLE, date1 STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';';

LOAD DATA LOCAL INPATH '/opt/hive/examples/files/transactions.txt' OVERWRITE INTO TABLE transactions;

docker cp parsed_transactions.txt twitter_hive-server_1:/opt/hive/examples/files/transactions.txt

CREATE TABLE transcations1 (id INT, bar STRING, created_date TIMESTAMP)
ROW FORMAT SERDE 'org.apache.hadoop.hive.contrib.serde2.MultiDelimitSerDe'

LOAD DATA LOCAL INPATH '/opt/hive/examples/files/kv1.txt' OVERWRITE INTO TABLE pokes;


I have a file of transactions as follows.

815581247;$144.82;2015-09-05
1534673027;$140.93;2014-03-11
842468364;$104.26;2014-05-06
1720001139;$194.60;2015-08-24

To remove the $, I can use sed, making sure to use the '\' character to escape the $ 
sed 's/\$//g'