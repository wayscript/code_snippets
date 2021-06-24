import boto3
#AWS keys

def build_client():
    lambda_client = boto3.client(
    'lambda',
    region_name = 'us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
    )
    return lambda_client

lambda_client = build_client()
response = lambda_client.invoke(
    FunctionName='HelloWorldTemplate',
    InvocationType='RequestResponse',
    LogType='Tail',
)

print(response)
