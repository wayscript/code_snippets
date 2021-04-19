import boto3

# build boto3 session
def build_session():
    session = boto3.Session(
        region_name='us-east-2',
        aws_access_key_id='',
        aws_secret_access_key='',
    )

    ec2 = session.resource('ec2')
    return ec2

# Get Instance info
def view_running_instances( ec2 ):
    instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    running_instances = []
    for instance in instances:
        i = {}
        i['id'] = instance.id
        i['type'] = instance.instance_type
        i['state'] = instance.state
        print(instance.id, instance.instance_type, instance.state)
        running_instances.append(i)
    variables['instances'] = running_instances

#  Start a stopped instance
def control_instance( ec2, instance_id, action ):
    if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

    else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

#Reboot an instance
def reboot_instances( ec2, instance_id ):
    try:
    ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print("You don't have permission to reboot instances.")
            raise

    try:
        response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
        print('Success', response)
    except ClientError as e:
        print('Error', e)

ec2 = build_session()
#view_running_instances( ec2 )
#instance_id = variables['Alert'].get('instance_id')
#change = variables['Alert'].get('change')
#control_instance( ec2, instance_id, change )
#reboot_instances( ec2, instance_id )
