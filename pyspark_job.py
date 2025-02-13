from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("SimplePySparkJob").getOrCreate()

# Create a DataFrame
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Perform a Transformation (Filter Age > 28)
df_filtered = df.filter(col("Age") > 28)

# Show Results
df_filtered.show()

# Stop Spark Session
spark.stop()
