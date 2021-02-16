import boto3
import json
from boto3.dynamodb.types import TypeDeserializer
from botocore.exceptions import ClientError
from marshmallow_dataclass import dataclass as marshmallow_dataclass
from marshmallow import EXCLUDE

client = boto3.client('dynamodb')
deserializer = TypeDeserializer()

@marshmallow_dataclass
class User:
    id: str
    avatar: str
    badges: list
    banner: str
    campus: str
    exp: int
    username: str
    trophies: list
    qwestLines: list

def get_item(table_name, key):
    try:
        get_result = client.get_item(
            TableName=table_name,
            Key={
                "id": {"S": key}
            }
        )
    except ClientError as err:
        raise err
    else:
        deserialised = {k: deserializer.deserialize(v) for k, v in get_result.get("Item").items() if k and k != 'id' }
        print("Deserialization is: ", deserialised)
        return User.Schema().load(deserialised, unknown=EXCLUDE)


def lambda_handler(event, context):
    if not event:
        raise Exception("Invalid event request")

    if "username" not in event:
        raise Exception("User ID not specified in payload")
    
    user_data = get_item('Users', event["username"])
    print(user_data)
    return {
        'statusCode': 200,
        'message': json.dumps(user_data)
    }
