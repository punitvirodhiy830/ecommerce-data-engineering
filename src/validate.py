from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def validate_data(df: DataFrame) -> bool:
    """Run data quality checks on transformed data."""

    # Check 1: DataFrame should not be empty
    if df.count() == 0:
        raise ValueError("Data validation failed: dataset is empty.")

    # Check 2: Required columns must exist
    required_columns = [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "unit_price",
        "total_amount"
    ]

    missing_columns = [
        column_name
        for column_name in required_columns
        if column_name not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Data validation failed: missing columns {missing_columns}"
        )

    # Check 3: Quantity must be positive
    invalid_quantity = df.filter(
        col("quantity") <= 0
    ).count()

    if invalid_quantity > 0:
        raise ValueError(
            f"Data validation failed: {invalid_quantity} "
            "invalid quantity records found."
        )

    # Check 4: Unit price cannot be negative
    invalid_price = df.filter(
        col("unit_price") < 0
    ).count()

    if invalid_price > 0:
        raise ValueError(
            f"Data validation failed: {invalid_price} "
            "negative price records found."
        )

    # Check 5: Total amount must be valid
    invalid_total = df.filter(
        col("total_amount") < 0
    ).count()

    if invalid_total > 0:
        raise ValueError(
            f"Data validation failed: {invalid_total} "
            "invalid total amount records found."
        )

    print("All data quality checks passed.")
    return True