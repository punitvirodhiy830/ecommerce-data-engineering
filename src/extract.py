import pandas as pd


def extract_data(file_path: str) -> pd.DataFrame:
    """Read raw order data from CSV."""
    return pd.read_csv(file_path)


if __name__ == "__main__":
    data = extract_data("data/orders.csv")
    print("Rows extracted:", len(data))
    print(data.head())