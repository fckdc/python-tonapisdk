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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from fdtapi.models.nft_item import NftItem

class DomainInfo(BaseModel):
    """
    DomainInfo
    """
    name: StrictStr = Field(...)
    expiring_at: Optional[StrictInt] = Field(None, description="date of expiring. optional. not all domain in ton has expiration date")
    item: Optional[NftItem] = None
    __properties = ["name", "expiring_at", "item"]

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
    def from_json(cls, json_str: str) -> DomainInfo:
        """Create an instance of DomainInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DomainInfo:
        """Create an instance of DomainInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DomainInfo.parse_obj(obj)

        _obj = DomainInfo.parse_obj({
            "name": obj.get("name"),
            "expiring_at": obj.get("expiring_at"),
            "item": NftItem.from_dict(obj.get("item")) if obj.get("item") is not None else None
        })
        return _obj

