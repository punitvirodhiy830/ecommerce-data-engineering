from extract import create_spark_session, extract_data
from transform import transform_data
from validate import validate_data
from load import load_data


INPUT_FILE = "data/orders.csv"


def run_pipeline():
    """Run the complete e-commerce data engineering pipeline."""

    spark = create_spark_session()

    try:
        print("Starting ETL pipeline...")

        # 1. Extract
        print("Step 1: Extracting data...")
        raw_data = extract_data(spark, INPUT_FILE)
        print(f"Raw rows: {raw_data.count()}")

        # 2. Transform
        print("Step 2: Transforming data...")
        transformed_data = transform_data(raw_data)
        print(f"Transformed rows: {transformed_data.count()}")

        # 3. Validate
        print("Step 3: Validating data...")
        validate_data(transformed_data)

        # 4. Load
        print("Step 4: Loading data...")
        load_data(transformed_data)

        print("ETL pipeline completed successfully.")

    except Exception as error:
        print(f"ETL pipeline failed: {error}")
        raise

    finally:
        spark.stop()


if __name__ == "__main__":
    run_pipeline()