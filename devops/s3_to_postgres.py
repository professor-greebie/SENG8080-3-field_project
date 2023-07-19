# import data from s3 bucket to PostgresSQL

import boto3
import psycopg2
from psycopg2 import sql

s3_bucket = 'your-s3-bucket'
s3_file = 'path/to/your/file.csv'
db_host = 'your-db-host'
db_port = 5432  # Replace with your PostgresSQL port number
db_name = 'your-db-name'
db_user = 'your-db-user'
db_password = 'your-db-password'


def push_csv_to_postgresql(s3_bucket, s3_file, db_host, db_port, db_name, db_user, db_password):
    """
    Pushes CSV data from AWS S3 to a PostgreSQL database.
    Args:
        s3_bucket (str): Name of the S3 bucket.
        s3_file (str): Path to the CSV file in S3.
        db_host (str): Hostname of the PostgresSQL database.
        db_port (int): Port number of the PostgresSQL database.
        db_name (str): Name of the PostgresSQL database.
        db_user (str): Username to connect to the PostgresSQL database.
        db_password (str): Password to connect to the PostgresSQL database.
    """
    # Download the CSV file from S3
    s3 = boto3.client('s3')
    s3.download_file(s3_bucket, s3_file, 'temp.csv')

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Create the table in the database
    table_name = 'csv_data'
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} (
            column1 data_type1,
            column2 data_type2,
            -- Add more columns as necessary
        );
    """).format(table=sql.Identifier(table_name))

    cursor.execute(create_table_query)

    # Load data from the CSV file into the table
    copy_query = sql.SQL("""
        COPY {table}
        FROM STDIN
        WITH (FORMAT CSV, HEADER TRUE);
    """).format(table=sql.Identifier(table_name))

    with open('temp.csv', 'r') as f:
        cursor.copy_expert(copy_query, f)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print(f"CSV data loaded into the '{table_name}' table successfully!")


push_csv_to_postgresql(s3_bucket, s3_file, db_host, db_port, db_name, db_user, db_password)
