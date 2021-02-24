import unittest
import json_data
from src.qwest_handler import lambda_handler as qwest_handler
from src.location_handler import lambda_handler as location_handler
from src.user_handler import lambda_handler as user_handler
from src.confirmation_handler import lambda_handler as confirmation_handler
from src.leaderboard_handler import lambda_handler as leaderboard_handler


# class TestAPIGatewayJson(unittest.TestCase):
#     def test_qwest_handler(self):
#         q_handler(event_json, None)

if __name__ == "__main__":
    result = confirmation_handler(event_json_confirmation, None)
    print(result)
    # unittest.main(verbosity=2)
