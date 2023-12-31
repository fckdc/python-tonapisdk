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
from fdtapi.models.get_staking_pool_info200_response import GetStakingPoolInfo200Response  # noqa: E501
from fdtapi.rest import ApiException

class TestGetStakingPoolInfo200Response(unittest.TestCase):
    """GetStakingPoolInfo200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetStakingPoolInfo200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStakingPoolInfo200Response`
        """
        model = fdtapi.models.get_staking_pool_info200_response.GetStakingPoolInfo200Response()  # noqa: E501
        if include_optional :
            return GetStakingPoolInfo200Response(
                implementation = fdtapi.models.pool_implementation.PoolImplementation(
                    name = 'TON Whales', 
                    description = 'Oldest pool with minimal staking amount 50 TON', 
                    url = 'https://tonvalidators.org/', ), 
                pool = fdtapi.models.pool_info.PoolInfo(
                    address = '0:48fb0195a7fc7454512377b9bd704503ded27f6e7c4c4a9d136fdab3ef9ec04c', 
                    name = 'Tonkeeper pool', 
                    total_amount = 56, 
                    implementation = 'whales', 
                    apy = 5.31, 
                    min_stake = 5000000000, 
                    cycle_start = 1678223064, 
                    cycle_end = 1678223064, 
                    verified = True, 
                    current_nominators = 10, 
                    max_nominators = 100, 
                    liquid_jetton_master = '0:4a91d32d0289bda9813ae00ff7640e6c38fdce76e4583dd6afc463b70c7d767c', 
                    nominators_stake = 5000000000, 
                    validator_stake = 5000000000, )
            )
        else :
            return GetStakingPoolInfo200Response(
                implementation = fdtapi.models.pool_implementation.PoolImplementation(
                    name = 'TON Whales', 
                    description = 'Oldest pool with minimal staking amount 50 TON', 
                    url = 'https://tonvalidators.org/', ),
                pool = fdtapi.models.pool_info.PoolInfo(
                    address = '0:48fb0195a7fc7454512377b9bd704503ded27f6e7c4c4a9d136fdab3ef9ec04c', 
                    name = 'Tonkeeper pool', 
                    total_amount = 56, 
                    implementation = 'whales', 
                    apy = 5.31, 
                    min_stake = 5000000000, 
                    cycle_start = 1678223064, 
                    cycle_end = 1678223064, 
                    verified = True, 
                    current_nominators = 10, 
                    max_nominators = 100, 
                    liquid_jetton_master = '0:4a91d32d0289bda9813ae00ff7640e6c38fdce76e4583dd6afc463b70c7d767c', 
                    nominators_stake = 5000000000, 
                    validator_stake = 5000000000, ),
        )
        """

    def testGetStakingPoolInfo200Response(self):
        """Test GetStakingPoolInfo200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
