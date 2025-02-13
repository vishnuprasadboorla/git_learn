from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("SimplePySparkJob") \
    .config("spark.jars", "/path/to/postgresql-42.2.27.jar") \  # Update with correct path
    .getOrCreate()

# PostgreSQL Connection Properties
postgres_url = "jdbc:postgresql://localhost:5432/postgres"  # Using local PostgreSQL
table_name = "filtered_users"  # Your target table name
properties = {
    "user": "postgres",  # Replace with your PostgreSQL username
    "password": "Dream",  # Replace with your PostgreSQL password
    "driver": "org.postgresql.Driver"
}

# Create a DataFrame
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Perform a Transformation (Filter Age > 28)
df_filtered = df.filter(col("Age") > 28)

# Write DataFrame to PostgreSQL Table
df_filtered.write \
    .jdbc(url=postgres_url, table=table_name, mode="overwrite", properties=properties)

# Stop Spark Session
spark.stop()
