import boto3
from botocore.exceptions import ClientError
import pandas as pd
from datetime import datetime

def build_client():
    ec2 = boto3.client(
    'ec2',
    region_name = 'us-east-2',
    aws_access_key_id=󰀂v.2-key_id󰀂,
    aws_secret_access_key=󰀂v.3-secret_key_id󰀂
    )
    return ec2

#print(build_client())

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

#print(ec2_info())

# create snapshots
def ec2_running_instances_backup():
    response = ec2_info()
    unique_volumes = []
    for instance in response:
        if instance[3] == 'running' and instance[2] not in unique_volumes :
            ec2 = build_client()
            instance = str(instance[2])
            ec2.create_snapshot(VolumeId=instance)
            unique_volumes.append(instance[2])
            print('Snapshot created for volume: ' + str(instance[2]))
    return unique_volumes

def reboot_running_ec2():
    instances = ec2_info()
    ec2 = build_client()
    for instance in instances:
        if instance[3] == 'running':
            response = ec2.reboot_instances(
    InstanceIds=[instance[1]],
    )

print(ec2_running_instances_backup())
print(reboot_running_ec2())
