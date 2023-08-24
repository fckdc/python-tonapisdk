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
from fdtapi.models.blockchain_config import BlockchainConfig  # noqa: E501
from fdtapi.rest import ApiException

class TestBlockchainConfig(unittest.TestCase):
    """BlockchainConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlockchainConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockchainConfig`
        """
        model = fdtapi.models.blockchain_config.BlockchainConfig()  # noqa: E501
        if include_optional :
            return BlockchainConfig(
                raw = 'te6ccgEBBgEARAABFP8A9KQT9LzyyAsBAgEgAgMCAUgEBQAE8jAAONBsIdMfMO1E0NM/MAHAAZekyMs/ye1UkzDyBuIAEaE0MdqJoaZ+YQ==', 
                var_0 = '', 
                var_1 = '', 
                var_2 = '', 
                var_4 = '', 
                var_32 = fdtapi.models.validators_set.ValidatorsSet(
                    utime_since = 56, 
                    utime_until = 56, 
                    total = 56, 
                    main = 56, 
                    total_weight = 56, 
                    list = [
                        fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                            public_key = '', )
                        ], ), 
                var_33 = fdtapi.models.validators_set.ValidatorsSet(
                    utime_since = 56, 
                    utime_until = 56, 
                    total = 56, 
                    main = 56, 
                    total_weight = 56, 
                    list = [
                        fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                            public_key = '', )
                        ], ), 
                var_34 = fdtapi.models.validators_set.ValidatorsSet(
                    utime_since = 56, 
                    utime_until = 56, 
                    total = 56, 
                    main = 56, 
                    total_weight = 56, 
                    list = [
                        fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                            public_key = '', )
                        ], ), 
                var_35 = fdtapi.models.validators_set.ValidatorsSet(
                    utime_since = 56, 
                    utime_until = 56, 
                    total = 56, 
                    main = 56, 
                    total_weight = 56, 
                    list = [
                        fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                            public_key = '', )
                        ], ), 
                var_36 = fdtapi.models.validators_set.ValidatorsSet(
                    utime_since = 56, 
                    utime_until = 56, 
                    total = 56, 
                    main = 56, 
                    total_weight = 56, 
                    list = [
                        fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                            public_key = '', )
                        ], ), 
                var_37 = fdtapi.models.validators_set.ValidatorsSet(
                    utime_since = 56, 
                    utime_until = 56, 
                    total = 56, 
                    main = 56, 
                    total_weight = 56, 
                    list = [
                        fdtapi.models.validators_set_list_inner.ValidatorsSet_list_inner(
                            public_key = '', )
                        ], )
            )
        else :
            return BlockchainConfig(
                raw = 'te6ccgEBBgEARAABFP8A9KQT9LzyyAsBAgEgAgMCAUgEBQAE8jAAONBsIdMfMO1E0NM/MAHAAZekyMs/ye1UkzDyBuIAEaE0MdqJoaZ+YQ==',
                var_0 = '',
                var_1 = '',
                var_2 = '',
                var_4 = '',
        )
        """

    def testBlockchainConfig(self):
        """Test BlockchainConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()