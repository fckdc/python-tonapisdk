# coding: utf-8

"""
    REST api to TON blockchain explorer

    Provide access to indexed TON blockchain  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@tonkeeper.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from fdtapi.models.account_address import AccountAddress
from fdtapi.models.nft_item import NftItem
from fdtapi.models.price import Price

class AuctionBidAction(BaseModel):
    """
    AuctionBidAction
    """
    auction_type: StrictStr = Field(...)
    amount: Price = Field(...)
    nft: Optional[NftItem] = None
    bidder: AccountAddress = Field(...)
    auction: AccountAddress = Field(...)
    __properties = ["auction_type", "amount", "nft", "bidder", "auction"]

    @validator('auction_type')
    def auction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DNS.ton', 'DNS.tg', 'NUMBER.tg', 'getgems'):
            raise ValueError("must be one of enum values ('DNS.ton', 'DNS.tg', 'NUMBER.tg', 'getgems')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuctionBidAction:
        """Create an instance of AuctionBidAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nft
        if self.nft:
            _dict['nft'] = self.nft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bidder
        if self.bidder:
            _dict['bidder'] = self.bidder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auction
        if self.auction:
            _dict['auction'] = self.auction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuctionBidAction:
        """Create an instance of AuctionBidAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuctionBidAction.parse_obj(obj)

        _obj = AuctionBidAction.parse_obj({
            "auction_type": obj.get("auction_type"),
            "amount": Price.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "nft": NftItem.from_dict(obj.get("nft")) if obj.get("nft") is not None else None,
            "bidder": AccountAddress.from_dict(obj.get("bidder")) if obj.get("bidder") is not None else None,
            "auction": AccountAddress.from_dict(obj.get("auction")) if obj.get("auction") is not None else None
        })
        return _obj

