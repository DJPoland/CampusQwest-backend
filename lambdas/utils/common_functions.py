def obtainDataFromEvent(event, getSubId=False):
    requestContext = event["requestContext"]

    subId = None
    if getSubId:
        subId = requestContext["authorizer"]["jwt"]["claims"]["sub"]

    method = requestContext["http"]["method"]
    path = requestContext["http"]["path"]

    return method, path, subId