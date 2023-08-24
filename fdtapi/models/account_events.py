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
from pydantic import BaseModel, Field, StrictInt, conlist
from fdtapi.models.account_event import AccountEvent

class AccountEvents(BaseModel):
    """
    AccountEvents
    """
    events: conlist(AccountEvent) = Field(...)
    next_from: StrictInt = Field(...)
    __properties = ["events", "next_from"]

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
    def from_json(cls, json_str: str) -> AccountEvents:
        """Create an instance of AccountEvents from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountEvents:
        """Create an instance of AccountEvents from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountEvents.parse_obj(obj)

        _obj = AccountEvents.parse_obj({
            "events": [AccountEvent.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "next_from": obj.get("next_from")
        })
        return _obj

