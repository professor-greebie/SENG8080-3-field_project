import boto3

def push_csv_to_s3(bucket_name, file_path, object_name):
    """
    Pushes a CSV file to an AWS S3 bucket.
    Args:
        bucket_name (str): Name of the S3 bucket.
        file_path (str): Path to the CSV file on the local system.
        object_name (str): Object name to be used for the file in S3.
    """
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # Upload the file to S3
    s3.upload_file(file_path, bucket_name, object_name)
    
    print(f"File '{object_name}' uploaded to '{bucket_name}' successfully!")

# Example usage
bucket_name = 'your-bucket-name'
file_path = '/path/to/your/file.csv'
object_name = 'your-object-name.csv'

push_csv_to_s3(bucket_name, file_path, object_name)


