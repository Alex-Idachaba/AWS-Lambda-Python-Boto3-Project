import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    sms_client =  boto3.client('sms')
    
    backup_filter = [
        {
            'Name': 'tag:Backup',
            'Values': ['Yes']
        }]
        
    snapshot_ids = []    
    # looping through list(ec2.instances)    
        
    for instance in ec2.instances.filter(Filters=backup_filter):
        for vol in instance.volumes.all():
            snapshot = vol.create_snapshot(Description='Created by Boto3') 
            snapshot_ids.append(snapshot.snapshot_id)
            
    print(snapshot_ids)