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


class SpaceDetailedInfo(object):
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
        'system_tier_maximum_supported_capacity': 'list[MaxSupportedCapacity]',
        'system_tier_space_info': 'list[TierInfo]',
        'node_space_info': 'list[NodeSpaceInfo]'
    }

    attribute_map = {
        'system_tier_maximum_supported_capacity': 'system_tier_maximum_supported_capacity',
        'system_tier_space_info': 'system_tier_space_info',
        'node_space_info': 'node_space_info'
    }

    def __init__(self, system_tier_maximum_supported_capacity=None, system_tier_space_info=None, node_space_info=None, _configuration=None):  # noqa: E501
        """SpaceDetailedInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._system_tier_maximum_supported_capacity = None
        self._system_tier_space_info = None
        self._node_space_info = None
        self.discriminator = None

        if system_tier_maximum_supported_capacity is not None:
            self.system_tier_maximum_supported_capacity = system_tier_maximum_supported_capacity
        self.system_tier_space_info = system_tier_space_info
        if node_space_info is not None:
            self.node_space_info = node_space_info

    @property
    def system_tier_maximum_supported_capacity(self):
        """Gets the system_tier_maximum_supported_capacity of this SpaceDetailedInfo.  # noqa: E501


        :return: The system_tier_maximum_supported_capacity of this SpaceDetailedInfo.  # noqa: E501
        :rtype: list[MaxSupportedCapacity]
        """
        return self._system_tier_maximum_supported_capacity

    @system_tier_maximum_supported_capacity.setter
    def system_tier_maximum_supported_capacity(self, system_tier_maximum_supported_capacity):
        """Sets the system_tier_maximum_supported_capacity of this SpaceDetailedInfo.


        :param system_tier_maximum_supported_capacity: The system_tier_maximum_supported_capacity of this SpaceDetailedInfo.  # noqa: E501
        :type: list[MaxSupportedCapacity]
        """

        self._system_tier_maximum_supported_capacity = system_tier_maximum_supported_capacity

    @property
    def system_tier_space_info(self):
        """Gets the system_tier_space_info of this SpaceDetailedInfo.  # noqa: E501


        :return: The system_tier_space_info of this SpaceDetailedInfo.  # noqa: E501
        :rtype: list[TierInfo]
        """
        return self._system_tier_space_info

    @system_tier_space_info.setter
    def system_tier_space_info(self, system_tier_space_info):
        """Sets the system_tier_space_info of this SpaceDetailedInfo.


        :param system_tier_space_info: The system_tier_space_info of this SpaceDetailedInfo.  # noqa: E501
        :type: list[TierInfo]
        """
        if self._configuration.client_side_validation and system_tier_space_info is None:
            raise ValueError("Invalid value for `system_tier_space_info`, must not be `None`")  # noqa: E501

        self._system_tier_space_info = system_tier_space_info

    @property
    def node_space_info(self):
        """Gets the node_space_info of this SpaceDetailedInfo.  # noqa: E501


        :return: The node_space_info of this SpaceDetailedInfo.  # noqa: E501
        :rtype: list[NodeSpaceInfo]
        """
        return self._node_space_info

    @node_space_info.setter
    def node_space_info(self, node_space_info):
        """Sets the node_space_info of this SpaceDetailedInfo.


        :param node_space_info: The node_space_info of this SpaceDetailedInfo.  # noqa: E501
        :type: list[NodeSpaceInfo]
        """

        self._node_space_info = node_space_info

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
        if issubclass(SpaceDetailedInfo, dict):
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
        if not isinstance(other, SpaceDetailedInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpaceDetailedInfo):
            return True

        return self.to_dict() != other.to_dict()
