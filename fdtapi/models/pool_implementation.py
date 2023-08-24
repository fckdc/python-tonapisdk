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



from pydantic import BaseModel, Field, StrictStr

class PoolImplementation(BaseModel):
    """
    PoolImplementation
    """
    name: StrictStr = Field(...)
    description: StrictStr = Field(...)
    url: StrictStr = Field(...)
    __properties = ["name", "description", "url"]

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
    def from_json(cls, json_str: str) -> PoolImplementation:
        """Create an instance of PoolImplementation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PoolImplementation:
        """Create an instance of PoolImplementation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PoolImplementation.parse_obj(obj)

        _obj = PoolImplementation.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "url": obj.get("url")
        })
        return _obj

