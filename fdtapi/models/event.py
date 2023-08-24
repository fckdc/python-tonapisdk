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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from fdtapi.models.action import Action
from fdtapi.models.value_flow import ValueFlow

class Event(BaseModel):
    """
    Event
    """
    event_id: StrictStr = Field(...)
    timestamp: StrictInt = Field(...)
    actions: conlist(Action) = Field(...)
    value_flow: conlist(ValueFlow) = Field(...)
    is_scam: StrictBool = Field(..., description="scam")
    lt: StrictInt = Field(...)
    in_progress: StrictBool = Field(..., description="Event is not finished yet. Transactions still happening")
    __properties = ["event_id", "timestamp", "actions", "value_flow", "is_scam", "lt", "in_progress"]

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
    def from_json(cls, json_str: str) -> Event:
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in value_flow (list)
        _items = []
        if self.value_flow:
            for _item in self.value_flow:
                if _item:
                    _items.append(_item.to_dict())
            _dict['value_flow'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Event:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Event.parse_obj(obj)

        _obj = Event.parse_obj({
            "event_id": obj.get("event_id"),
            "timestamp": obj.get("timestamp"),
            "actions": [Action.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "value_flow": [ValueFlow.from_dict(_item) for _item in obj.get("value_flow")] if obj.get("value_flow") is not None else None,
            "is_scam": obj.get("is_scam"),
            "lt": obj.get("lt"),
            "in_progress": obj.get("in_progress")
        })
        return _obj

