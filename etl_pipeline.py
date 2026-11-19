import pandas as pd
import requests
import sqlite3
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def extract_data():
    logging.info("Starting data extraction")

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data)

    df = df[["id", "name", "username", "email", "phone", "website"]]

    return df


def transform_data(df):
    logging.info("Starting data transformation")

    df = df.drop_duplicates()
    return df


def load_data(df):
    logging.info("Starting data loading")

    conn = sqlite3.connect("customers.db")

    try:
        df.to_sql("customers", conn, if_exists="replace", index=False)
        conn.commit()
        logging.info("Data loaded successfully")

    except sqlite3.Error:
        conn.rollback()
        logging.exception("Database loading failed")
        raise

    finally:
        conn.close()


def main():
    try:
        df = extract_data()
        df = transform_data(df)
        load_data(df)

        print("ETL pipeline completed successfully!")

    except Exception:
        logging.exception("Pipeline failed")
        print("ETL pipeline failed. Check pipeline.log")


if __name__ == "__main__":
    main()
