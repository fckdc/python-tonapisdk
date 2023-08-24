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
from fdtapi.models.get_account_public_key200_response import GetAccountPublicKey200Response  # noqa: E501
from fdtapi.rest import ApiException

class TestGetAccountPublicKey200Response(unittest.TestCase):
    """GetAccountPublicKey200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetAccountPublicKey200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountPublicKey200Response`
        """
        model = fdtapi.models.get_account_public_key200_response.GetAccountPublicKey200Response()  # noqa: E501
        if include_optional :
            return GetAccountPublicKey200Response(
                public_key = 'NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ3...'
            )
        else :
            return GetAccountPublicKey200Response(
                public_key = 'NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ3...',
        )
        """

    def testGetAccountPublicKey200Response(self):
        """Test GetAccountPublicKey200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
