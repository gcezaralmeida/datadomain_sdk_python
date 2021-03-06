# coding: utf-8

"""
    DataDomain Rest API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dd_sdk_1_0.configuration import Configuration


class SettingsModifyOps(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SET_ADMIN_INFO = "set_admin_info"
    SET_ADMIN_EMAIL = "set_admin_email"
    SET_ADMIN_HOST = "set_admin_host"
    SET_LOCATION = "set_location"
    SET_TIMEZONE = "set_timezone"
    SET_MAIL_SERVER = "set_mail_server"
    SET_ALL = "set_all"
    RESET_ADMIN_INFO = "reset_admin_info"
    RESET_ADMIN_EMAIL = "reset_admin_email"
    RESET_ADMIN_HOST = "reset_admin_host"
    RESET_LOCATION = "reset_location"
    RESET_TIMEZONE = "reset_timezone"
    RESET_MAIL_SERVER = "reset_mail_server"
    RESET_ALL = "reset_all"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, _configuration=None):  # noqa: E501
        """SettingsModifyOps - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SettingsModifyOps, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingsModifyOps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsModifyOps):
            return True

        return self.to_dict() != other.to_dict()
