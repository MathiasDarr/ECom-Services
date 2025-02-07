import findspark
findspark.init()
import pyspark as ps
import os
from pyspark.conf import SparkConf

def getSparkInstance():
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location
    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()

    # .config("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf()) \
        # .enableHiveSupport() \
    return spark

