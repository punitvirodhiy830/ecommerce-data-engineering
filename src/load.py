import sqlite3
import pandas as pd

from extract import extract_data
from transform import transform_data


DATABASE_NAME = "ecommerce.db"
INPUT_FILE = "data/orders.csv"


def load_data(df: pd.DataFrame) -> None:
    """Load transformed data into SQLite database."""

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        # Main transformed orders table
        df.to_sql(
            "sales",
            connection,
            if_exists="replace",
            index=False
        )

        print("Data successfully loaded into SQLite.")
        print(f"Rows loaded: {len(df)}")

    finally:
        connection.close()


if __name__ == "__main__":
    raw_data = extract_data(INPUT_FILE)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)