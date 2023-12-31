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
from fdtapi.models.get_raw_shard_block_proof200_response_links_inner import GetRawShardBlockProof200ResponseLinksInner  # noqa: E501
from fdtapi.rest import ApiException

class TestGetRawShardBlockProof200ResponseLinksInner(unittest.TestCase):
    """GetRawShardBlockProof200ResponseLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRawShardBlockProof200ResponseLinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRawShardBlockProof200ResponseLinksInner`
        """
        model = fdtapi.models.get_raw_shard_block_proof200_response_links_inner.GetRawShardBlockProof200ResponseLinksInner()  # noqa: E501
        if include_optional :
            return GetRawShardBlockProof200ResponseLinksInner(
                id = fdtapi.models.block_raw.BlockRaw(
                    workchain = 4294967295, 
                    shard = 56, 
                    seqno = 30699640, 
                    root_hash = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85', 
                    file_hash = 'A6A0BD6608672B11B79538A50B2204E748305C12AA0DED9C16CF0006CE3AF8DB', ), 
                proof = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85'
            )
        else :
            return GetRawShardBlockProof200ResponseLinksInner(
                id = fdtapi.models.block_raw.BlockRaw(
                    workchain = 4294967295, 
                    shard = 56, 
                    seqno = 30699640, 
                    root_hash = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85', 
                    file_hash = 'A6A0BD6608672B11B79538A50B2204E748305C12AA0DED9C16CF0006CE3AF8DB', ),
                proof = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85',
        )
        """

    def testGetRawShardBlockProof200ResponseLinksInner(self):
        """Test GetRawShardBlockProof200ResponseLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
