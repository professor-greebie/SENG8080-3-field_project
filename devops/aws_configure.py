import boto3
from config import *

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

s3_client = session.client('s3')
