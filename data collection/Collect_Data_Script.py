# Download files from an Amazon S3 bucket, decompress compressed files (.gz), and save them to a local folder

import gzip
import json
import os
import subprocess
import sys

def create_local_folder(local_folder):
    # Create the local folder if it doesn't exist
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

def list_objects(bucket_name, s3_folder_key):
    # Retrieve the list of objects in the S3 folder
    list_objects_command = [
        "aws", "s3api", "list-objects", "--bucket", bucket_name,
        "--prefix", s3_folder_key, "--output", "json", "--no-sign-request"
    ]
    objects_output = subprocess.check_output(list_objects_command, universal_newlines=True)
    objects = json.loads(objects_output)["Contents"]
    return objects

def download_file(bucket_name, s3_key, local_file_path):
    # Download a file from S3
    download_command = [
        "aws", "s3", "cp", "s3://{}/{}".format(bucket_name, s3_key),
        local_file_path, "--no-sign-request"
    ]
    subprocess.check_call(download_command)

def decompress_file(file):
    # Decompress a .gz file
    with gzip.open(file, 'rb') as f_in:
        output_file = os.path.splitext(file)[0]
        with open(output_file, 'wb') as f_out:
            f_out.write(f_in.read())

def main():
    bucket_name = "genome-browser"
    s3_folder_key = "goldenPath/hs1/bigZips/genes"

    if len(sys.argv) >= 2:
        local_folder = sys.argv[1]
    else:
        local_folder = "C:/genome/"

    create_local_folder(local_folder)

    objects = list_objects(bucket_name, s3_folder_key)

    for obj in objects:
        s3_key = obj["Key"]
        local_file_path = os.path.join(local_folder, s3_key)
        print(local_file_path)
        try:
            download_file(bucket_name, s3_key, local_file_path)
            print("File downloaded successfully: {}".format(local_file_path))
        except subprocess.CalledProcessError:
            print("Error downloading file: {}".format(s3_key))

    gz_files = [
        os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(local_folder)
        for filename in filenames
        if filename.endswith(".gz")
    ]
    print(gz_files)

    for file in gz_files:
        print(file)
        decompress_file(file)
        print("File decompressed: {}".format(os.path.basename(file)))

if __name__ == "__main__":
    main()
