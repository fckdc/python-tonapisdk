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
from fdtapi.models.validators_set import ValidatorsSet  # noqa: E501
from fdtapi.rest import ApiException

class TestValidatorsSet(unittest.TestCase):
    """ValidatorsSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ValidatorsSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidatorsSet`
        """
        model = fdtapi.models.validators_set.ValidatorsSet()  # noqa: E501
        if include_optional :
            return ValidatorsSet(
                utime_since = 56, 
                utime_until = 56, 
                total = 56, 
                main = 56, 
                total_weight = 56, 
                list = [
                    fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                        public_key = '', )
                    ]
            )
        else :
            return ValidatorsSet(
                utime_since = 56,
                utime_until = 56,
                total = 56,
                main = 56,
                list = [
                    fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                        public_key = '', )
                    ],
        )
        """

    def testValidatorsSet(self):
        """Test ValidatorsSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
