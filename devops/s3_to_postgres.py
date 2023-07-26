import pandas as pd
from sqlalchemy import create_engine

from aws_configure import *
from config import *


def get_s3_csv_data():
    obj = s3_client.get_object(Bucket=S3_BUCKET, Key=CSV_FILE)
    return pd.read_csv(obj['Body'])


def push_data_to_postgres(dataframe, table_name):
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    dataframe.to_sql(table_name, engine, if_exists='replace', index=False)


def s3_to_postgres():
    print("Pulling data from S3")
    df = get_s3_csv_data()
    print("Pushing data to Postgres")
    print(df.head())
    push_data_to_postgres(df, "data")
    print("Data pushed successfully.!!")


if __name__ == "__main__":
    s3_to_postgres()
