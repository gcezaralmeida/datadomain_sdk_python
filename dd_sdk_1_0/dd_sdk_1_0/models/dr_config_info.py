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


class DrConfigInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ip_address': 'str',
        'system_mtree_name': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'system_mtree_name': 'system_mtree_name'
    }

    def __init__(self, ip_address=None, system_mtree_name=None, _configuration=None):  # noqa: E501
        """DrConfigInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ip_address = None
        self._system_mtree_name = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if system_mtree_name is not None:
            self.system_mtree_name = system_mtree_name

    @property
    def ip_address(self):
        """Gets the ip_address of this DrConfigInfo.  # noqa: E501

        IP address of DR target host  # noqa: E501

        :return: The ip_address of this DrConfigInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DrConfigInfo.

        IP address of DR target host  # noqa: E501

        :param ip_address: The ip_address of this DrConfigInfo.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def system_mtree_name(self):
        """Gets the system_mtree_name of this DrConfigInfo.  # noqa: E501

        System Mtree name on the DR target host  # noqa: E501

        :return: The system_mtree_name of this DrConfigInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_mtree_name

    @system_mtree_name.setter
    def system_mtree_name(self, system_mtree_name):
        """Sets the system_mtree_name of this DrConfigInfo.

        System Mtree name on the DR target host  # noqa: E501

        :param system_mtree_name: The system_mtree_name of this DrConfigInfo.  # noqa: E501
        :type: str
        """

        self._system_mtree_name = system_mtree_name

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
        if issubclass(DrConfigInfo, dict):
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
        if not isinstance(other, DrConfigInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DrConfigInfo):
            return True

        return self.to_dict() != other.to_dict()
