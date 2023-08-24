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
from fdtapi.models.jetton_swap_action import JettonSwapAction  # noqa: E501
from fdtapi.rest import ApiException

class TestJettonSwapAction(unittest.TestCase):
    """JettonSwapAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JettonSwapAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JettonSwapAction`
        """
        model = fdtapi.models.jetton_swap_action.JettonSwapAction()  # noqa: E501
        if include_optional :
            return JettonSwapAction(
                dex = 'stonfi', 
                amount_in = '1660050553', 
                amount_out = '1660050553', 
                user_wallet = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ), 
                router = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ), 
                jetton_wallet_in = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee', 
                jetton_master_in = fdtapi.models.jetton_preview.JettonPreview(
                    address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                    name = 'Wrapped TON', 
                    symbol = 'WTON', 
                    decimals = 9, 
                    image = 'https://cache.tonapi.io/images/jetton.jpg', 
                    verification = 'whitelist', ), 
                jetton_wallet_out = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee', 
                jetton_master_out = fdtapi.models.jetton_preview.JettonPreview(
                    address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                    name = 'Wrapped TON', 
                    symbol = 'WTON', 
                    decimals = 9, 
                    image = 'https://cache.tonapi.io/images/jetton.jpg', 
                    verification = 'whitelist', )
            )
        else :
            return JettonSwapAction(
                dex = 'stonfi',
                amount_in = '1660050553',
                amount_out = '1660050553',
                user_wallet = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ),
                router = fdtapi.models.account_address.AccountAddress(
                    address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                    name = 'Ton foundation', 
                    is_scam = True, 
                    icon = 'https://ton.org/logo.png', ),
                jetton_wallet_in = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee',
                jetton_master_in = fdtapi.models.jetton_preview.JettonPreview(
                    address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                    name = 'Wrapped TON', 
                    symbol = 'WTON', 
                    decimals = 9, 
                    image = 'https://cache.tonapi.io/images/jetton.jpg', 
                    verification = 'whitelist', ),
                jetton_wallet_out = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee',
                jetton_master_out = fdtapi.models.jetton_preview.JettonPreview(
                    address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                    name = 'Wrapped TON', 
                    symbol = 'WTON', 
                    decimals = 9, 
                    image = 'https://cache.tonapi.io/images/jetton.jpg', 
                    verification = 'whitelist', ),
        )
        """

    def testJettonSwapAction(self):
        """Test JettonSwapAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()