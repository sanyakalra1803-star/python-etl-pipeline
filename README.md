
# Python ETL Pipeline

## Project Overview
A simple end-to-end ETL pipeline built using Python, Pandas, Requests, and SQLite.

The pipeline extracts user data from a public REST API, performs basic data cleaning, and loads the cleaned records into a SQLite database.

## ETL Process

1. **Extract:** Fetch user data from JSONPlaceholder API.
2. **Transform:** Convert JSON data into a Pandas DataFrame and remove duplicate records.
3. **Load:** Store the cleaned data in a SQLite database.

## Technologies Used
- Python
- Pandas
- Requests
- SQLite
- Logging

## Project Structure

```text
python-etl-pipeline/
├── etl_pipeline.py
├── requirements.txt
├── README.md
├── .gitignore
```

## How to Run

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Run the pipeline:

   `python etl_pipeline.py`

## Data Source
JSONPlaceholder public API:
https://jsonplaceholder.typicode.com/users
