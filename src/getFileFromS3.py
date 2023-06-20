import boto3

# This function downloads a file from an Amazon S3 bucket using the boto3 library.
# TODO - Have to replace the bucket name, object key and file path
def download_file_from_s3(bucket_name, object_key, file_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, object_key, file_path)
        print(f"File downloaded: {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")

download_file_from_s3(bucket_name, object_key, file_path)