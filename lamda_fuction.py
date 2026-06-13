import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LeaveRequests')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    leave_id = str(uuid.uuid4())

    item = {
        'leave_id': leave_id,
        'employee_name': body['employee_name'],
        'leave_type': body['leave_type'],
        'status': 'Pending'
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Leave Request Submitted',
            'leave_id': leave_id
        })
    }
