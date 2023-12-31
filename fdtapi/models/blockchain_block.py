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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class BlockchainBlock(BaseModel):
    """
    BlockchainBlock
    """
    workchain_id: StrictInt = Field(...)
    shard: StrictStr = Field(...)
    seqno: StrictInt = Field(...)
    root_hash: StrictStr = Field(...)
    file_hash: StrictStr = Field(...)
    global_id: StrictInt = Field(...)
    version: StrictInt = Field(...)
    after_merge: StrictBool = Field(...)
    before_split: StrictBool = Field(...)
    after_split: StrictBool = Field(...)
    want_split: StrictBool = Field(...)
    want_merge: StrictBool = Field(...)
    key_block: StrictBool = Field(...)
    gen_utime: StrictInt = Field(...)
    start_lt: StrictInt = Field(...)
    end_lt: StrictInt = Field(...)
    vert_seqno: StrictInt = Field(...)
    gen_catchain_seqno: StrictInt = Field(...)
    min_ref_mc_seqno: StrictInt = Field(...)
    prev_key_block_seqno: StrictInt = Field(...)
    gen_software_version: Optional[StrictInt] = None
    gen_software_capabilities: Optional[StrictInt] = None
    master_ref: Optional[StrictStr] = None
    prev_refs: conlist(StrictStr) = Field(...)
    in_msg_descr_length: StrictInt = Field(...)
    out_msg_descr_length: StrictInt = Field(...)
    rand_seed: StrictStr = Field(...)
    created_by: StrictStr = Field(...)
    __properties = ["workchain_id", "shard", "seqno", "root_hash", "file_hash", "global_id", "version", "after_merge", "before_split", "after_split", "want_split", "want_merge", "key_block", "gen_utime", "start_lt", "end_lt", "vert_seqno", "gen_catchain_seqno", "min_ref_mc_seqno", "prev_key_block_seqno", "gen_software_version", "gen_software_capabilities", "master_ref", "prev_refs", "in_msg_descr_length", "out_msg_descr_length", "rand_seed", "created_by"]

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
    def from_json(cls, json_str: str) -> BlockchainBlock:
        """Create an instance of BlockchainBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlockchainBlock:
        """Create an instance of BlockchainBlock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlockchainBlock.parse_obj(obj)

        _obj = BlockchainBlock.parse_obj({
            "workchain_id": obj.get("workchain_id"),
            "shard": obj.get("shard"),
            "seqno": obj.get("seqno"),
            "root_hash": obj.get("root_hash"),
            "file_hash": obj.get("file_hash"),
            "global_id": obj.get("global_id"),
            "version": obj.get("version"),
            "after_merge": obj.get("after_merge"),
            "before_split": obj.get("before_split"),
            "after_split": obj.get("after_split"),
            "want_split": obj.get("want_split"),
            "want_merge": obj.get("want_merge"),
            "key_block": obj.get("key_block"),
            "gen_utime": obj.get("gen_utime"),
            "start_lt": obj.get("start_lt"),
            "end_lt": obj.get("end_lt"),
            "vert_seqno": obj.get("vert_seqno"),
            "gen_catchain_seqno": obj.get("gen_catchain_seqno"),
            "min_ref_mc_seqno": obj.get("min_ref_mc_seqno"),
            "prev_key_block_seqno": obj.get("prev_key_block_seqno"),
            "gen_software_version": obj.get("gen_software_version"),
            "gen_software_capabilities": obj.get("gen_software_capabilities"),
            "master_ref": obj.get("master_ref"),
            "prev_refs": obj.get("prev_refs"),
            "in_msg_descr_length": obj.get("in_msg_descr_length"),
            "out_msg_descr_length": obj.get("out_msg_descr_length"),
            "rand_seed": obj.get("rand_seed"),
            "created_by": obj.get("created_by")
        })
        return _obj

