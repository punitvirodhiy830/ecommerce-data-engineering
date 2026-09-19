import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform raw order data."""

    df = df.copy()

    # Standardize text columns
    df["customer_name"] = df["customer_name"].str.strip()
    df["country"] = df["country"].str.strip()
    df["product_name"] = df["product_name"].str.strip()
    df["category"] = df["category"].str.strip()
    df["status"] = df["status"].str.strip()

    # Convert data types
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # Remove invalid records
    df = df.dropna(
        subset=[
            "order_id",
            "customer_id",
            "product_id",
            "order_date",
            "quantity",
            "unit_price",
        ]
    )

    # Keep valid quantities and prices
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]

    # Create calculated column
    df["total_amount"] = df["quantity"] * df["unit_price"]

    # Remove duplicate order-product records
    df = df.drop_duplicates(
        subset=["order_id", "product_id"]
    )

    return df


if __name__ == "__main__":
    raw_data = pd.read_csv("data/orders.csv")
    transformed_data = transform_data(raw_data)

    print("Rows after transformation:", len(transformed_data))
    print(transformed_data.head())