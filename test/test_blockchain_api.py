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

import fdtapi
from fdtapi.api.blockchain_api import BlockchainApi  # noqa: E501
from fdtapi.rest import ApiException


class TestBlockchainApi(unittest.TestCase):
    """BlockchainApi unit test stubs"""

    def setUp(self):
        self.api = fdtapi.api.blockchain_api.BlockchainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_exec_get_method_for_blockchain_account(self):
        """Test case for exec_get_method_for_blockchain_account

        """
        pass

    def test_get_blockchain_account_transactions(self):
        """Test case for get_blockchain_account_transactions

        """
        pass

    def test_get_blockchain_block(self):
        """Test case for get_blockchain_block

        """
        pass

    def test_get_blockchain_block_transactions(self):
        """Test case for get_blockchain_block_transactions

        """
        pass

    def test_get_blockchain_config(self):
        """Test case for get_blockchain_config

        """
        pass

    def test_get_blockchain_masterchain_head(self):
        """Test case for get_blockchain_masterchain_head

        """
        pass

    def test_get_blockchain_raw_account(self):
        """Test case for get_blockchain_raw_account

        """
        pass

    def test_get_blockchain_transaction(self):
        """Test case for get_blockchain_transaction

        """
        pass

    def test_get_blockchain_transaction_by_message_hash(self):
        """Test case for get_blockchain_transaction_by_message_hash

        """
        pass

    def test_get_blockchain_validators(self):
        """Test case for get_blockchain_validators

        """
        pass

    def test_send_blockchain_message(self):
        """Test case for send_blockchain_message

        """
        pass


if __name__ == '__main__':
    unittest.main()