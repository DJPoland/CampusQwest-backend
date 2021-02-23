from boto3.dynamodb.types import TypeDeserializer

serializer = TypeSerializer().serialize

def obtainDataFromEvent(event, getSubId=False):
    requestContext = event["requestContext"]

    subId = None
    if getSubId:
        subId = requestContext["authorizer"]["jwt"]["claims"]["sub"]

    method = requestContext["http"]["method"]
    path = requestContext["http"]["path"]

    return method, path, subId

def serializeDatamodelForDynamoDb(classObj):
    return { k: serializer(v) for k, v in classObj.Schema().dump(item).items() }