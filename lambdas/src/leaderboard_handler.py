import boto3
import json
from utils.common_functions import obtainDataFromEvent, decimal_default
from utils.dynamodb_functions import get_item

def leaderboard_data():
    campus_data = get_item('CampusData', 'UCF', 'campus')
    if not campus_data:
        raise Exception("The Campus UCF does not have data for leaderboards")
    elif 'qwestsOnCampus' not in campus_data:
        raise Exception("Database for leaderboard does not have qwestsOnCampus key")
    else:
        qwests_with_leaderboard = campus_data['qwestsOnCampus']
        return json.dumps(qwests_with_leaderboard, default=decimal_default)

def lambda_handler(event, context):
    print(event)
    method, path, _ = obtainDataFromEvent(event)

    if path == '/leaderboard' and method == 'GET':
        qwests_for_leaderboard = leaderboard_data()
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