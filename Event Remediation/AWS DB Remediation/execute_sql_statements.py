# Function 1 of the DB remediation video
# Using boto3 clients to perform actions against your db so you can automatically correct potential problems

import boto3
from botocore.exceptions import ClientError

def build_client():
    ec2 = boto3.client(
    'rds',
    region_name = 'us-east-2',
    aws_access_key_id=󰀂v.9-key_id󰀂,
    aws_secret_access_key=󰀂v.12-key_secret󰀂
)
    return rds

rds = build_client()
response = rds.execute_statement(
    continueAfterTimeout=False,
    database='database-1',
    includeResultMetadata=False,
    resourceArn='aws:rds:us-east-2:725294532515:db:database-1',
    schema='string',
    secretArn='string',
    sql='string',
    transactionId='string'
)
