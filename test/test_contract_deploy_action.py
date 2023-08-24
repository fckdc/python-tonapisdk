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
from fdtapi.models.contract_deploy_action import ContractDeployAction  # noqa: E501
from fdtapi.rest import ApiException

class TestContractDeployAction(unittest.TestCase):
    """ContractDeployAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractDeployAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractDeployAction`
        """
        model = fdtapi.models.contract_deploy_action.ContractDeployAction()  # noqa: E501
        if include_optional :
            return ContractDeployAction(
                address = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                interfaces = ["nft_item","nft_royalty"]
            )
        else :
            return ContractDeployAction(
                address = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf',
                interfaces = ["nft_item","nft_royalty"],
        )
        """

    def testContractDeployAction(self):
        """Test ContractDeployAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()