# coding: utf-8

"""
    REST api to TON blockchain explorer

    Provide access to indexed TON blockchain  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@tonkeeper.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AccStatusChange(str, Enum):
    """
    AccStatusChange
    """

    """
    allowed enum values
    """
    ACST_UNCHANGED = 'acst_unchanged'
    ACST_FROZEN = 'acst_frozen'
    ACST_DELETED = 'acst_deleted'

    @classmethod
    def from_json(cls, json_str: str) -> AccStatusChange:
        """Create an instance of AccStatusChange from a JSON string"""
        return AccStatusChange(json.loads(json_str))


