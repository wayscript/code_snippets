import boto3
from botocore.exceptions import ClientError
import pandas as pd
from datetime import datetime


def build_client():
    ec2 = boto3.client(
    'ec2',
    region_name = 'us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
    )
    return ec2

def ec2_info( ):
    ec2 = build_client()
    response = ec2.describe_instances()
    instances_info = []
    for reservation in response['Reservations']:
            for instance_description in reservation['Instances']:
                image_id = instance_description['ImageId']
                instance_id = instance_description['InstanceId']
                volume_id = instance_description['BlockDeviceMappings'][0]['Ebs']['VolumeId']
                status = instance_description['State'].get('Name')
                a = [ image_id, instance_id, volume_id, status ]
                instances_info.append( a )
    return instances_info

# Create the snapshot on S3
def ec2_running_instances_backup():
    response = ec2_info()
    unique_volumes = []
    for instance in response:
        if instance[3] = 'running' and instance[2] not in unique_volumes :
            ec2 = build_client()
            ec2.create_snapshot(instance[2])
            unique_volumes.append(instance[2])
            print('Snapshot created for volume:' instance[2])
    return unique_volumes

# Reboot instances
def reboot_running_ec2():
    instances = ec2_info()
    ec2 = build_client()
    for instance in instances:
        if instance[3] = 'running':
            response = ec2.reboot_instances(
    InstanceIds=[instance[1]],
    )


print(ec2_info())
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)
