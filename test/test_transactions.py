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
from fdtapi.models.transactions import Transactions  # noqa: E501
from fdtapi.rest import ApiException

class TestTransactions(unittest.TestCase):
    """Transactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Transactions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Transactions`
        """
        model = fdtapi.models.transactions.Transactions()  # noqa: E501
        if include_optional :
            return Transactions(
                transactions = [
                    fdtapi.models.transaction.Transaction(
                        hash = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        lt = 25713146000001, 
                        account = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        success = True, 
                        utime = 1645544908, 
                        orig_status = 'active', 
                        end_status = 'active', 
                        total_fees = 25713146000001, 
                        transaction_type = 'TransOrd', 
                        state_update_old = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        state_update_new = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        in_msg = fdtapi.models.message.Message(
                            created_lt = 25713146000001, 
                            ihr_disabled = True, 
                            bounce = True, 
                            bounced = True, 
                            value = 60000000, 
                            fwd_fee = 5681002, 
                            ihr_fee = 5681002, 
                            destination = fdtapi.models.account_address.AccountAddress(
                                address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                name = 'Ton foundation', 
                                is_scam = True, 
                                icon = 'https://ton.org/logo.png', ), 
                            source = , 
                            import_fee = 5681002, 
                            created_at = 5681002, 
                            op_code = '0xdeadbeaf', 
                            init = fdtapi.models.state_init.StateInit(
                                boc = 'te6ccgEBBgEARAABFP8A9KQT9LzyyAsBAgEgAgMCAUgEBQAE8jAAONBsIdMfMO1E0NM/MAHAAZekyMs/ye1UkzDyBuIAEaE0MdqJoaZ+YQ==', ), 
                            raw_body = 'B5EE9C7201010101001100001D00048656C6C6F2C20776F726C64218', 
                            decoded_op_name = 'nft_transfer', 
                            decoded_body = null, ), 
                        out_msgs = [
                            fdtapi.models.message.Message(
                                created_lt = 25713146000001, 
                                ihr_disabled = True, 
                                bounce = True, 
                                bounced = True, 
                                value = 60000000, 
                                fwd_fee = 5681002, 
                                ihr_fee = 5681002, 
                                import_fee = 5681002, 
                                created_at = 5681002, 
                                op_code = '0xdeadbeaf', 
                                raw_body = 'B5EE9C7201010101001100001D00048656C6C6F2C20776F726C64218', 
                                decoded_op_name = 'nft_transfer', 
                                decoded_body = null, )
                            ], 
                        block = '(-1,4234234,8000000000000000)', 
                        prev_trans_hash = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        prev_trans_lt = 25713146000001, 
                        compute_phase = fdtapi.models.compute_phase.ComputePhase(
                            skipped = True, 
                            skip_reason = 'cskip_no_state', 
                            success = True, 
                            gas_fees = 1000, 
                            gas_used = 10000, 
                            vm_steps = 5, 
                            exit_code = 0, ), 
                        storage_phase = fdtapi.models.storage_phase.StoragePhase(
                            fees_collected = 25713146000001, 
                            fees_due = 25713146000001, 
                            status_change = 'acst_unchanged', ), 
                        credit_phase = fdtapi.models.credit_phase.CreditPhase(
                            fees_collected = 100, 
                            credit = 1000, ), 
                        action_phase = fdtapi.models.action_phase.ActionPhase(
                            success = True, 
                            total_actions = 5, 
                            skipped_actions = 5, 
                            fwd_fees = 1000, 
                            total_fees = 1000, ), 
                        bounce_phase = 'cskip_no_state', 
                        aborted = True, 
                        destroyed = True, )
                    ]
            )
        else :
            return Transactions(
                transactions = [
                    fdtapi.models.transaction.Transaction(
                        hash = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        lt = 25713146000001, 
                        account = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        success = True, 
                        utime = 1645544908, 
                        orig_status = 'active', 
                        end_status = 'active', 
                        total_fees = 25713146000001, 
                        transaction_type = 'TransOrd', 
                        state_update_old = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        state_update_new = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        in_msg = fdtapi.models.message.Message(
                            created_lt = 25713146000001, 
                            ihr_disabled = True, 
                            bounce = True, 
                            bounced = True, 
                            value = 60000000, 
                            fwd_fee = 5681002, 
                            ihr_fee = 5681002, 
                            destination = fdtapi.models.account_address.AccountAddress(
                                address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                name = 'Ton foundation', 
                                is_scam = True, 
                                icon = 'https://ton.org/logo.png', ), 
                            source = , 
                            import_fee = 5681002, 
                            created_at = 5681002, 
                            op_code = '0xdeadbeaf', 
                            init = fdtapi.models.state_init.StateInit(
                                boc = 'te6ccgEBBgEARAABFP8A9KQT9LzyyAsBAgEgAgMCAUgEBQAE8jAAONBsIdMfMO1E0NM/MAHAAZekyMs/ye1UkzDyBuIAEaE0MdqJoaZ+YQ==', ), 
                            raw_body = 'B5EE9C7201010101001100001D00048656C6C6F2C20776F726C64218', 
                            decoded_op_name = 'nft_transfer', 
                            decoded_body = null, ), 
                        out_msgs = [
                            fdtapi.models.message.Message(
                                created_lt = 25713146000001, 
                                ihr_disabled = True, 
                                bounce = True, 
                                bounced = True, 
                                value = 60000000, 
                                fwd_fee = 5681002, 
                                ihr_fee = 5681002, 
                                import_fee = 5681002, 
                                created_at = 5681002, 
                                op_code = '0xdeadbeaf', 
                                raw_body = 'B5EE9C7201010101001100001D00048656C6C6F2C20776F726C64218', 
                                decoded_op_name = 'nft_transfer', 
                                decoded_body = null, )
                            ], 
                        block = '(-1,4234234,8000000000000000)', 
                        prev_trans_hash = '55e8809519cd3c49098c9ee45afdafcea7a894a74d0f628d94a115a50e045122', 
                        prev_trans_lt = 25713146000001, 
                        compute_phase = fdtapi.models.compute_phase.ComputePhase(
                            skipped = True, 
                            skip_reason = 'cskip_no_state', 
                            success = True, 
                            gas_fees = 1000, 
                            gas_used = 10000, 
                            vm_steps = 5, 
                            exit_code = 0, ), 
                        storage_phase = fdtapi.models.storage_phase.StoragePhase(
                            fees_collected = 25713146000001, 
                            fees_due = 25713146000001, 
                            status_change = 'acst_unchanged', ), 
                        credit_phase = fdtapi.models.credit_phase.CreditPhase(
                            fees_collected = 100, 
                            credit = 1000, ), 
                        action_phase = fdtapi.models.action_phase.ActionPhase(
                            success = True, 
                            total_actions = 5, 
                            skipped_actions = 5, 
                            fwd_fees = 1000, 
                            total_fees = 1000, ), 
                        bounce_phase = 'cskip_no_state', 
                        aborted = True, 
                        destroyed = True, )
                    ],
        )
        """

    def testTransactions(self):
        """Test Transactions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
