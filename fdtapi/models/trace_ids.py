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
from pydantic import BaseModel, Field, conlist
from fdtapi.models.trace_id import TraceID

class TraceIDs(BaseModel):
    """
    TraceIDs
    """
    traces: conlist(TraceID) = Field(...)
    __properties = ["traces"]

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
    def from_json(cls, json_str: str) -> TraceIDs:
        """Create an instance of TraceIDs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in traces (list)
        _items = []
        if self.traces:
            for _item in self.traces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['traces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceIDs:
        """Create an instance of TraceIDs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceIDs.parse_obj(obj)

        _obj = TraceIDs.parse_obj({
            "traces": [TraceID.from_dict(_item) for _item in obj.get("traces")] if obj.get("traces") is not None else None
        })
        return _obj
