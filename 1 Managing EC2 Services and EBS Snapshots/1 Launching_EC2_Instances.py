import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    resp = client.run_instances(ImageId='ami-053b0d53c279acc90',
                    InstanceType='t2.micro',
                    MaxCount=1,
                    MinCount=1,
                    Monitoring={
                        'Enabled':True
                    },
                    )
    for instance in resp['Instances']:
        print(instance['InstanceId'])