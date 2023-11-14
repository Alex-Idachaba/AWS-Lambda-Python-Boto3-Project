import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    sns_arn = 'arn:aws:sns:us-east-1:058771366375:Prod-Alerts'
    message = 'Prod server stopped, please look into it.'
    client.publish(TopicArn=sns_arn, Message=message)