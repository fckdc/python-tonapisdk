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


from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictInt, conlist
from fdtapi.models.jetton_quantity import JettonQuantity
from fdtapi.models.nft_item import NftItem

class Risk(BaseModel):
    """
    Risk specifies assets that could be lost if a message would be sent to a malicious smart contract. It makes sense to understand the risk BEFORE sending a message to the blockchain.
    """
    transfer_all_remaining_balance: StrictBool = Field(..., description="transfer all the remaining balance of the wallet.")
    ton: StrictInt = Field(...)
    jettons: conlist(JettonQuantity) = Field(...)
    nfts: conlist(NftItem) = Field(...)
    __properties = ["transfer_all_remaining_balance", "ton", "jettons", "nfts"]

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
    def from_json(cls, json_str: str) -> Risk:
        """Create an instance of Risk from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in jettons (list)
        _items = []
        if self.jettons:
            for _item in self.jettons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jettons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nfts (list)
        _items = []
        if self.nfts:
            for _item in self.nfts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nfts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Risk:
        """Create an instance of Risk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Risk.parse_obj(obj)

        _obj = Risk.parse_obj({
            "transfer_all_remaining_balance": obj.get("transfer_all_remaining_balance"),
            "ton": obj.get("ton"),
            "jettons": [JettonQuantity.from_dict(_item) for _item in obj.get("jettons")] if obj.get("jettons") is not None else None,
            "nfts": [NftItem.from_dict(_item) for _item in obj.get("nfts")] if obj.get("nfts") is not None else None
        })
        return _obj

