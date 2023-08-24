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
from fdtapi.models.jettons_balances import JettonsBalances  # noqa: E501
from fdtapi.rest import ApiException

class TestJettonsBalances(unittest.TestCase):
    """JettonsBalances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JettonsBalances
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JettonsBalances`
        """
        model = fdtapi.models.jettons_balances.JettonsBalances()  # noqa: E501
        if include_optional :
            return JettonsBalances(
                balances = [
                    fdtapi.models.jetton_balance.JettonBalance(
                        balance = '597968399', 
                        wallet_address = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        jetton = fdtapi.models.jetton_preview.JettonPreview(
                            address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                            name = 'Wrapped TON', 
                            symbol = 'WTON', 
                            decimals = 9, 
                            image = 'https://cache.tonapi.io/images/jetton.jpg', 
                            verification = 'whitelist', ), )
                    ]
            )
        else :
            return JettonsBalances(
                balances = [
                    fdtapi.models.jetton_balance.JettonBalance(
                        balance = '597968399', 
                        wallet_address = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        jetton = fdtapi.models.jetton_preview.JettonPreview(
                            address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                            name = 'Wrapped TON', 
                            symbol = 'WTON', 
                            decimals = 9, 
                            image = 'https://cache.tonapi.io/images/jetton.jpg', 
                            verification = 'whitelist', ), )
                    ],
        )
        """

    def testJettonsBalances(self):
        """Test JettonsBalances"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
