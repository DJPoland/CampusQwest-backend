import boto3
import json
import decimal

from datetime import datetime
from utils.common_functions import obtainDataFromEvent
from utils.dynamodb_functions import get_all_items, get_item, update_attribute_list_of_item
from utils.schemas import CurrentQwest


def filter_qwests(qwests, campus, qwestsCompleted):
    filteredQwests = []
    for qwest in qwests:
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

def begin_qwest_for_user(subId, qwestId):
    currentQwest = CurrentQwest(locationIndex="4", qwestId=qwestId, timeStarted=datetime.utcnow().isoformat())
    print("appended object: ", currentQwest)
    update_attribute_list_of_item('Users', subId, currentQwest)


def lambda_handler(event, context):
    print(event)
    method, path, subId = obtainDataFromEvent(event, True)
    print("Method: ", method, "Path: ", path, "subId: ", subId)

    if path == '/user/qwests/fetchQwests' and method == 'GET':
        qwests = get_qwests_for_user(subId)
        return {
            'statusCode': 200,
            'body': json.dumps(qwests)
        }
    elif path == '/user/qwests/startQwest' and method == 'POST':
        qwestId = json.loads(event['body'])
        idString = qwestId['id']
        begin_qwest_for_user(subId, idString)
        return {
            'statusCode': 201
        }
    else:
        return {
            'statusCode': 400
        }
