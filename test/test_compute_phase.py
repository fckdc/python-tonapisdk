# coding: utf-8

"""
    REST api to TON blockchain explorer

    Provide access to indexed TON blockchain  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@tonkeeper.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import fdtapi
from fdtapi.models.compute_phase import ComputePhase  # noqa: E501
from fdtapi.rest import ApiException

class TestComputePhase(unittest.TestCase):
    """ComputePhase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputePhase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComputePhase`
        """
        model = fdtapi.models.compute_phase.ComputePhase()  # noqa: E501
        if include_optional :
            return ComputePhase(
                skipped = True, 
                skip_reason = 'cskip_no_state', 
                success = True, 
                gas_fees = 1000, 
                gas_used = 10000, 
                vm_steps = 5, 
                exit_code = 0
            )
        else :
            return ComputePhase(
                skipped = True,
        )
        """

    def testComputePhase(self):
        """Test ComputePhase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()