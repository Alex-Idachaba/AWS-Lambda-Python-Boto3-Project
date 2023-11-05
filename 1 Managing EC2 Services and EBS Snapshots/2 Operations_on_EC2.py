import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    resp = client.terminate_instances(InstanceIds=[
        'i-037ef165ff2b1a82d'
        ])
        
    for instance in resp['TerminatingInstances']:
        print(f"Instance with id {instance['InstanceId']} terminated")