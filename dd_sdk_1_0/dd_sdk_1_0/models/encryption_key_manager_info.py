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


class EncryptionKeyManagerInfo(object):
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
        'key_manager': 'str',
        'key_manager_status': 'str',
        'key_manager_info': 'KeyManagerInfo',
        'last_key_rotation_date': 'int',
        'next_key_rotation_date': 'int',
        'action_needed': 'str',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'key_manager': 'key_manager',
        'key_manager_status': 'key_manager_status',
        'key_manager_info': 'key_manager_info',
        'last_key_rotation_date': 'last_key_rotation_date',
        'next_key_rotation_date': 'next_key_rotation_date',
        'action_needed': 'action_needed',
        'link': 'link'
    }

    def __init__(self, key_manager=None, key_manager_status=None, key_manager_info=None, last_key_rotation_date=None, next_key_rotation_date=None, action_needed=None, link=None, _configuration=None):  # noqa: E501
        """EncryptionKeyManagerInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key_manager = None
        self._key_manager_status = None
        self._key_manager_info = None
        self._last_key_rotation_date = None
        self._next_key_rotation_date = None
        self._action_needed = None
        self._link = None
        self.discriminator = None

        if key_manager is not None:
            self.key_manager = key_manager
        if key_manager_status is not None:
            self.key_manager_status = key_manager_status
        if key_manager_info is not None:
            self.key_manager_info = key_manager_info
        if last_key_rotation_date is not None:
            self.last_key_rotation_date = last_key_rotation_date
        if next_key_rotation_date is not None:
            self.next_key_rotation_date = next_key_rotation_date
        if action_needed is not None:
            self.action_needed = action_needed
        if link is not None:
            self.link = link

    @property
    def key_manager(self):
        """Gets the key_manager of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The key_manager of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_manager

    @key_manager.setter
    def key_manager(self, key_manager):
        """Sets the key_manager of this EncryptionKeyManagerInfo.


        :param key_manager: The key_manager of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: str
        """

        self._key_manager = key_manager

    @property
    def key_manager_status(self):
        """Gets the key_manager_status of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The key_manager_status of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_manager_status

    @key_manager_status.setter
    def key_manager_status(self, key_manager_status):
        """Sets the key_manager_status of this EncryptionKeyManagerInfo.


        :param key_manager_status: The key_manager_status of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: str
        """

        self._key_manager_status = key_manager_status

    @property
    def key_manager_info(self):
        """Gets the key_manager_info of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The key_manager_info of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: KeyManagerInfo
        """
        return self._key_manager_info

    @key_manager_info.setter
    def key_manager_info(self, key_manager_info):
        """Sets the key_manager_info of this EncryptionKeyManagerInfo.


        :param key_manager_info: The key_manager_info of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: KeyManagerInfo
        """

        self._key_manager_info = key_manager_info

    @property
    def last_key_rotation_date(self):
        """Gets the last_key_rotation_date of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The last_key_rotation_date of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_key_rotation_date

    @last_key_rotation_date.setter
    def last_key_rotation_date(self, last_key_rotation_date):
        """Sets the last_key_rotation_date of this EncryptionKeyManagerInfo.


        :param last_key_rotation_date: The last_key_rotation_date of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                last_key_rotation_date is not None and last_key_rotation_date < 0):  # noqa: E501
            raise ValueError("Invalid value for `last_key_rotation_date`, must be a value greater than or equal to `0`")  # noqa: E501

        self._last_key_rotation_date = last_key_rotation_date

    @property
    def next_key_rotation_date(self):
        """Gets the next_key_rotation_date of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The next_key_rotation_date of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: int
        """
        return self._next_key_rotation_date

    @next_key_rotation_date.setter
    def next_key_rotation_date(self, next_key_rotation_date):
        """Sets the next_key_rotation_date of this EncryptionKeyManagerInfo.


        :param next_key_rotation_date: The next_key_rotation_date of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                next_key_rotation_date is not None and next_key_rotation_date < 0):  # noqa: E501
            raise ValueError("Invalid value for `next_key_rotation_date`, must be a value greater than or equal to `0`")  # noqa: E501

        self._next_key_rotation_date = next_key_rotation_date

    @property
    def action_needed(self):
        """Gets the action_needed of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The action_needed of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: str
        """
        return self._action_needed

    @action_needed.setter
    def action_needed(self, action_needed):
        """Sets the action_needed of this EncryptionKeyManagerInfo.


        :param action_needed: The action_needed of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: str
        """

        self._action_needed = action_needed

    @property
    def link(self):
        """Gets the link of this EncryptionKeyManagerInfo.  # noqa: E501


        :return: The link of this EncryptionKeyManagerInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EncryptionKeyManagerInfo.


        :param link: The link of this EncryptionKeyManagerInfo.  # noqa: E501
        :type: list[RestLinkRep]
        """

        self._link = link

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
        if issubclass(EncryptionKeyManagerInfo, dict):
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
        if not isinstance(other, EncryptionKeyManagerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncryptionKeyManagerInfo):
            return True

        return self.to_dict() != other.to_dict()
