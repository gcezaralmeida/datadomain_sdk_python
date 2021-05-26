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
from dd_sdk_1_0.api.ddboost_api import DdboostApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestDdboostApi(unittest.TestCase):
    """DdboostApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.ddboost_api.DdboostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v10_dd_systems_systemid_protocols_ddboost_get(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_ddboost_get

        Get the DDBoost configuration.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_protocols_ddboost_put(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_ddboost_put

        Modify DDBoost configuration.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()