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
from fdtapi.models.domain_bids import DomainBids  # noqa: E501
from fdtapi.rest import ApiException

class TestDomainBids(unittest.TestCase):
    """DomainBids unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DomainBids
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainBids`
        """
        model = fdtapi.models.domain_bids.DomainBids()  # noqa: E501
        if include_optional :
            return DomainBids(
                data = [
                    fdtapi.models.domain_bid.DomainBid(
                        success = True, 
                        value = 1660050553, 
                        tx_time = 1660050553, 
                        tx_hash = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        bidder = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), )
                    ]
            )
        else :
            return DomainBids(
                data = [
                    fdtapi.models.domain_bid.DomainBid(
                        success = True, 
                        value = 1660050553, 
                        tx_time = 1660050553, 
                        tx_hash = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        bidder = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), )
                    ],
        )
        """

    def testDomainBids(self):
        """Test DomainBids"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
