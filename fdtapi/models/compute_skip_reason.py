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





class ComputeSkipReason(str, Enum):
    """
    ComputeSkipReason
    """

    """
    allowed enum values
    """
    CSKIP_NO_STATE = 'cskip_no_state'
    CSKIP_BAD_STATE = 'cskip_bad_state'
    CSKIP_NO_GAS = 'cskip_no_gas'

    @classmethod
    def from_json(cls, json_str: str) -> ComputeSkipReason:
        """Create an instance of ComputeSkipReason from a JSON string"""
        return ComputeSkipReason(json.loads(json_str))


