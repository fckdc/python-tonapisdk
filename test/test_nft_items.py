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
from fdtapi.models.nft_items import NftItems  # noqa: E501
from fdtapi.rest import ApiException

class TestNftItems(unittest.TestCase):
    """NftItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NftItems
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NftItems`
        """
        model = fdtapi.models.nft_items.NftItems()  # noqa: E501
        if include_optional :
            return NftItems(
                nft_items = [
                    fdtapi.models.nft_item.NftItem(
                        address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                        index = 58, 
                        owner = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        collection = fdtapi.models.nft_item_collection.NftItem_collection(
                            address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                            name = 'TON Diamonds', 
                            description = 'Best collection in TON network', ), 
                        verified = True, 
                        metadata = {}, 
                        sale = fdtapi.models.sale.Sale(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            market = fdtapi.models.account_address.AccountAddress(
                                address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                name = 'Ton foundation', 
                                is_scam = True, 
                                icon = 'https://ton.org/logo.png', ), 
                            price = fdtapi.models.price.Price(
                                value = '123000000000', 
                                token_name = 'TON', ), ), 
                        previews = [
                            fdtapi.models.image_preview.ImagePreview(
                                resolution = '100x100', 
                                url = 'https://site.com/pic1.jpg', )
                            ], 
                        dns = 'crypto.ton', 
                        approved_by = [
                            'getgems'
                            ], )
                    ]
            )
        else :
            return NftItems(
                nft_items = [
                    fdtapi.models.nft_item.NftItem(
                        address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                        index = 58, 
                        owner = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        collection = fdtapi.models.nft_item_collection.NftItem_collection(
                            address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                            name = 'TON Diamonds', 
                            description = 'Best collection in TON network', ), 
                        verified = True, 
                        metadata = {}, 
                        sale = fdtapi.models.sale.Sale(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            market = fdtapi.models.account_address.AccountAddress(
                                address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                name = 'Ton foundation', 
                                is_scam = True, 
                                icon = 'https://ton.org/logo.png', ), 
                            price = fdtapi.models.price.Price(
                                value = '123000000000', 
                                token_name = 'TON', ), ), 
                        previews = [
                            fdtapi.models.image_preview.ImagePreview(
                                resolution = '100x100', 
                                url = 'https://site.com/pic1.jpg', )
                            ], 
                        dns = 'crypto.ton', 
                        approved_by = [
                            'getgems'
                            ], )
                    ],
        )
        """

    def testNftItems(self):
        """Test NftItems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
