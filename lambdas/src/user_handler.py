import boto3
import json
import decimal
from utils.common_functions import obtainDataFromEvent
from utils.dynamodb_functions import get_item

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)

def user_endpoint(subId):
    user_item = get_item('Users', subId)
    return json.dumps(user_data, default=decimal_default)

def update_profile_endpoint():
    pass


def lambda_handler(event, context):
    print(event)
    method, path, subId = obtainDataFromEvent(event, True)

    if path == '/user' and method == 'GET':
        user_data = user_endpoint(subId)
        return {
            'statusCode': 200,
            'body': user_data
        }
    elif path == '/user/updateProfile' and method == 'POST':
        return update_profile_endpoint(subId)
        # edit profile for user based on payload
    else:
        return {
            'statusCode': 400
        }