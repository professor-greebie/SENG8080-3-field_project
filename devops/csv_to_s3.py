from aws_configure import *


def push_csv_to_s3():
    s3_client.upload_file(CSV_FILE, S3_BUCKET, CSV_FILE)
    print(f"File '{CSV_FILE}' uploaded to '{S3_BUCKET}' successfully!")


if __name__ == "__main__":
    push_csv_to_s3()
