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


class EncryptionKeysModify(object):
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
        'operations': 'KeysOperations',
        'modify_info': 'KeysModifyInfo'
    }

    attribute_map = {
        'operations': 'operations',
        'modify_info': 'modify_info'
    }

    def __init__(self, operations=None, modify_info=None, _configuration=None):  # noqa: E501
        """EncryptionKeysModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operations = None
        self._modify_info = None
        self.discriminator = None

        self.operations = operations
        if modify_info is not None:
            self.modify_info = modify_info

    @property
    def operations(self):
        """Gets the operations of this EncryptionKeysModify.  # noqa: E501


        :return: The operations of this EncryptionKeysModify.  # noqa: E501
        :rtype: KeysOperations
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this EncryptionKeysModify.


        :param operations: The operations of this EncryptionKeysModify.  # noqa: E501
        :type: KeysOperations
        """
        if self._configuration.client_side_validation and operations is None:
            raise ValueError("Invalid value for `operations`, must not be `None`")  # noqa: E501

        self._operations = operations

    @property
    def modify_info(self):
        """Gets the modify_info of this EncryptionKeysModify.  # noqa: E501


        :return: The modify_info of this EncryptionKeysModify.  # noqa: E501
        :rtype: KeysModifyInfo
        """
        return self._modify_info

    @modify_info.setter
    def modify_info(self, modify_info):
        """Sets the modify_info of this EncryptionKeysModify.


        :param modify_info: The modify_info of this EncryptionKeysModify.  # noqa: E501
        :type: KeysModifyInfo
        """

        self._modify_info = modify_info

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
        if issubclass(EncryptionKeysModify, dict):
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
        if not isinstance(other, EncryptionKeysModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncryptionKeysModify):
            return True

        return self.to_dict() != other.to_dict()
