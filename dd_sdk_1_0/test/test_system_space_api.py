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
from dd_sdk_1_0.api.system_space_api import SystemSpaceApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestSystemSpaceApi(unittest.TestCase):
    """SystemSpaceApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.system_space_api.SystemSpaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v20_dd_systems_systemid_systems_stats_space_get(self):
        """Test case for rest_v20_dd_systems_systemid_systems_stats_space_get

        Get system space stats.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
