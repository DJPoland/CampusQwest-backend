import boto3
from boto3.dynamodb.types import TypeSerializer
from botocore.exceptions import ClientError
from utils.schemas import User
from utils.dynamodb_functions import put_item

def lambda_handler(event, context):
    print(event)

    if not event:
        raise Exception("Invalid event request")

    sub_id = event["request"]["userAttributes"]["sub"]
    campus_id = event["request"]["userAttributes"]["custom:campus"]
    user_name = event['userName']

    create_user = User(
        id=sub_id,
        campus=campus_id,
        exp=0,
        rank="Rank 1",
        selectedAvatar=0,
        selectedBanner=0,
        trophies=[0 for _ in range(8)],
        medals=[0 for _ in range(10)],
        username=user_name,
        currentQwest={},
        qwestsCompleted=[]
    )

    put_item('Users', create_user)
    print("Created user: ", create_user)

    return {
        'statusCode': 200,
    }
