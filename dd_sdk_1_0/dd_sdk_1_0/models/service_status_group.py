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


class ServiceStatusGroup(object):
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
        'status_group': 'ServiceStatus',
        'status_list': 'ServiceStatusList'
    }

    attribute_map = {
        'status_group': 'status_group',
        'status_list': 'status_list'
    }

    def __init__(self, status_group=None, status_list=None, _configuration=None):  # noqa: E501
        """ServiceStatusGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status_group = None
        self._status_list = None
        self.discriminator = None

        self.status_group = status_group
        if status_list is not None:
            self.status_list = status_list

    @property
    def status_group(self):
        """Gets the status_group of this ServiceStatusGroup.  # noqa: E501

        Overall status of a bulk request.  # noqa: E501

        :return: The status_group of this ServiceStatusGroup.  # noqa: E501
        :rtype: ServiceStatus
        """
        return self._status_group

    @status_group.setter
    def status_group(self, status_group):
        """Sets the status_group of this ServiceStatusGroup.

        Overall status of a bulk request.  # noqa: E501

        :param status_group: The status_group of this ServiceStatusGroup.  # noqa: E501
        :type: ServiceStatus
        """
        if self._configuration.client_side_validation and status_group is None:
            raise ValueError("Invalid value for `status_group`, must not be `None`")  # noqa: E501

        self._status_group = status_group

    @property
    def status_list(self):
        """Gets the status_list of this ServiceStatusGroup.  # noqa: E501

        Ordered list of status for a bulk request.  # noqa: E501

        :return: The status_list of this ServiceStatusGroup.  # noqa: E501
        :rtype: ServiceStatusList
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this ServiceStatusGroup.

        Ordered list of status for a bulk request.  # noqa: E501

        :param status_list: The status_list of this ServiceStatusGroup.  # noqa: E501
        :type: ServiceStatusList
        """

        self._status_list = status_list

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
        if issubclass(ServiceStatusGroup, dict):
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
        if not isinstance(other, ServiceStatusGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceStatusGroup):
            return True

        return self.to_dict() != other.to_dict()