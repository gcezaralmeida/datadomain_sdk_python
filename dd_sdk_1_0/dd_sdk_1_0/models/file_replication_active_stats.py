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


class FileReplicationActiveStats(object):
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
        'outbound': 'FileReplicationActiveStatsDetails',
        'inbound': 'FileReplicationActiveStatsDetails'
    }

    attribute_map = {
        'outbound': 'outbound',
        'inbound': 'inbound'
    }

    def __init__(self, outbound=None, inbound=None, _configuration=None):  # noqa: E501
        """FileReplicationActiveStats - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._outbound = None
        self._inbound = None
        self.discriminator = None

        self.outbound = outbound
        self.inbound = inbound

    @property
    def outbound(self):
        """Gets the outbound of this FileReplicationActiveStats.  # noqa: E501


        :return: The outbound of this FileReplicationActiveStats.  # noqa: E501
        :rtype: FileReplicationActiveStatsDetails
        """
        return self._outbound

    @outbound.setter
    def outbound(self, outbound):
        """Sets the outbound of this FileReplicationActiveStats.


        :param outbound: The outbound of this FileReplicationActiveStats.  # noqa: E501
        :type: FileReplicationActiveStatsDetails
        """
        if self._configuration.client_side_validation and outbound is None:
            raise ValueError("Invalid value for `outbound`, must not be `None`")  # noqa: E501

        self._outbound = outbound

    @property
    def inbound(self):
        """Gets the inbound of this FileReplicationActiveStats.  # noqa: E501


        :return: The inbound of this FileReplicationActiveStats.  # noqa: E501
        :rtype: FileReplicationActiveStatsDetails
        """
        return self._inbound

    @inbound.setter
    def inbound(self, inbound):
        """Sets the inbound of this FileReplicationActiveStats.


        :param inbound: The inbound of this FileReplicationActiveStats.  # noqa: E501
        :type: FileReplicationActiveStatsDetails
        """
        if self._configuration.client_side_validation and inbound is None:
            raise ValueError("Invalid value for `inbound`, must not be `None`")  # noqa: E501

        self._inbound = inbound

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
        if issubclass(FileReplicationActiveStats, dict):
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
        if not isinstance(other, FileReplicationActiveStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileReplicationActiveStats):
            return True

        return self.to_dict() != other.to_dict()