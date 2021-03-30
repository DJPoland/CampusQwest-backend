import json

from datetime import datetime
from utils.common_functions import obtainDataFromEvent
from utils.dynamodb_functions import get_item, increment_location_index_for_user, remove_current_qwest_for_user, update_attribute_list_of_item, put_item, set_timestamp_for_qwest

def finish_qwest(subId: str, timeStarted: str, qwestId: str, userItem: dict) -> None:
    # Get total time based on available UTC data
    datetimeTimeStarted = datetime.fromisoformat(timeStarted)
    datetimeCurrentTime = datetime.utcnow()
    totalTime = datetimeCurrentTime - datetimeTimeStarted
    totalTimeInSeconds = int(totalTime.total_seconds())
    
    # Add completed qwest to qwest completed
    update_attribute_list_of_item(table_name="Users", key_value=subId, appended_obj={'totalTime': totalTimeInSeconds, 'qwestId': qwestId})

    username = userItem['username']
    selectedAvatar = int(userItem['selectedAvatar'])
    put_item(table_name="all_recorded_times", item={'qwestId': qwestId, 'totalTime': totalTimeInSeconds, 'username': username, 'selectedAvatar': selectedAvatar})

    # Remove current qwest data from user item
    remove_current_qwest_for_user(subId)


def response_logic(currentQwest: dict, subId: str, userItem: dict) -> dict:
    nextLocation = int(currentQwest['locationIndex']) + 1
    numOfLocations = int(currentQwest['numOfLocations'])
    timeStarted = currentQwest['timeStarted'] if nextLocation > 1 else None
    qwestId = currentQwest['qwestId']


    if nextLocation < numOfLocations:

        if nextLocation == 1:
            set_timestamp_for_qwest(sub_id=subId, startTime=datetime.utcnow().isoformat())

        increment_location_index_for_user(subId)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'qwestComplete': False,
                'nextLocation': nextLocation
            })
        }
    elif nextLocation == numOfLocations:
        finish_qwest(subId=subId, timeStarted=timeStarted, qwestId=qwestId, userItem=userItem)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'qwestComplete': True,
            })
        }
    else:
        return {
            'statusCode': 409,
            'body': json.dumps({
                'Error': 'The database has invalid logic and needs to be fixed',
            })
        }

def lambda_handler(event, context):
    print("event is: ", event)
    method, path, subId = obtainDataFromEvent(event=event, getSubId=True)

    if not method or not path or path != '/user/location/nextLocation' or method != 'POST':
        return {
            'statusCode': 400
        }

    print("results: ", method, path, subId)
    userItem = get_item('Users', subId)
    currentQwest = userItem['currentQwest']
    if not currentQwest:
        return {
            'statusCode': 409,
            'body': json.dumps({
                'Error': 'CurrentQwest does not exist for User.'
            })
        }
    try:
        return response_logic(currentQwest=currentQwest, subId=subId, userItem=userItem)
    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps({
                'Error': 'Issue when updating database likely because a Qwest has not been started'
            })
        }