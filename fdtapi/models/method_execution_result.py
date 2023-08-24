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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, conlist
from fdtapi.models.tvm_stack_record import TvmStackRecord

class MethodExecutionResult(BaseModel):
    """
    MethodExecutionResult
    """
    success: StrictBool = Field(...)
    exit_code: StrictInt = Field(..., description="tvm exit code")
    stack: conlist(TvmStackRecord) = Field(...)
    decoded: Optional[Any] = None
    __properties = ["success", "exit_code", "stack", "decoded"]

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
    def from_json(cls, json_str: str) -> MethodExecutionResult:
        """Create an instance of MethodExecutionResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in stack (list)
        _items = []
        if self.stack:
            for _item in self.stack:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stack'] = _items
        # set to None if decoded (nullable) is None
        # and __fields_set__ contains the field
        if self.decoded is None and "decoded" in self.__fields_set__:
            _dict['decoded'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MethodExecutionResult:
        """Create an instance of MethodExecutionResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MethodExecutionResult.parse_obj(obj)

        _obj = MethodExecutionResult.parse_obj({
            "success": obj.get("success"),
            "exit_code": obj.get("exit_code"),
            "stack": [TvmStackRecord.from_dict(_item) for _item in obj.get("stack")] if obj.get("stack") is not None else None,
            "decoded": obj.get("decoded")
        })
        return _obj

