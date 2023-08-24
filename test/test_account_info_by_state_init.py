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
from fdtapi.models.account_info_by_state_init import AccountInfoByStateInit  # noqa: E501
from fdtapi.rest import ApiException

class TestAccountInfoByStateInit(unittest.TestCase):
    """AccountInfoByStateInit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountInfoByStateInit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountInfoByStateInit`
        """
        model = fdtapi.models.account_info_by_state_init.AccountInfoByStateInit()  # noqa: E501
        if include_optional :
            return AccountInfoByStateInit(
                public_key = 'NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ3...', 
                address = '0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b'
            )
        else :
            return AccountInfoByStateInit(
                public_key = 'NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ3...',
                address = '0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b',
        )
        """

    def testAccountInfoByStateInit(self):
        """Test AccountInfoByStateInit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()