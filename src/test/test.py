from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder \
    .appName("CreateEmptyTable") \
    .config("spark.jars", "C:\\my_sql_jar\\mysql-connector-java-8.0.26.jar") \
    .getOrCreate()

# Create an empty DataFrame with schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

empty_df = spark.createDataFrame([], schema)

# JDBC config
url = "jdbc:mysql://localhost:3306/de_project"
properties = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Write to MySQL
empty_df.write.jdbc(url=url, table="test_table", mode="overwrite", properties=properties)