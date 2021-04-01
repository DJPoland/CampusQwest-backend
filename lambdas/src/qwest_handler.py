import boto3
import json

from datetime import datetime
from urllib.parse import unquote
from utils.common_functions import obtainDataFromEvent, decimal_default
from utils.dynamodb_functions import get_all_items, get_item, start_current_qwest_for_user
from utils.schemas import CurrentQwest


def filter_qwests(qwests: list, campus: str, qwestsCompleted: set) -> list:
    filteredQwests = []
    for qwest in qwests:
        if qwest['campus'] == campus and qwest['id'] not in qwestsCompleted:
            filteredQwests.append(qwest)

    return filteredQwests


def get_qwests_for_user(subId: str) -> list:
    allQwests = get_all_items('Qwests')
    userItem = get_item('Users', subId)
    qwestsCompleted = set()
    if 'qwestsCompleted' in userItem:
        qwestsCompleted = {qwest['qwestId']
                           for qwest in userItem['qwestsCompleted']}

    return filter_qwests(allQwests, "UCF", qwestsCompleted)


def begin_qwest_for_user(subId: str, qwestId: str) -> None:
    qwestItem = get_item('Qwests', qwestId)
    print("qwestItem is:", qwestItem)

    totalLocations = str(qwestItem['numOfLocations'])
    print("total locations is:", totalLocations)

    currentQwest = CurrentQwest(qwestId=qwestId, locationIndex="0", numOfLocations=totalLocations)
    print("appended object: ", currentQwest)

    start_current_qwest_for_user(subId, currentQwest)


def lambda_handler(event, context):
    print(event)
    method, path, subId = obtainDataFromEvent(event, True)
    print("Method: ", method, "Path: ", path, "subId: ", subId)

    if path == '/user/qwests/fetchQwests' and method == 'GET':
        qwests = get_qwests_for_user(subId)

        return {
            'statusCode': 200,
            'body': json.dumps(qwests, default=decimal_default)
        }
    elif path == '/user/qwests/startQwest' and method == 'POST':
        jsonBody = unquote(event['body'])
        qwestId = json.loads(jsonBody)
        idString = str(qwestId['id'])
        print("subId is:", subId, " and id string is:", idString)
        try:
            begin_qwest_for_user(subId, idString)
        except Exception as err:
            print(err)
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'Error': "Qwest failed to start likely due to malformed data for user in database"
                })
            }
        else:
            return {
                'statusCode': 201
            }
    else:

        return {
            'statusCode': 400
        }
