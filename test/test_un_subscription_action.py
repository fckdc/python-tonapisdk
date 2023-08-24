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
from fdtapi.models.un_subscription_action import UnSubscriptionAction  # noqa: E501
from fdtapi.rest import ApiException

class TestUnSubscriptionAction(unittest.TestCase):
    """UnSubscriptionAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UnSubscriptionAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnSubscriptionAction`
        """
        model = fdtapi.models.un_subscription_action.UnSubscriptionAction()  # noqa: E501
        if include_optional :
            return UnSubscriptionAction(
                subscriber = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ), 
                subscription = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                beneficiary = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', )
            )
        else :
            return UnSubscriptionAction(
                subscriber = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ),
                subscription = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf',
                beneficiary = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ),
        )
        """

    def testUnSubscriptionAction(self):
        """Test UnSubscriptionAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
