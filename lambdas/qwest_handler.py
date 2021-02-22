import boto3
import json
import decimal
from utils.common_functions import obtainDataFromEvent
from utils.dynamodb_functions import get_all_items, get_item


def filter_qwests(qwests, campus, qwestsCompleted):
    filteredQwests = []
    for qwest in qwests:
        qwest.pop('locations', None)
        if qwest['campus'] == campus and qwest['id'] not in qwestsCompleted:
            filteredQwests.append(qwest)

    return filteredQwests

def get_qwests_for_user(subId):
    allQwests = get_all_items('Qwests')
    userItem = get_item('Users', subId)
    qwestsCompleted = set()
    if 'qwestsCompleted' in userItem:
        qwestsCompleted = {qwest['qwestId']
                           for qwest in userItem['qwestsCompleted']}
    qwestsForUser = filter_qwests(allQwests, "UCF", qwestsCompleted)

    return qwestsForUser


def lambda_handler(event, context):
    method, path, subId = obtainDataFromEvent(event, True)
    print("Method: ", method, "Path: ", path, "subId: ", subId)

    if path == '/user/qwests/fetchQwests' and method == 'GET':
        qwests = get_qwests_for_user(subId)
        return {
            'statusCode': 200,
            'body': json.dumps(qwests)
        }
    elif path == '/user/qwests/startQwest' and method == 'POST':
        print("test")
        # Get users completed qwests, and get all UCF related qwests that user has not completed
    else:
        return {
            'statusCode': 400
        }
