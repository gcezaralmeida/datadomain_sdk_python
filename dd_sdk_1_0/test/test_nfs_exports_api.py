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
from dd_sdk_1_0.api.nfs_exports_api import NfsExportsApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestNfsExportsApi(unittest.TestCase):
    """NfsExportsApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.nfs_exports_api.NfsExportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v10_dd_systems_systemid_protocols_nfs_exports_get(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_nfs_exports_get

        Get NFS export list.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete

        Delete an NFS export.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get

        Get an NFS export.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put

        Modify an NFS export.  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_protocols_nfs_exports_post(self):
        """Test case for rest_v10_dd_systems_systemid_protocols_nfs_exports_post

        Create NFS export.  # noqa: E501
        """
        pass

    def test_rest_v20_dd_systems_systemid_protocols_nfs_exports_delete(self):
        """Test case for rest_v20_dd_systems_systemid_protocols_nfs_exports_delete

        Destroy NFS export[s].  # noqa: E501
        """
        pass

    def test_rest_v20_dd_systems_systemid_protocols_nfs_exports_get(self):
        """Test case for rest_v20_dd_systems_systemid_protocols_nfs_exports_get

        Get NFS export list.  # noqa: E501
        """
        pass

    def test_rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete(self):
        """Test case for rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete

        Destroy an NFS export  # noqa: E501
        """
        pass

    def test_rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get(self):
        """Test case for rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get

        Get details of an NFS export.  # noqa: E501
        """
        pass

    def test_rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put(self):
        """Test case for rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put

        Modify an NFS export  # noqa: E501
        """
        pass

    def test_rest_v20_dd_systems_systemid_protocols_nfs_exports_post(self):
        """Test case for rest_v20_dd_systems_systemid_protocols_nfs_exports_post

        Create an NFS export.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()