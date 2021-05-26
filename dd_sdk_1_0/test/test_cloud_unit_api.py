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
from dd_sdk_1_0.api.cloud_unit_api import CloudUnitApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestCloudUnitApi(unittest.TestCase):
    """CloudUnitApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.cloud_unit_api.CloudUnitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v10_dd_systems_systemid_cloud_units_get(self):
        """Test case for rest_v10_dd_systems_systemid_cloud_units_get

        Get List of Cloud Units.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_cloud_units_id_delete(self):
        """Test case for rest_v10_dd_systems_systemid_cloud_units_id_delete

        Delete a Cloud Unit.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_cloud_units_id_get(self):
        """Test case for rest_v10_dd_systems_systemid_cloud_units_id_get

        Get Cloud Unit Details.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_cloud_units_post(self):
        """Test case for rest_v10_dd_systems_systemid_cloud_units_post

        Create a Cloud Unit.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()