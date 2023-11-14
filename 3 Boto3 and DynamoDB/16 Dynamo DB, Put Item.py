import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
table.put_item(
    Item={
        'emp_id': '2',
        'name': 'musk',
        'salary': 20000
    }
)