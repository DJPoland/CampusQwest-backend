from utils.common_functions import obtainDataFromEvent

def lambda_handler(event, context):
    print(event)
    method, path, subId = obtainDataFromEvent(event)

    if not method or not path:
        return {
            'statusCode': 400
        }

    if path == '/user/location/nextLocation' and method == 'POST':
        # check qwestId for next location (or increment), then update locationId for user.
        # no need for qwest complete since this endpoint will return a boolean indicating complete or not.
        return {
            'statusCode': 200,
            'body': 'qwestComplete: false, nextLocation: 2, locationObject: (location object from database)'
        }
    elif path == '/user/location/updateThermometer' and method == 'POST':
        pass
