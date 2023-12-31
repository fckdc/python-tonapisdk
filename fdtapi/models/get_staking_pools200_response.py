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


from typing import Dict, List
from pydantic import BaseModel, Field, conlist
from fdtapi.models.pool_implementation import PoolImplementation
from fdtapi.models.pool_info import PoolInfo

class GetStakingPools200Response(BaseModel):
    """
    GetStakingPools200Response
    """
    pools: conlist(PoolInfo) = Field(...)
    implementations: Dict[str, PoolImplementation] = Field(...)
    __properties = ["pools", "implementations"]

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
    def from_json(cls, json_str: str) -> GetStakingPools200Response:
        """Create an instance of GetStakingPools200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in pools (list)
        _items = []
        if self.pools:
            for _item in self.pools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pools'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in implementations (dict)
        _field_dict = {}
        if self.implementations:
            for _key in self.implementations:
                if self.implementations[_key]:
                    _field_dict[_key] = self.implementations[_key].to_dict()
            _dict['implementations'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetStakingPools200Response:
        """Create an instance of GetStakingPools200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetStakingPools200Response.parse_obj(obj)

        _obj = GetStakingPools200Response.parse_obj({
            "pools": [PoolInfo.from_dict(_item) for _item in obj.get("pools")] if obj.get("pools") is not None else None,
            "implementations": dict(
                (_k, PoolImplementation.from_dict(_v))
                for _k, _v in obj.get("implementations").items()
            )
            if obj.get("implementations") is not None
            else None
        })
        return _obj

