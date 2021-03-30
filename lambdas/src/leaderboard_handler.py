import boto3
import json
from urllib.parse import unquote
from utils.common_functions import obtainDataFromEvent, decimal_default
from utils.dynamodb_functions import get_leaderboard_by_qwest

def leaderboard_data(qwestId: str) -> str:
    result = get_leaderboard_by_qwest(qwest_id=qwestId)

    return json.dumps(result, default=decimal_default)

def lambda_handler(event, context):
    print(event)
    method, path, _ = obtainDataFromEvent(event)

    event['body'] = unquote(event['body'])

    if path == '/leaderboard' and method == 'POST':
        body = json.loads(event['body'])
        qwestId = str(body['qwestId'])
        qwests_for_leaderboard = leaderboard_data(qwestId=qwestId)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": qwests_for_leaderboard
        }
    else:
        return {
            'statusCode': 400
        }