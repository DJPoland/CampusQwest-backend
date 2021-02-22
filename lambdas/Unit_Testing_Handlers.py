import unittest
from utils.common_functions import obtainDataFromEvent
from qwest_handler import lambda_handler as q_handler
from leaderboard_handler import lambda_handler as l_handler

# TODO: Should move this stuff below to another file
event_json_fetchQwests = {
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
                    "sub": "6ca50b89-7445-4805-bcb7-aee24feb3191",
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

event_json_leaderboard = {
    "version": "2.0",
    "routeKey": "GET /leaderboard",
    "rawPath": "/leaderboard",
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
                    "sub": "6ca50b89-7445-4805-bcb7-aee24feb3191",
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
            "path": "/leaderboard",
            "protocol": "HTTP/1.1",
            "sourceIp": "",
            "userAgent": "",
        },
        "requestId": "",
        "routeKey": "GET /leaderboard",
        "stage": "$default",
        "time": "21/Feb/2021:22:56:41 +0000",
        "timeEpoch": 1613948201895,
    },
    "isBase64Encoded": False,
}


# class TestAPIGatewayJson(unittest.TestCase):
#     def test_qwest_handler(self):
#         q_handler(event_json, None)


if __name__ == "__main__":
    result = l_handler(event_json_leaderboard, None)
    print(result)
    # unittest.main(verbosity=2)