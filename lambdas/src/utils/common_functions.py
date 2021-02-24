from boto3.dynamodb.types import TypeSerializer

serializer = TypeSerializer().serialize

def obtainDataFromEvent(event, getSubId=False):
    requestContext = event.requestContext

    subId = None
    if getSubId:
        subId = requestContext.authorizer.jwt.claims.sub

    method, path = requestContext.http
    return method, path, subId
