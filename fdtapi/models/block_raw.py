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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class BlockRaw(BaseModel):
    """
    BlockRaw
    """
    workchain: StrictInt = Field(...)
    shard: StrictInt = Field(...)
    seqno: StrictInt = Field(...)
    root_hash: StrictStr = Field(...)
    file_hash: StrictStr = Field(...)
    __properties = ["workchain", "shard", "seqno", "root_hash", "file_hash"]

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
    def from_json(cls, json_str: str) -> BlockRaw:
        """Create an instance of BlockRaw from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlockRaw:
        """Create an instance of BlockRaw from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlockRaw.parse_obj(obj)

        _obj = BlockRaw.parse_obj({
            "workchain": obj.get("workchain"),
            "shard": obj.get("shard"),
            "seqno": obj.get("seqno"),
            "root_hash": obj.get("root_hash"),
            "file_hash": obj.get("file_hash")
        })
        return _obj

