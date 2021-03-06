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


class PowerActionInfo(object):
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
        'hostname': 'str',
        'result': 'PowerActionResult',
        'error': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'result': 'result',
        'error': 'error'
    }

    def __init__(self, hostname=None, result=None, error=None, _configuration=None):  # noqa: E501
        """PowerActionInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hostname = None
        self._result = None
        self._error = None
        self.discriminator = None

        self.hostname = hostname
        self.result = result
        self.error = error

    @property
    def hostname(self):
        """Gets the hostname of this PowerActionInfo.  # noqa: E501


        :return: The hostname of this PowerActionInfo.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PowerActionInfo.


        :param hostname: The hostname of this PowerActionInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def result(self):
        """Gets the result of this PowerActionInfo.  # noqa: E501


        :return: The result of this PowerActionInfo.  # noqa: E501
        :rtype: PowerActionResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PowerActionInfo.


        :param result: The result of this PowerActionInfo.  # noqa: E501
        :type: PowerActionResult
        """
        if self._configuration.client_side_validation and result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def error(self):
        """Gets the error of this PowerActionInfo.  # noqa: E501


        :return: The error of this PowerActionInfo.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PowerActionInfo.


        :param error: The error of this PowerActionInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

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
        if issubclass(PowerActionInfo, dict):
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
        if not isinstance(other, PowerActionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerActionInfo):
            return True

        return self.to_dict() != other.to_dict()
