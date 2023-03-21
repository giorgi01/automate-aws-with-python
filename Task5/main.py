import argparse
import boto3
from os import getenv
from botocore.exceptions import ClientError

def create_bucket(bucket_name):
    client = boto3.client('s3',
                     aws_access_key_id=getenv("aws_access_key_id"),
                      aws_secret_access_key=getenv("aws_secret_access_key"),
                      aws_session_token=getenv("aws_session_token"),
                      region_name=getenv("region_name")
                     )
    try:
        client.head_bucket(Bucket=bucket_name)
        print(f"Bucket with name {bucket_name} already exists.")
    except ClientError:
        client.create_bucket(Bucket=bucket_name)
        print(f"Bucket with name {bucket_name} has been created.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('bucket_name', type=str)
    args = parser.parse_args()

    create_bucket(args.bucket_name)
