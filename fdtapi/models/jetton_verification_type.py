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





class JettonVerificationType(str, Enum):
    """
    JettonVerificationType
    """

    """
    allowed enum values
    """
    WHITELIST = 'whitelist'
    BLACKLIST = 'blacklist'
    NONE = 'none'

    @classmethod
    def from_json(cls, json_str: str) -> JettonVerificationType:
        """Create an instance of JettonVerificationType from a JSON string"""
        return JettonVerificationType(json.loads(json_str))

