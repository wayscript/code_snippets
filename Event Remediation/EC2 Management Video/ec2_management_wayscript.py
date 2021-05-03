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

def ec2_info( ):
    ec2 = build_client()
    response = ec2.describe_instances()
    return response

def check_instance_state( instance_id ):
    ec2 = build_client()
    response = ec2.describe_instance_status(
    InstanceIds = [ instance_id ] )
    try:
        instance_status = response.get( 'InstanceStatuses' )[0].get('InstanceState').get('Name')
        response = instance_status
    except:
        response = 'not running'
    return response

def turn_instance_on( instance_id ):
    ec2 = build_client()
    current_state = check_instance_state( instance_id )
    if current_state == 'not running':
        try:
            response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
            new_state = response.get('StartInstances')[0].get('CurrentState').get('Name')
            return 'Success'
        except ClientError as response:
            return response
    else:
        return 'Instace Already Running'


def turn_instance_off( instance_id ):
    ec2 = build_client()
    current_state = check_instance_state( instance_id )
    if current_state == 'running':
        try:
            response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
            old_state = response.get('StoppingInstances')[0].get('PreviousState').get('Name')
            new_state = response.get('StoppingInstances')[0].get('CurrentState').get('Name')
        except ClientError as e:
            print(e)
    else:
        return 'Instance Already Off'

def reboot_an_instance( instance_id ):
    ec2 = build_client()
    current_state = check_instance_state( instance_id )
    if current_state == 'running':
        try:
            response = ec2.reboot_instances(InstanceIds=[ instance_id ], DryRun=False)
            return 'Success'
        except ClientError as e:
            print('Error', e)
    else:
        return 'Cannot Reboot - Instance Not Running'

#print(ec2_info( ) )
micro_instance = 'i-095eaf403ed90d73f'
print(reboot_an_instance( micro_instance ))
