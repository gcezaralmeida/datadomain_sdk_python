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


class ServerInfo(object):
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
        'tier_type': 'str',
        'physical_capacity': 'Capacity',
        'logical_capacity': 'Capacity',
        'compression_factor': 'float',
        'subscribed_capacity': 'int'
    }

    attribute_map = {
        'tier_type': 'tier_type',
        'physical_capacity': 'physical_capacity',
        'logical_capacity': 'logical_capacity',
        'compression_factor': 'compression_factor',
        'subscribed_capacity': 'subscribed_capacity'
    }

    def __init__(self, tier_type=None, physical_capacity=None, logical_capacity=None, compression_factor=None, subscribed_capacity=None, _configuration=None):  # noqa: E501
        """ServerInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tier_type = None
        self._physical_capacity = None
        self._logical_capacity = None
        self._compression_factor = None
        self._subscribed_capacity = None
        self.discriminator = None

        if tier_type is not None:
            self.tier_type = tier_type
        if physical_capacity is not None:
            self.physical_capacity = physical_capacity
        if logical_capacity is not None:
            self.logical_capacity = logical_capacity
        if compression_factor is not None:
            self.compression_factor = compression_factor
        if subscribed_capacity is not None:
            self.subscribed_capacity = subscribed_capacity

    @property
    def tier_type(self):
        """Gets the tier_type of this ServerInfo.  # noqa: E501


        :return: The tier_type of this ServerInfo.  # noqa: E501
        :rtype: str
        """
        return self._tier_type

    @tier_type.setter
    def tier_type(self, tier_type):
        """Sets the tier_type of this ServerInfo.


        :param tier_type: The tier_type of this ServerInfo.  # noqa: E501
        :type: str
        """

        self._tier_type = tier_type

    @property
    def physical_capacity(self):
        """Gets the physical_capacity of this ServerInfo.  # noqa: E501


        :return: The physical_capacity of this ServerInfo.  # noqa: E501
        :rtype: Capacity
        """
        return self._physical_capacity

    @physical_capacity.setter
    def physical_capacity(self, physical_capacity):
        """Sets the physical_capacity of this ServerInfo.


        :param physical_capacity: The physical_capacity of this ServerInfo.  # noqa: E501
        :type: Capacity
        """

        self._physical_capacity = physical_capacity

    @property
    def logical_capacity(self):
        """Gets the logical_capacity of this ServerInfo.  # noqa: E501


        :return: The logical_capacity of this ServerInfo.  # noqa: E501
        :rtype: Capacity
        """
        return self._logical_capacity

    @logical_capacity.setter
    def logical_capacity(self, logical_capacity):
        """Sets the logical_capacity of this ServerInfo.


        :param logical_capacity: The logical_capacity of this ServerInfo.  # noqa: E501
        :type: Capacity
        """

        self._logical_capacity = logical_capacity

    @property
    def compression_factor(self):
        """Gets the compression_factor of this ServerInfo.  # noqa: E501


        :return: The compression_factor of this ServerInfo.  # noqa: E501
        :rtype: float
        """
        return self._compression_factor

    @compression_factor.setter
    def compression_factor(self, compression_factor):
        """Sets the compression_factor of this ServerInfo.


        :param compression_factor: The compression_factor of this ServerInfo.  # noqa: E501
        :type: float
        """

        self._compression_factor = compression_factor

    @property
    def subscribed_capacity(self):
        """Gets the subscribed_capacity of this ServerInfo.  # noqa: E501


        :return: The subscribed_capacity of this ServerInfo.  # noqa: E501
        :rtype: int
        """
        return self._subscribed_capacity

    @subscribed_capacity.setter
    def subscribed_capacity(self, subscribed_capacity):
        """Sets the subscribed_capacity of this ServerInfo.


        :param subscribed_capacity: The subscribed_capacity of this ServerInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                subscribed_capacity is not None and subscribed_capacity < 0):  # noqa: E501
            raise ValueError("Invalid value for `subscribed_capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._subscribed_capacity = subscribed_capacity

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
        if issubclass(ServerInfo, dict):
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
        if not isinstance(other, ServerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerInfo):
            return True

        return self.to_dict() != other.to_dict()
