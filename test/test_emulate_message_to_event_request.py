# coding: utf-8

"""
    REST api to TON blockchain explorer

    Provide access to indexed TON blockchain  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@tonkeeper.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import fdtapi
from fdtapi.models.emulate_message_to_event_request import EmulateMessageToEventRequest  # noqa: E501
from fdtapi.rest import ApiException

class TestEmulateMessageToEventRequest(unittest.TestCase):
    """EmulateMessageToEventRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmulateMessageToEventRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmulateMessageToEventRequest`
        """
        model = fdtapi.models.emulate_message_to_event_request.EmulateMessageToEventRequest()  # noqa: E501
        if include_optional :
            return EmulateMessageToEventRequest(
                boc = 'te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg'
            )
        else :
            return EmulateMessageToEventRequest(
                boc = 'te6ccgECBQEAARUAAkWIAWTtae+KgtbrX26Bep8JSq8lFLfGOoyGR/xwdjfvpvEaHg',
        )
        """

    def testEmulateMessageToEventRequest(self):
        """Test EmulateMessageToEventRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
