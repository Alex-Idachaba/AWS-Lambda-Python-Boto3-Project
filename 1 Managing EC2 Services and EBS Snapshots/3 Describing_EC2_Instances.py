import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    resp = client.describe_instances()
    
    for reservation in resp['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instanceid is {instance['InstanceId']}")