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


class FileReplicationLocalSystemDetails(object):
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
        'storage_unit': 'str',
        'logical_remaining': 'int',
        'repl_system_status': 'FileReplSystemStatus'
    }

    attribute_map = {
        'hostname': 'hostname',
        'storage_unit': 'storage_unit',
        'logical_remaining': 'logical_remaining',
        'repl_system_status': 'repl_system_status'
    }

    def __init__(self, hostname=None, storage_unit=None, logical_remaining=None, repl_system_status=None, _configuration=None):  # noqa: E501
        """FileReplicationLocalSystemDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hostname = None
        self._storage_unit = None
        self._logical_remaining = None
        self._repl_system_status = None
        self.discriminator = None

        self.hostname = hostname
        self.storage_unit = storage_unit
        self.logical_remaining = logical_remaining
        self.repl_system_status = repl_system_status

    @property
    def hostname(self):
        """Gets the hostname of this FileReplicationLocalSystemDetails.  # noqa: E501


        :return: The hostname of this FileReplicationLocalSystemDetails.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this FileReplicationLocalSystemDetails.


        :param hostname: The hostname of this FileReplicationLocalSystemDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def storage_unit(self):
        """Gets the storage_unit of this FileReplicationLocalSystemDetails.  # noqa: E501


        :return: The storage_unit of this FileReplicationLocalSystemDetails.  # noqa: E501
        :rtype: str
        """
        return self._storage_unit

    @storage_unit.setter
    def storage_unit(self, storage_unit):
        """Sets the storage_unit of this FileReplicationLocalSystemDetails.


        :param storage_unit: The storage_unit of this FileReplicationLocalSystemDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_unit is None:
            raise ValueError("Invalid value for `storage_unit`, must not be `None`")  # noqa: E501

        self._storage_unit = storage_unit

    @property
    def logical_remaining(self):
        """Gets the logical_remaining of this FileReplicationLocalSystemDetails.  # noqa: E501


        :return: The logical_remaining of this FileReplicationLocalSystemDetails.  # noqa: E501
        :rtype: int
        """
        return self._logical_remaining

    @logical_remaining.setter
    def logical_remaining(self, logical_remaining):
        """Sets the logical_remaining of this FileReplicationLocalSystemDetails.


        :param logical_remaining: The logical_remaining of this FileReplicationLocalSystemDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and logical_remaining is None:
            raise ValueError("Invalid value for `logical_remaining`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_remaining is not None and logical_remaining < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_remaining`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_remaining = logical_remaining

    @property
    def repl_system_status(self):
        """Gets the repl_system_status of this FileReplicationLocalSystemDetails.  # noqa: E501


        :return: The repl_system_status of this FileReplicationLocalSystemDetails.  # noqa: E501
        :rtype: FileReplSystemStatus
        """
        return self._repl_system_status

    @repl_system_status.setter
    def repl_system_status(self, repl_system_status):
        """Sets the repl_system_status of this FileReplicationLocalSystemDetails.


        :param repl_system_status: The repl_system_status of this FileReplicationLocalSystemDetails.  # noqa: E501
        :type: FileReplSystemStatus
        """
        if self._configuration.client_side_validation and repl_system_status is None:
            raise ValueError("Invalid value for `repl_system_status`, must not be `None`")  # noqa: E501

        self._repl_system_status = repl_system_status

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
        if issubclass(FileReplicationLocalSystemDetails, dict):
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
        if not isinstance(other, FileReplicationLocalSystemDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileReplicationLocalSystemDetails):
            return True

        return self.to_dict() != other.to_dict()
