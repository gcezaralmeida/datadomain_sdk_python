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


class EncryptionKeysIdModify(object):
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
        'operations': 'KeysIdOperations',
        'tier': 'Tier',
        'unit_name': 'str'
    }

    attribute_map = {
        'operations': 'operations',
        'tier': 'tier',
        'unit_name': 'unit_name'
    }

    def __init__(self, operations=None, tier=None, unit_name=None, _configuration=None):  # noqa: E501
        """EncryptionKeysIdModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operations = None
        self._tier = None
        self._unit_name = None
        self.discriminator = None

        self.operations = operations
        if tier is not None:
            self.tier = tier
        if unit_name is not None:
            self.unit_name = unit_name

    @property
    def operations(self):
        """Gets the operations of this EncryptionKeysIdModify.  # noqa: E501


        :return: The operations of this EncryptionKeysIdModify.  # noqa: E501
        :rtype: KeysIdOperations
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this EncryptionKeysIdModify.


        :param operations: The operations of this EncryptionKeysIdModify.  # noqa: E501
        :type: KeysIdOperations
        """
        if self._configuration.client_side_validation and operations is None:
            raise ValueError("Invalid value for `operations`, must not be `None`")  # noqa: E501

        self._operations = operations

    @property
    def tier(self):
        """Gets the tier of this EncryptionKeysIdModify.  # noqa: E501


        :return: The tier of this EncryptionKeysIdModify.  # noqa: E501
        :rtype: Tier
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this EncryptionKeysIdModify.


        :param tier: The tier of this EncryptionKeysIdModify.  # noqa: E501
        :type: Tier
        """

        self._tier = tier

    @property
    def unit_name(self):
        """Gets the unit_name of this EncryptionKeysIdModify.  # noqa: E501


        :return: The unit_name of this EncryptionKeysIdModify.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this EncryptionKeysIdModify.


        :param unit_name: The unit_name of this EncryptionKeysIdModify.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

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
        if issubclass(EncryptionKeysIdModify, dict):
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
        if not isinstance(other, EncryptionKeysIdModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncryptionKeysIdModify):
            return True

        return self.to_dict() != other.to_dict()
