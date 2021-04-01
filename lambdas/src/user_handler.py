import boto3
import json
from urllib.parse import unquote
from utils.common_functions import obtainDataFromEvent, decimal_default
from utils.dynamodb_functions import get_item, update_profile_selected_avatar, update_profile_selected_banner


def user_endpoint(subId: str):
    user_item = get_item('Users', subId)
    return json.dumps(user_item, default=decimal_default)

def update_profile_endpoint(subId: str, json_obj: dict):
    try:
        if 'selectedAvatar' in json_obj:
            selectedAvatar = str(json_obj['selectedAvatar'])
            update_profile_selected_avatar(sub_id=subId, selected_avatar=selectedAvatar)
        elif 'selectedBanner' in json_obj:
            selectedBanner = str(json_obj['selectedBanner'])
            update_profile_selected_banner(sub_id=subId, selected_banner=selectedBanner)
        else:
            raise Exception("No avatar or banner in body!")

    except Exception as err:
        print("Error with updating user profile due to: ", err)
        raise err

def lambda_handler(event, context):
    print(event)
    method, path, subId = obtainDataFromEvent(event=event, getSubId=True)

    if path == '/user' and method == 'GET':
        user_data = user_endpoint(subId)
        return {
            'statusCode': 200,
            'body': user_data
        }
    elif path == '/user/updateProfile' and method == 'POST':
        jsonBody = unquote(event['body'])
        jsonBodyObj = json.loads(jsonBody)
        update_profile_data = update_profile_endpoint(subId=subId, json_obj=jsonBodyObj)
        return {
            'statusCode': 201,
            'body': update_profile_data
        }
    else:
        return {
            'statusCode': 400
        }