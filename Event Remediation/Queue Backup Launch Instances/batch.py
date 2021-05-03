# Getting current Batch Jobs

import boto3
from botocore.exceptions import ClientError

def build_batch_client():
    batch = boto3.client(
    'batch',
    region_name = 'us-east-2',
    aws_access_key_id = '',
    aws_secret_access_key = ''
    )
    return batch

def build_batch_client():
    batch = boto3.client(
    'batch',
    region_name = 'us-east-2',
    aws_access_key_id = '',
    aws_secret_access_key = ''
    )
    return batch

def describe_queues():
    batch = build_batch_client()
    response = batch.describe_job_queues(
    jobQueues = [
    'string',
    ],
    nextToken = 'string'
    )
    return response

def get_pending_jobs():
    batch = build_batch_client()
    response = batch.list_jobs(
    jobQueue='string',
    jobStatus='PENDING',
    )
    return response

response = get_pending_jobs()
print(response)
variables['pending_jobs'] = response.get('ResponseMetadata').get('jobSummaryList')
try:
    variables['jobs_count'] = len(variables['pending_jobs'])
except:
    variables['jobs_count'] = 0
