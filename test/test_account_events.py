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
from fdtapi.models.account_events import AccountEvents  # noqa: E501
from fdtapi.rest import ApiException

class TestAccountEvents(unittest.TestCase):
    """AccountEvents unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountEvents
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountEvents`
        """
        model = fdtapi.models.account_events.AccountEvents()  # noqa: E501
        if include_optional :
            return AccountEvents(
                events = [
                    fdtapi.models.account_event.AccountEvent(
                        event_id = 'e8b0e3fee4a26bd2317ac1f9952fcdc87dc08fdb617656b5202416323337372e', 
                        account = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        timestamp = 1234567890, 
                        actions = [
                            fdtapi.models.action.Action(
                                type = 'TonTransfer', 
                                status = 'ok', 
                                ton_transfer = fdtapi.models.ton_transfer_action.TonTransferAction(
                                    sender = fdtapi.models.account_address.AccountAddress(
                                        address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                        name = 'Ton foundation', 
                                        is_scam = True, 
                                        icon = 'https://ton.org/logo.png', ), 
                                    recipient = , 
                                    amount = 123456789, 
                                    comment = 'Hi! This is your salary. 
From accounting with love.', 
                                    encrypted_comment = fdtapi.models.encrypted_comment.EncryptedComment(
                                        encryption_type = 'simple', 
                                        cipher_text = 'A6A0BD6608672B...CE3AF8DB', ), 
                                    refund = fdtapi.models.refund.Refund(
                                        type = 'DNS.ton', 
                                        origin = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', ), ), 
                                contract_deploy = fdtapi.models.contract_deploy_action.ContractDeployAction(
                                    address = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                                    interfaces = ["nft_item","nft_royalty"], ), 
                                jetton_transfer = fdtapi.models.jetton_transfer_action.JettonTransferAction(
                                    senders_wallet = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                    recipients_wallet = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                    amount = '1000000000', 
                                    comment = 'Hi! This is your salary. 
From accounting with love.', 
                                    jetton = fdtapi.models.jetton_preview.JettonPreview(
                                        address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                                        name = 'Wrapped TON', 
                                        symbol = 'WTON', 
                                        decimals = 9, 
                                        image = 'https://cache.tonapi.io/images/jetton.jpg', 
                                        verification = 'whitelist', ), ), 
                                nft_item_transfer = fdtapi.models.nft_item_transfer_action.NftItemTransferAction(
                                    nft = '', 
                                    comment = 'Hi! This is your salary. 
From accounting with love.', 
                                    payload = '0234de3e21d21b3ee21f3', ), 
                                subscribe = fdtapi.models.subscription_action.SubscriptionAction(
                                    subscriber = , 
                                    subscription = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                                    beneficiary = , 
                                    amount = 1000000000, 
                                    initial = False, ), 
                                un_subscribe = fdtapi.models.un_subscription_action.UnSubscriptionAction(
                                    subscriber = , 
                                    subscription = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                                    beneficiary = , ), 
                                auction_bid = fdtapi.models.auction_bid_action.AuctionBidAction(
                                    auction_type = 'DNS.ton', 
                                    amount = fdtapi.models.price.Price(
                                        value = '123000000000', 
                                        token_name = 'TON', ), 
                                    nft = fdtapi.models.nft_item.NftItem(
                                        address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                        index = 58, 
                                        owner = , 
                                        collection = fdtapi.models.nft_item_collection.NftItem_collection(
                                            address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                            name = 'TON Diamonds', 
                                            description = 'Best collection in TON network', ), 
                                        verified = True, 
                                        metadata = {}, 
                                        sale = fdtapi.models.sale.Sale(
                                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                            market = , 
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
                                            ], ), 
                                    bidder = , 
                                    auction = , ), 
                                nft_purchase = fdtapi.models.nft_purchase_action.NftPurchaseAction(
                                    auction_type = 'DNS.tg', 
                                    amount = , 
                                    nft = fdtapi.models.nft_item.NftItem(
                                        address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                        index = 58, 
                                        verified = True, 
                                        metadata = {}, 
                                        dns = 'crypto.ton', 
                                        approved_by = [
                                            'getgems'
                                            ], ), 
                                    seller = , 
                                    buyer = , ), 
                                deposit_stake = fdtapi.models.deposit_stake_action.DepositStakeAction(
                                    amount = 1660050553, 
                                    staker = , ), 
                                recover_stake = fdtapi.models.recover_stake_action.RecoverStakeAction(
                                    amount = 1660050553, 
                                    staker = , ), 
                                jetton_swap = fdtapi.models.jetton_swap_action.JettonSwapAction(
                                    dex = 'stonfi', 
                                    amount_in = '1660050553', 
                                    amount_out = '1660050553', 
                                    user_wallet = , 
                                    router = , 
                                    jetton_wallet_in = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee', 
                                    jetton_master_in = fdtapi.models.jetton_preview.JettonPreview(
                                        address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                                        name = 'Wrapped TON', 
                                        symbol = 'WTON', 
                                        decimals = 9, 
                                        image = 'https://cache.tonapi.io/images/jetton.jpg', 
                                        verification = 'whitelist', ), 
                                    jetton_wallet_out = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee', 
                                    jetton_master_out = , ), 
                                smart_contract_exec = fdtapi.models.smart_contract_action.SmartContractAction(
                                    executor = , 
                                    contract = , 
                                    ton_attached = 123456789, 
                                    operation = 'NftTransfer or 0x35d95a12', 
                                    payload = '', ), 
                                simple_preview = fdtapi.models.action_simple_preview.ActionSimplePreview(
                                    name = 'Ton Transfer', 
                                    description = 'Transferring 5 Ton', 
                                    action_image = '', 
                                    value = '5 Ton', 
                                    value_image = '', 
                                    accounts = [
                                        
                                        ], ), )
                            ], 
                        is_scam = False, 
                        lt = 25713146000001, 
                        in_progress = False, 
                        extra = 3, )
                    ], 
                next_from = 25713146000001
            )
        else :
            return AccountEvents(
                events = [
                    fdtapi.models.account_event.AccountEvent(
                        event_id = 'e8b0e3fee4a26bd2317ac1f9952fcdc87dc08fdb617656b5202416323337372e', 
                        account = fdtapi.models.account_address.AccountAddress(
                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                            name = 'Ton foundation', 
                            is_scam = True, 
                            icon = 'https://ton.org/logo.png', ), 
                        timestamp = 1234567890, 
                        actions = [
                            fdtapi.models.action.Action(
                                type = 'TonTransfer', 
                                status = 'ok', 
                                ton_transfer = fdtapi.models.ton_transfer_action.TonTransferAction(
                                    sender = fdtapi.models.account_address.AccountAddress(
                                        address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                        name = 'Ton foundation', 
                                        is_scam = True, 
                                        icon = 'https://ton.org/logo.png', ), 
                                    recipient = , 
                                    amount = 123456789, 
                                    comment = 'Hi! This is your salary. 
From accounting with love.', 
                                    encrypted_comment = fdtapi.models.encrypted_comment.EncryptedComment(
                                        encryption_type = 'simple', 
                                        cipher_text = 'A6A0BD6608672B...CE3AF8DB', ), 
                                    refund = fdtapi.models.refund.Refund(
                                        type = 'DNS.ton', 
                                        origin = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', ), ), 
                                contract_deploy = fdtapi.models.contract_deploy_action.ContractDeployAction(
                                    address = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                                    interfaces = ["nft_item","nft_royalty"], ), 
                                jetton_transfer = fdtapi.models.jetton_transfer_action.JettonTransferAction(
                                    senders_wallet = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                    recipients_wallet = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                    amount = '1000000000', 
                                    comment = 'Hi! This is your salary. 
From accounting with love.', 
                                    jetton = fdtapi.models.jetton_preview.JettonPreview(
                                        address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                                        name = 'Wrapped TON', 
                                        symbol = 'WTON', 
                                        decimals = 9, 
                                        image = 'https://cache.tonapi.io/images/jetton.jpg', 
                                        verification = 'whitelist', ), ), 
                                nft_item_transfer = fdtapi.models.nft_item_transfer_action.NftItemTransferAction(
                                    nft = '', 
                                    comment = 'Hi! This is your salary. 
From accounting with love.', 
                                    payload = '0234de3e21d21b3ee21f3', ), 
                                subscribe = fdtapi.models.subscription_action.SubscriptionAction(
                                    subscriber = , 
                                    subscription = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                                    beneficiary = , 
                                    amount = 1000000000, 
                                    initial = False, ), 
                                un_subscribe = fdtapi.models.un_subscription_action.UnSubscriptionAction(
                                    subscriber = , 
                                    subscription = '0:da6b1b6663a0e4d18cc8574ccd9db5296e367dd9324706f3bbd9eb1cd2caf0bf', 
                                    beneficiary = , ), 
                                auction_bid = fdtapi.models.auction_bid_action.AuctionBidAction(
                                    auction_type = 'DNS.ton', 
                                    amount = fdtapi.models.price.Price(
                                        value = '123000000000', 
                                        token_name = 'TON', ), 
                                    nft = fdtapi.models.nft_item.NftItem(
                                        address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                        index = 58, 
                                        owner = , 
                                        collection = fdtapi.models.nft_item_collection.NftItem_collection(
                                            address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                            name = 'TON Diamonds', 
                                            description = 'Best collection in TON network', ), 
                                        verified = True, 
                                        metadata = {}, 
                                        sale = fdtapi.models.sale.Sale(
                                            address = '0:10C1073837B93FDAAD594284CE8B8EFF7B9CF25427440EB2FC682762E1471365', 
                                            market = , 
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
                                            ], ), 
                                    bidder = , 
                                    auction = , ), 
                                nft_purchase = fdtapi.models.nft_purchase_action.NftPurchaseAction(
                                    auction_type = 'DNS.tg', 
                                    amount = , 
                                    nft = fdtapi.models.nft_item.NftItem(
                                        address = '0:E93E7D444180608B8520C00DC664383A387356FB6E16FDDF99DBE5E1415A574B', 
                                        index = 58, 
                                        verified = True, 
                                        metadata = {}, 
                                        dns = 'crypto.ton', 
                                        approved_by = [
                                            'getgems'
                                            ], ), 
                                    seller = , 
                                    buyer = , ), 
                                deposit_stake = fdtapi.models.deposit_stake_action.DepositStakeAction(
                                    amount = 1660050553, 
                                    staker = , ), 
                                recover_stake = fdtapi.models.recover_stake_action.RecoverStakeAction(
                                    amount = 1660050553, 
                                    staker = , ), 
                                jetton_swap = fdtapi.models.jetton_swap_action.JettonSwapAction(
                                    dex = 'stonfi', 
                                    amount_in = '1660050553', 
                                    amount_out = '1660050553', 
                                    user_wallet = , 
                                    router = , 
                                    jetton_wallet_in = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee', 
                                    jetton_master_in = fdtapi.models.jetton_preview.JettonPreview(
                                        address = '0:0BB5A9F69043EEBDDA5AD2E946EB953242BD8F603FE795D90698CEEC6BFC60A0', 
                                        name = 'Wrapped TON', 
                                        symbol = 'WTON', 
                                        decimals = 9, 
                                        image = 'https://cache.tonapi.io/images/jetton.jpg', 
                                        verification = 'whitelist', ), 
                                    jetton_wallet_out = '0:dea8f638b789172ce36d10a20318125e52c649aa84893cd77858224fe2b9b0ee', 
                                    jetton_master_out = , ), 
                                smart_contract_exec = fdtapi.models.smart_contract_action.SmartContractAction(
                                    executor = , 
                                    contract = , 
                                    ton_attached = 123456789, 
                                    operation = 'NftTransfer or 0x35d95a12', 
                                    payload = '', ), 
                                simple_preview = fdtapi.models.action_simple_preview.ActionSimplePreview(
                                    name = 'Ton Transfer', 
                                    description = 'Transferring 5 Ton', 
                                    action_image = '', 
                                    value = '5 Ton', 
                                    value_image = '', 
                                    accounts = [
                                        
                                        ], ), )
                            ], 
                        is_scam = False, 
                        lt = 25713146000001, 
                        in_progress = False, 
                        extra = 3, )
                    ],
                next_from = 25713146000001,
        )
        """

    def testAccountEvents(self):
        """Test AccountEvents"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
