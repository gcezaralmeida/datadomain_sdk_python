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


class ClusterInfo(object):
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
        'initial_capability': 'ClusterCapability',
        'maximum_capability': 'ClusterCapability'
    }

    attribute_map = {
        'initial_capability': 'initial_capability',
        'maximum_capability': 'maximum_capability'
    }

    def __init__(self, initial_capability=None, maximum_capability=None, _configuration=None):  # noqa: E501
        """ClusterInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._initial_capability = None
        self._maximum_capability = None
        self.discriminator = None

        if initial_capability is not None:
            self.initial_capability = initial_capability
        if maximum_capability is not None:
            self.maximum_capability = maximum_capability

    @property
    def initial_capability(self):
        """Gets the initial_capability of this ClusterInfo.  # noqa: E501


        :return: The initial_capability of this ClusterInfo.  # noqa: E501
        :rtype: ClusterCapability
        """
        return self._initial_capability

    @initial_capability.setter
    def initial_capability(self, initial_capability):
        """Sets the initial_capability of this ClusterInfo.


        :param initial_capability: The initial_capability of this ClusterInfo.  # noqa: E501
        :type: ClusterCapability
        """

        self._initial_capability = initial_capability

    @property
    def maximum_capability(self):
        """Gets the maximum_capability of this ClusterInfo.  # noqa: E501


        :return: The maximum_capability of this ClusterInfo.  # noqa: E501
        :rtype: ClusterCapability
        """
        return self._maximum_capability

    @maximum_capability.setter
    def maximum_capability(self, maximum_capability):
        """Sets the maximum_capability of this ClusterInfo.


        :param maximum_capability: The maximum_capability of this ClusterInfo.  # noqa: E501
        :type: ClusterCapability
        """

        self._maximum_capability = maximum_capability

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
        if issubclass(ClusterInfo, dict):
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
        if not isinstance(other, ClusterInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterInfo):
            return True

        return self.to_dict() != other.to_dict()
