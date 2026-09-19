from pyspark.sql import SparkSession, DataFrame


def create_spark_session() -> SparkSession:
    """Create and return a Spark session."""
    return (
        SparkSession.builder
        .appName("EcommerceDataPipeline")
        .getOrCreate()
    )


def extract_data(spark: SparkSession, file_path: str) -> DataFrame:
    """Extract raw order data from CSV using PySpark."""
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
    )


if __name__ == "__main__":
    spark = create_spark_session()

    data = extract_data(
        spark,
        "data/orders.csv"
    )

    print("Rows extracted:", data.count())
    data.show(5, truncate=False)

    spark.stop()from pyspark.sql import SparkSession, DataFrame


def create_spark_session() -> SparkSession:
    """Create and return a Spark session."""
    return (
        SparkSession.builder
        .appName("EcommerceDataPipeline")
        .getOrCreate()
    )


def extract_data(spark: SparkSession, file_path: str) -> DataFrame:
    """Extract raw order data from CSV using PySpark."""
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
    )


if __name__ == "__main__":
    spark = create_spark_session()

    data = extract_data(
        spark,
        "data/orders.csv"
    )

    print("Rows extracted:", data.count())
    data.show(5, truncate=False)

    spark.stop()