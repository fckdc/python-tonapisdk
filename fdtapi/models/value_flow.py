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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from fdtapi.models.account_address import AccountAddress
from fdtapi.models.value_flow_jettons_inner import ValueFlowJettonsInner

class ValueFlow(BaseModel):
    """
    ValueFlow
    """
    account: AccountAddress = Field(...)
    ton: StrictInt = Field(...)
    fees: StrictInt = Field(...)
    jettons: Optional[conlist(ValueFlowJettonsInner)] = None
    __properties = ["account", "ton", "fees", "jettons"]

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
    def from_json(cls, json_str: str) -> ValueFlow:
        """Create an instance of ValueFlow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in jettons (list)
        _items = []
        if self.jettons:
            for _item in self.jettons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jettons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValueFlow:
        """Create an instance of ValueFlow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValueFlow.parse_obj(obj)

        _obj = ValueFlow.parse_obj({
            "account": AccountAddress.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "ton": obj.get("ton"),
            "fees": obj.get("fees"),
            "jettons": [ValueFlowJettonsInner.from_dict(_item) for _item in obj.get("jettons")] if obj.get("jettons") is not None else None
        })
        return _obj

