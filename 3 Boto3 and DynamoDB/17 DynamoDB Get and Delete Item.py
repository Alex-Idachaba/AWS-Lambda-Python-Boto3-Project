import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
# Get Item
resp = table.get_item(
    Key={
        'emp_id': '2'
    }
)

# Delete Item
deleted_item = table.delete_item(
    Key={
        'emp_id': '2'
    }
)
