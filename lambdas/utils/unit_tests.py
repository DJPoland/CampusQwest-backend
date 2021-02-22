import unittest
from common_functions import obtainDataFromEvent

event_json = {
    "version": "2.0",
    "routeKey": "GET /user/qwests/fetchQwests",
    "rawPath": "/user/qwests/fetchQwests",
    "rawQueryString": "",
    "headers": {
        "authorization": "",
        "content-length": "0",
        "host": "",
        "x-amzn-trace-id": "",
        "x-forwarded-for": "",
        "x-forwarded-port": "",
        "x-forwarded-proto": "",
    },
    "requestContext": {
        "accountId": "236049568950",
        "apiId": "0evhdn85ei",
        "authorizer": {
            "jwt": {
                "claims": {
                    "auth_time": "",
                    "client_id": "",
                    "event_id": "",
                    "exp": "",
                    "iat": "",
                    "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_t",
                    "jti": "000000-00c-4ec8-a00f-edc6a98ee52e",
                    "scope": "aws.cognito.signin.user.admin",
                    "sub": "a0d0aee8-0fe5-4c8d-9523-26036ff0c246",
                    "token_use": "access",
                    "username": "test",
                },
                "scopes": None,
            }
        },
        "domainName": "0evhdn85ei.execute-api.us-east-1.amazonaws.com",
        "domainPrefix": "0evhdn85ei",
        "http": {
            "method": "GET",
            "path": "/user/qwests/fetchQwests",
            "protocol": "HTTP/1.1",
            "sourceIp": "",
            "userAgent": "",
        },
        "requestId": "",
        "routeKey": "GET /user/qwests/fetchQwests",
        "stage": "$default",
        "time": "21/Feb/2021:22:56:41 +0000",
        "timeEpoch": 1613948201895,
    },
    "isBase64Encoded": False,
}


class TestAPIGatewayJson(unittest.TestCase):
    def test_json(self):
        method, path, subId = obtainDataFromEvent(event_json)
        self.assertEqual(method, "GET")
        self.assertEqual(path, "/user/qwests/fetchQwests")
        self.assertEqual(subId, "000000-00c-4ec8-a00f-edc6a98ee52e")


if __name__ == "__main__":
    unittest.main(verbosity=2)