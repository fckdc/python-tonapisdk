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
from pydantic import BaseModel, Field, StrictBool, StrictInt
from fdtapi.models.compute_skip_reason import ComputeSkipReason

class ComputePhase(BaseModel):
    """
    ComputePhase
    """
    skipped: StrictBool = Field(...)
    skip_reason: Optional[ComputeSkipReason] = None
    success: Optional[StrictBool] = None
    gas_fees: Optional[StrictInt] = None
    gas_used: Optional[StrictInt] = None
    vm_steps: Optional[StrictInt] = None
    exit_code: Optional[StrictInt] = None
    __properties = ["skipped", "skip_reason", "success", "gas_fees", "gas_used", "vm_steps", "exit_code"]

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
    def from_json(cls, json_str: str) -> ComputePhase:
        """Create an instance of ComputePhase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComputePhase:
        """Create an instance of ComputePhase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComputePhase.parse_obj(obj)

        _obj = ComputePhase.parse_obj({
            "skipped": obj.get("skipped"),
            "skip_reason": obj.get("skip_reason"),
            "success": obj.get("success"),
            "gas_fees": obj.get("gas_fees"),
            "gas_used": obj.get("gas_used"),
            "vm_steps": obj.get("vm_steps"),
            "exit_code": obj.get("exit_code")
        })
        return _obj

