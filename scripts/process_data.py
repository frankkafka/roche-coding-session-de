import argparse
from pathlib import Path
import sqlite3
import pandas as pd

def merge_and_store(users_csv: str, orders_csv: str, output_db: str) -> None:
    """Reads two CSVs, merges on user_id, and writes to SQLite."""
    
    # Read CSV files
    users = pd.read_csv(users_csv)
    orders = pd.read_csv(orders_csv)

    # Inner join on user_id
    merged = pd.merge(users, orders, on="user_id", how="inner")

    # Ensure output directory exists
    Path(output_db).parent.mkdir(parents=True, exist_ok=True)

    # Write to SQLite database
    with sqlite3.connect(output_db) as conn:
        merged.to_sql("user_orders", conn, if_exists="replace", index=False)

    print(f"Successfully merged {len(merged)} records and wrote to {output_db}")

def main():
    parser = argparse.ArgumentParser(description="Merge CSVs and load into SQLite database.")
    parser.add_argument("--users_csv", required=True, help="Path to users.csv")
    parser.add_argument("--orders_csv", required=True, help="Path to orders.csv")
    parser.add_argument("--output_db", required=True, help="Path to output SQLite DB (e.g., data/processed/analytics.sqlite)")
    args = parser.parse_args()

    merge_and_store(args.users_csv, args.orders_csv, args.output_db)

if __name__ == "__main__":
    main()
