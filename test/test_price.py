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
from fdtapi.models.price import Price  # noqa: E501
from fdtapi.rest import ApiException

class TestPrice(unittest.TestCase):
    """Price unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Price
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Price`
        """
        model = fdtapi.models.price.Price()  # noqa: E501
        if include_optional :
            return Price(
                value = '123000000000', 
                token_name = 'TON'
            )
        else :
            return Price(
                value = '123000000000',
                token_name = 'TON',
        )
        """

    def testPrice(self):
        """Test Price"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
