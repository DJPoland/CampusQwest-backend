import boto3
from boto3.dynamodb.types import TypeSerializer
from botocore.exceptions import ClientError
from utils.schemas import User

client = boto3.client('dynamodb')
serializer = TypeSerializer().serialize

def put_item(table_name, item):
    try:
        response = client.put_item(
            TableName=table_name,
            Item={ k: serializer(v) for k, v in item.items() }
        )
    except ClientError as err:
        raise err
    else:
        return response

def lambda_handler(event, context):
    print(event)

    if not event:
        raise Exception("Invalid event request")

    sub_id = event["request"]["userAttributes"]["sub"]
    campus_id = event["request"]["userAttributes"]["custom:campus"]
    user_name = event['userName']

    # TODO: frontend needs to verify campus
    create_user = User(
        id=sub_id,
        avatar="default",
        badges=["default"],
        banner="default",
        campus=campus_id,
        exp=0,
        username=user_name,
        trophies=[],
        qwestLines=[],
    )

    put_item('Users', create_user)
    print(create_user)

    return {
        'statusCode': 200,
    }
