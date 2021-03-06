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


class AzureInfo(object):
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
        'account_name': 'str',
        'primary_key': 'str',
        'secondary_key': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'primary_key': 'primary_key',
        'secondary_key': 'secondary_key'
    }

    def __init__(self, account_name=None, primary_key=None, secondary_key=None, _configuration=None):  # noqa: E501
        """AzureInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._primary_key = None
        self._secondary_key = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if primary_key is not None:
            self.primary_key = primary_key
        if secondary_key is not None:
            self.secondary_key = secondary_key

    @property
    def account_name(self):
        """Gets the account_name of this AzureInfo.  # noqa: E501


        :return: The account_name of this AzureInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AzureInfo.


        :param account_name: The account_name of this AzureInfo.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def primary_key(self):
        """Gets the primary_key of this AzureInfo.  # noqa: E501


        :return: The primary_key of this AzureInfo.  # noqa: E501
        :rtype: str
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this AzureInfo.


        :param primary_key: The primary_key of this AzureInfo.  # noqa: E501
        :type: str
        """

        self._primary_key = primary_key

    @property
    def secondary_key(self):
        """Gets the secondary_key of this AzureInfo.  # noqa: E501


        :return: The secondary_key of this AzureInfo.  # noqa: E501
        :rtype: str
        """
        return self._secondary_key

    @secondary_key.setter
    def secondary_key(self, secondary_key):
        """Sets the secondary_key of this AzureInfo.


        :param secondary_key: The secondary_key of this AzureInfo.  # noqa: E501
        :type: str
        """

        self._secondary_key = secondary_key

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
        if issubclass(AzureInfo, dict):
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
        if not isinstance(other, AzureInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureInfo):
            return True

        return self.to_dict() != other.to_dict()
