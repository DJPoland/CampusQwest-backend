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
            Item={ k: serializer(v) for k, v in item.items() }
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

def update_attribute_list_of_item(table_name: str, key_value: str, appended_obj: dict = {}, key_attr: str = 'id') -> None:
    try:
        appended_obj = serializer(appended_obj)
        print("This is object", appended_obj)
        get_result = client.update_item(
            TableName=table_name,
            Key={
                key_attr: {"S": key_value}
            },
            UpdateExpression="SET currentQwests = list_append(if_not_exists(currentQwests, :empty_list), :my_value)",
            ExpressionAttributeValues={
                ":my_value": {"L": [appended_obj]},
                ":empty_list": {"L": []}
            }
        )
    except ClientError as err:
        raise err
    else:
        print("Updated item: ", get_result)