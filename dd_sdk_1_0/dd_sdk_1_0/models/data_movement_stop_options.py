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


class DataMovementStopOptions(object):
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
        'path': 'str',
        'to_tier': 'DataMovementStopTiers'
    }

    attribute_map = {
        'path': 'path',
        'to_tier': 'to_tier'
    }

    def __init__(self, path=None, to_tier=None, _configuration=None):  # noqa: E501
        """DataMovementStopOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._path = None
        self._to_tier = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if to_tier is not None:
            self.to_tier = to_tier

    @property
    def path(self):
        """Gets the path of this DataMovementStopOptions.  # noqa: E501

        Stop recall of the given file path.  # noqa: E501

        :return: The path of this DataMovementStopOptions.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DataMovementStopOptions.

        Stop recall of the given file path.  # noqa: E501

        :param path: The path of this DataMovementStopOptions.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def to_tier(self):
        """Gets the to_tier of this DataMovementStopOptions.  # noqa: E501

        Which tier to stop Data Movement on.  # noqa: E501

        :return: The to_tier of this DataMovementStopOptions.  # noqa: E501
        :rtype: DataMovementStopTiers
        """
        return self._to_tier

    @to_tier.setter
    def to_tier(self, to_tier):
        """Sets the to_tier of this DataMovementStopOptions.

        Which tier to stop Data Movement on.  # noqa: E501

        :param to_tier: The to_tier of this DataMovementStopOptions.  # noqa: E501
        :type: DataMovementStopTiers
        """

        self._to_tier = to_tier

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
        if issubclass(DataMovementStopOptions, dict):
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
        if not isinstance(other, DataMovementStopOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataMovementStopOptions):
            return True

        return self.to_dict() != other.to_dict()
