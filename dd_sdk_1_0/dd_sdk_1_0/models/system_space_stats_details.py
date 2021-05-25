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


class SystemSpaceStatsDetails(object):
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
        'in_bytes': 'int',
        'out_bytes': 'int'
    }

    attribute_map = {
        'in_bytes': 'in_bytes',
        'out_bytes': 'out_bytes'
    }

    def __init__(self, in_bytes=None, out_bytes=None, _configuration=None):  # noqa: E501
        """SystemSpaceStatsDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._in_bytes = None
        self._out_bytes = None
        self.discriminator = None

        if in_bytes is not None:
            self.in_bytes = in_bytes
        if out_bytes is not None:
            self.out_bytes = out_bytes

    @property
    def in_bytes(self):
        """Gets the in_bytes of this SystemSpaceStatsDetails.  # noqa: E501


        :return: The in_bytes of this SystemSpaceStatsDetails.  # noqa: E501
        :rtype: int
        """
        return self._in_bytes

    @in_bytes.setter
    def in_bytes(self, in_bytes):
        """Sets the in_bytes of this SystemSpaceStatsDetails.


        :param in_bytes: The in_bytes of this SystemSpaceStatsDetails.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                in_bytes is not None and in_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `in_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._in_bytes = in_bytes

    @property
    def out_bytes(self):
        """Gets the out_bytes of this SystemSpaceStatsDetails.  # noqa: E501


        :return: The out_bytes of this SystemSpaceStatsDetails.  # noqa: E501
        :rtype: int
        """
        return self._out_bytes

    @out_bytes.setter
    def out_bytes(self, out_bytes):
        """Sets the out_bytes of this SystemSpaceStatsDetails.


        :param out_bytes: The out_bytes of this SystemSpaceStatsDetails.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                out_bytes is not None and out_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `out_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._out_bytes = out_bytes

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
        if issubclass(SystemSpaceStatsDetails, dict):
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
        if not isinstance(other, SystemSpaceStatsDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemSpaceStatsDetails):
            return True

        return self.to_dict() != other.to_dict()
