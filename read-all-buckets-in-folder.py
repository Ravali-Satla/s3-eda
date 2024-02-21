import os
import boto3
AWS_DEFAULT_REGION="ap-south-1"
os.environ["AWS_ACCESS_KEY_ID"] = 'aws_access_key_id1'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'aws_secret_access_key'
s3Client=boto3.client("s3",region_name=AWS_DEFAULT_REGION)

allBuckets = s3Client.list_buckets()

for bucket in allBuckets['Buckets']:
    print(f' {bucket["Name"]}')