# coding: utf-8

"""
    DataDomain Rest API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dd_sdk_1_0
from dd_sdk_1_0.api.comp_measurements_support_check_api import CompMeasurementsSupportCheckApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestCompMeasurementsSupportCheckApi(unittest.TestCase):
    """CompMeasurementsSupportCheckApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.comp_measurements_support_check_api.CompMeasurementsSupportCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v10_dd_systems_systemid_stats_compression_measurements_support_check_get(self):
        """Test case for rest_v10_dd_systems_systemid_stats_compression_measurements_support_check_get

        Get information about measurements support on this system.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
