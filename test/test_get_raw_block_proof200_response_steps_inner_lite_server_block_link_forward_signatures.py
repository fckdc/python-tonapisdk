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
from fdtapi.models.get_raw_block_proof200_response_steps_inner_lite_server_block_link_forward_signatures import GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures  # noqa: E501
from fdtapi.rest import ApiException

class TestGetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures(unittest.TestCase):
    """GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures`
        """
        model = fdtapi.models.get_raw_block_proof200_response_steps_inner_lite_server_block_link_forward_signatures.GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures()  # noqa: E501
        if include_optional :
            return GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures(
                validator_set_hash = 56, 
                catchain_seqno = 56, 
                signatures = [
                    fdtapi.models.get_raw_block_proof_200_response_steps_inner_lite_server_block_link_forward_signatures_signatures_inner.getRawBlockProof_200_response_steps_inner_lite_server_block_link_forward_signatures_signatures_inner(
                        node_id_short = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85', 
                        signature = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85', )
                    ]
            )
        else :
            return GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures(
                validator_set_hash = 56,
                catchain_seqno = 56,
                signatures = [
                    fdtapi.models.get_raw_block_proof_200_response_steps_inner_lite_server_block_link_forward_signatures_signatures_inner.getRawBlockProof_200_response_steps_inner_lite_server_block_link_forward_signatures_signatures_inner(
                        node_id_short = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85', 
                        signature = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85', )
                    ],
        )
        """

    def testGetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures(self):
        """Test GetRawBlockProof200ResponseStepsInnerLiteServerBlockLinkForwardSignatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()