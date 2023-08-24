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



from pydantic import BaseModel, Field
from fdtapi.models.account_event import AccountEvent
from fdtapi.models.risk import Risk
from fdtapi.models.trace import Trace

class MessageConsequences(BaseModel):
    """
    MessageConsequences
    """
    trace: Trace = Field(...)
    risk: Risk = Field(...)
    event: AccountEvent = Field(...)
    __properties = ["trace", "risk", "event"]

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
    def from_json(cls, json_str: str) -> MessageConsequences:
        """Create an instance of MessageConsequences from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of trace
        if self.trace:
            _dict['trace'] = self.trace.to_dict()
        # override the default output from pydantic by calling `to_dict()` of risk
        if self.risk:
            _dict['risk'] = self.risk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageConsequences:
        """Create an instance of MessageConsequences from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessageConsequences.parse_obj(obj)

        _obj = MessageConsequences.parse_obj({
            "trace": Trace.from_dict(obj.get("trace")) if obj.get("trace") is not None else None,
            "risk": Risk.from_dict(obj.get("risk")) if obj.get("risk") is not None else None,
            "event": AccountEvent.from_dict(obj.get("event")) if obj.get("event") is not None else None
        })
        return _obj
