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
from dd_sdk_1_0.api.alerts_notifylists_api import AlertsNotifylistsApi  # noqa: E501
from dd_sdk_1_0.rest import ApiException


class TestAlertsNotifylistsApi(unittest.TestCase):
    """AlertsNotifylistsApi unit test stubs"""

    def setUp(self):
        self.api = dd_sdk_1_0.api.alerts_notifylists_api.AlertsNotifylistsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v10_dd_systems_systemid_alerts_notify_lists_delete(self):
        """Test case for rest_v10_dd_systems_systemid_alerts_notify_lists_delete

        Delete all user-configured alert notification lists  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_alerts_notify_lists_get(self):
        """Test case for rest_v10_dd_systems_systemid_alerts_notify_lists_get

        Show list of alerts notification lists  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete(self):
        """Test case for rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete

        Delete an alert notification list  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_alerts_notify_lists_id_get(self):
        """Test case for rest_v10_dd_systems_systemid_alerts_notify_lists_id_get

        Show details of an alert notification list  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_alerts_notify_lists_id_put(self):
        """Test case for rest_v10_dd_systems_systemid_alerts_notify_lists_id_put

        Modify an alert notification list. Existing information will be replaced by new input  # noqa: E501
        """
        pass

    def test_rest_v10_dd_systems_systemid_alerts_notify_lists_post(self):
        """Test case for rest_v10_dd_systems_systemid_alerts_notify_lists_post

        Create an alert notification list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
