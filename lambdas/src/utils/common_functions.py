import decimal
from boto3.dynamodb.types import TypeSerializer

serializer = TypeSerializer().serialize

def obtainDataFromEvent(event, getSubId=False):
    requestContext = event["requestContext"]

    subId = None
    if getSubId:
        subId = requestContext["authorizer"]["jwt"]["claims"]["sub"]

    httpObject = requestContext["http"]
    method, path = httpObject["method"], httpObject["path"]
    return method, path, subId

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
