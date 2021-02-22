import boto3
from boto3.dynamodb.types import TypeSerializer
from botocore.exceptions import ClientError
from marshmallow_dataclass import dataclass as marshmallow_dataclass

client = boto3.client('dynamodb')
serializer = TypeSerializer().serialize

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

def put_item(table_name, item):
    try:
        response = client.put_item(
            TableName=table_name,
            Item={ k: serializer(v) for k, v in User.Schema().dump(item).items() }
        )
    except ClientError as err:
        raise err
    else:
        return response

def lambda_handler(event, context):
    print(event)

    if not event:
        raise Exception("Invalid event request")

    subId = event['request']['userAttributes']['sub'] 
    user_name = event['userName']
    # TODO: frontend needs to verify campus
    create_user = User(
        subId,
        "default",
        ["default"],
        "default",
        "",
        0,
        user_name,
        [],
        [],
    )
    put_item('Users', create_user)
    print(create_user)

    return {
        'statusCode': 200,
    }
