import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

client = boto3.client('dynamodb')
deserializer = TypeDeserializer().deserialize
serializer = TypeSerializer().serialize


def get_item(table_name: str, key_value: str, key_attr: str = 'id') -> dict:
    try:
        get_result = client.get_item(
            TableName=table_name,
            Key={
                key_attr: {"S": key_value}
            }
        )
    except ClientError as err:
        raise err
    else:
        deserialised = {k: deserializer(v) for k, v in get_result.get(
            "Item").items() if k != 'id'}

        return deserialised


def put_item(table_name: str, item: dict) -> None:
    try:
        response = client.put_item(
            TableName=table_name,
            Item={k: serializer(v) for k, v in item.items()}
        )
    except ClientError as err:
        raise err
    else:
        print("Successfully put item: ", response)


def get_all_items(table_name: str) -> list:
    try:
        get_result = client.scan(
            TableName=table_name,
        )
    except ClientError as err:
        raise err
    else:
        itemsDeserialized = []
        for item in get_result.get('Items'):
            deserialized = {}
            for k, v in item.items():
                deserialized[k] = deserializer(v)

            itemsDeserialized.append(deserialized)

        return itemsDeserialized


def increment_location_index_for_user(sub_id: str) -> None:
    try:
        get_result = client.update_item(
            TableName="Users",
            Key={
                'id': {"S": sub_id}
            },
            ConditionExpression="attribute_exists(currentQwest.locationIndex)",
            UpdateExpression="ADD currentQwest.locationIndex :q",
            ExpressionAttributeValues={
                ":q": {"N": "1"}
            }
        )
    except ClientError as err:
        raise err
    else:
        print("Successfully incremented locationIndex for user")

# Ensures there is no currentQwest for user. If there is an error is thrown.


def start_current_qwest_for_user(sub_id: str, currentQwest: dict) -> None:
    try:
        get_result = client.update_item(
            TableName="Users",
            Key={
                'id': {"S": sub_id}
            },
            ConditionExpression="attribute_not_exists(currentQwest.locationIndex)",
            UpdateExpression="SET currentQwest.locationIndex = :loc, currentQwest.numOfLocations = :numl, currentQwest.qwestId = :qid, currentQwest.timeStarted = :time",
            ExpressionAttributeValues={
                ":loc": {'N': currentQwest['locationIndex']}, 
                ":numl": {'N': currentQwest['numOfLocations']},
                ":qid": {'S': currentQwest['qwestId']},
                ":time": {'S': currentQwest['timeStarted']}
            }
        )
    except ClientError as err:
        raise err
    else:
        print("Qwest successfully started")


def update_attribute_list_of_item(table_name: str, key_value: str, appended_obj: dict = {}, key_attr: str = 'id') -> None:
    try:
        appended_obj = serializer(appended_obj)
        print("This is object", appended_obj)
        get_result = client.update_item(
            TableName=table_name,
            Key={
                key_attr: {"S": key_value}
            },
            UpdateExpression="SET qwestsCompleted = list_append(if_not_exists(qwestsCompleted, :empty_list), :my_value)",
            ExpressionAttributeValues={
                ":my_value": {"L": [appended_obj]},
                ":empty_list": {"L": []}
            }
        )
    except ClientError as err:
        raise err
    else:
        print("Updated item: ", get_result)
