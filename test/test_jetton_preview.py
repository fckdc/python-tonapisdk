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
from fdtapi.models.jetton_preview import JettonPreview  # noqa: E501
from fdtapi.rest import ApiException

class TestJettonPreview(unittest.TestCase):
    """JettonPreview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JettonPreview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JettonPreview`
        """
        model = fdtapi.models.jetton_preview.JettonPreview()  # noqa: E501
        if include_optional :
            return JettonPreview(
                address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                name = 'Wrapped TON', 
                symbol = 'WTON', 
                decimals = 9, 
                image = 'https://cache.tonapi.io/images/jetton.jpg', 
                verification = 'whitelist'
            )
        else :
            return JettonPreview(
                address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0',
                name = 'Wrapped TON',
                symbol = 'WTON',
                decimals = 9,
                image = 'https://cache.tonapi.io/images/jetton.jpg',
                verification = 'whitelist',
        )
        """

    def testJettonPreview(self):
        """Test JettonPreview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
