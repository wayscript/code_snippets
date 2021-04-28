# EC2 Instance Event Remediation

## Setup
### Datadog
This section covers:
* Connecting your WayScript account to datadog
* Creating a Webhook to execute your wayscript program through datadog monitors

**Connecting your Datadog account to WayScript**
To begin, you'll need to connect your datadog account to WayScript.
In case you need it, a [Video Tutorial](https://youtu.be/EUtfLi5LqWA) is available.

You will need:
* Application Key - Gives access to interacting with the datadog account.
* API Key - Unique to your organization.

Both of those keys can be found under your [datadog account](https://app.datadoghq.com/account/settings#api)

Additional help with connecting your datadog account can be found in the [WayScript docs](https://docs.wayscript.com/library/modules/datadog)

**Creating the Datadog Monitor**
Create a monitor as usual by choosing the event type to watch and the tolerances of the event.
More information can be found [here.](https://docs.datadoghq.com/monitors/monitor_types/)

A Notification string needs to be included to trigger your wayscript programs *@webhook-wayscript-datadog-trigger*

This send the notification event to wayscript, which will then cause the execution of your wayscript programs including the datadog trigger.

### Boto3
This section covers:
* Getting your boto3 access credentials

**IAM User Management**
In this example, we're only working with EC2 instances. Therefore, we can create a user with only the permissions to access our EC2 instanes.
Creating users and setting permissions is a task we can do under the [IAM User Management](https://aws.amazon.com/iam/#:~:text=AWS%20Identity%20and%20Access%20Management%20(IAM)%20enables%20you%20to%20manage,offered%20at%20no%20additional%20charge.)

After creating this user, we have access to two keys, these keys can be passed to the boto3 API to access our EC2 resources.

## Connecting to EC2 via Boto3

**Creating a Boto3 Client**
In our code, we can create a boto3 client accessing aws EC2 resources by using a function and then calling that function in our code.
The objet returned will be the client we can reference, here it is called *ec2*

<cpre>
def build_client():
    ec2 = boto3.client(
    'ec2',
    region_name = 'us-east-2',
    aws_access_key_id='<yourAccessKey>',
    aws_secret_access_key='<yourSecretKey>'
)
    return ec2
</pre>    

**WayScript supports storing secrets in your projects**
With the .env and .secrets files inside your file manager, you can create variables which hide your keys from the editor.

**Accessing EC2 resources**
Once our session is created, we can access any method of the boto3 EC2 client.

To turn an instance on, we may have some code that looks like this:
<pre>
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
        </pre>
