import os

from pyspark.sql import DataFrame


def load_data(df: DataFrame) -> None:
    """Load transformed data into PostgreSQL."""

    postgres_url = os.getenv(
        "POSTGRES_URL",
        "jdbc:postgresql://localhost:5432/ecommerce"
    )

    postgres_properties = {
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "driver": "org.postgresql.Driver"
    }

    (
        df.write
        .mode("append")
        .jdbc(
            url=postgres_url,
            table="orders",
            properties=postgres_properties
        )
    )

    print("Data successfully loaded into PostgreSQL.")
    print(f"Rows loaded: {df.count()}")