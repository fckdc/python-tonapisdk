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
from fdtapi.models.dns_record import DnsRecord  # noqa: E501
from fdtapi.rest import ApiException

class TestDnsRecord(unittest.TestCase):
    """DnsRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DnsRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsRecord`
        """
        model = fdtapi.models.dns_record.DnsRecord()  # noqa: E501
        if include_optional :
            return DnsRecord(
                wallet = fdtapi.models.wallet_dns.WalletDNS(
                    address = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                    is_wallet = True, 
                    has_method_pubkey = True, 
                    has_method_seqno = True, 
                    names = [
                        'name'
                        ], ), 
                next_resolver = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                sites = [
                    'http://12234.ton'
                    ], 
                storage = 'da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf'
            )
        else :
            return DnsRecord(
                sites = [
                    'http://12234.ton'
                    ],
        )
        """

    def testDnsRecord(self):
        """Test DnsRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()