import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
        
    ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]).stop()
    
    
    
    # instances = ec2.instances.filter(Filters=[
    #     {
    #         'Name': 'availability-zone',
    #         'Values': ['us-east-1c']
    #     }
    # ])
    # for instance in instances:
    #     print(f"Instance id is {instance.instance_id} and instance type is {instance.instance_type}")