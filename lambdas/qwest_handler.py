import boto3
import json
import decimal

from datetime import datetime
from utils.common_functions import obtainDataFromEvent, serializeDatamodelForDynamoDb
from utils.dynamodb_functions import get_all_items, get_item, update_attribute_list_of_item
from datamodels.common_datamodels import CurrentQwest


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
    currentQwest = CurrentQwest("0", qwestId, datetime.utcnow().isoformat)
    append_obj = serializeDatamodelForDynamoDb(currentQwest)
    update_attribute_list_of_item('Users', subId, append_obj)


def lambda_handler(event, context):
    print(event)
    # method, path, subId = obtainDataFromEvent(event, True)
    # print("Method: ", method, "Path: ", path, "subId: ", subId)

    # if path == '/user/qwests/fetchQwests' and method == 'GET':
    #     qwests = get_qwests_for_user(subId)
    #     return {
    #         'statusCode': 200,
    #         'body': json.dumps(qwests)
    #     }
    # elif path == '/user/qwests/startQwest' and method == 'POST':
    #     qwests = 
    #     # Get users completed qwests, and get all UCF related qwests that user has not completed
    # else:
    #     return {
    #         'statusCode': 400
    #     }
