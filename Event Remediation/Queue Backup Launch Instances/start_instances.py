import boto3
from botocore.exceptions import ClientError

def build_client():
    ec2 = boto3.client(
    'ec2',
    region_name = 'us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)
    return ec2

def create_another_instance():
    ec2 = build_client()
    response = ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)
    return response


print(create_another_instane)
