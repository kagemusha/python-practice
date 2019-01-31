from pyspark.sql import SparkSession


spark = SparkSession.builder \
  .master('local') \
  .appName("misc") \
  .getOrCreate()
data = [('mm', 50),('riri',32), ('jl',8), ('il',8)]
df = spark.createDataFrame(data, ['name','age'])
df.collect()