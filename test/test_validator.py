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
from fdtapi.models.validator import Validator  # noqa: E501
from fdtapi.rest import ApiException

class TestValidator(unittest.TestCase):
    """Validator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Validator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Validator`
        """
        model = fdtapi.models.validator.Validator()  # noqa: E501
        if include_optional :
            return Validator(
                address = '0:55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122'
            )
        else :
            return Validator(
                address = '0:55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122',
        )
        """

    def testValidator(self):
        """Test Validator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()