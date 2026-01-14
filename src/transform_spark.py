from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from config import PROCESSED_DATA_PATH

def transform(df_pandas):
    spark = SparkSession.builder.appName("ETL").getOrCreate()
    df = spark.createDataFrame(df_pandas)
    df_clean = df.dropna().withColumn("total_price", col("quantity") * col("unit_price"))
    df_clean.write.mode("overwrite").parquet(PROCESSED_DATA_PATH)
    spark.stop()
    return df_clean
