import json

from utils.common_functions import obtainDataFromEvent
from utils.dynamodb_functions import increment_location_index_for_user

def finish_qwest(subId):
    # Get currentQwest.qwestId and currentQwest.timeStarted
    # Get current time and subtract currentQwest.timeEnded
    # Append {qwestId: currentQwest.qwestId, totalTime: totalTime}
    # Remove current Qwest from user item.

def response_logic(currentQwest, subId)
    nextLocation = int(currentQwest.locationIndex) + 1
    if nextLocation < currentQwest.numOfLocations:
        increment_location_index_for_user(subId)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'qwestComplete': False,
                'nextLocation': currentQwest.locationIndex + 1,
            })
        }
    elif nextLocation == currentQwest.numOfLocations:
        finish_qwest(subId)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'qwestComplete': True,
            })
        }
    else:
        return {
            'statusCode': 409,
            'body' json.dumps({
                'Error': 'The database has invalid logic and needs to be fixed',
            })
        }

def lambda_handler(event, context):
    print(event)
    method, path, subId = obtainDataFromEvent(event)

    if not method or not path or path != '/user/location/nextLocation' or method != 'POST':
        return {
            'statusCode': 400
        }

    userItem = get_item('Users', subId)
    currentQwest = userItem['currentQwest']
    if not currentQwest:
        return {
            'statusCode': 409,
            'body': json.dumps({
                'Error': 'CurrentQwest does not exist for User.'
            })
        }

    return response_logic(currentQwest)