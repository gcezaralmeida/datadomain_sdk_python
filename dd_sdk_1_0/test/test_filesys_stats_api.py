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
from dd_sdk_1_0.api.filesys_stats_api import FilesysStatsApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestFilesysStatsApi(unittest.TestCase):
    """FilesysStatsApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.filesys_stats_api.FilesysStatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v10_dd_systems_systemid_stats_file_systems_get(self):
        """Test case for rest_v10_dd_systems_systemid_stats_file_systems_get

        File System show stats.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
