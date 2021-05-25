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


class DdboostModify(object):
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
        'operation': 'DdboostModifyOperations',
        'ddboost_options': 'list[DdboostOption]',
        'ddboost_file_replication_options': 'list[DdboostFileReplicationOption]'
    }

    attribute_map = {
        'operation': 'operation',
        'ddboost_options': 'ddboost_options',
        'ddboost_file_replication_options': 'ddboost_file_replication_options'
    }

    def __init__(self, operation=None, ddboost_options=None, ddboost_file_replication_options=None, _configuration=None):  # noqa: E501
        """DdboostModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation = None
        self._ddboost_options = None
        self._ddboost_file_replication_options = None
        self.discriminator = None

        self.operation = operation
        if ddboost_options is not None:
            self.ddboost_options = ddboost_options
        if ddboost_file_replication_options is not None:
            self.ddboost_file_replication_options = ddboost_file_replication_options

    @property
    def operation(self):
        """Gets the operation of this DdboostModify.  # noqa: E501


        :return: The operation of this DdboostModify.  # noqa: E501
        :rtype: DdboostModifyOperations
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this DdboostModify.


        :param operation: The operation of this DdboostModify.  # noqa: E501
        :type: DdboostModifyOperations
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def ddboost_options(self):
        """Gets the ddboost_options of this DdboostModify.  # noqa: E501


        :return: The ddboost_options of this DdboostModify.  # noqa: E501
        :rtype: list[DdboostOption]
        """
        return self._ddboost_options

    @ddboost_options.setter
    def ddboost_options(self, ddboost_options):
        """Sets the ddboost_options of this DdboostModify.


        :param ddboost_options: The ddboost_options of this DdboostModify.  # noqa: E501
        :type: list[DdboostOption]
        """

        self._ddboost_options = ddboost_options

    @property
    def ddboost_file_replication_options(self):
        """Gets the ddboost_file_replication_options of this DdboostModify.  # noqa: E501


        :return: The ddboost_file_replication_options of this DdboostModify.  # noqa: E501
        :rtype: list[DdboostFileReplicationOption]
        """
        return self._ddboost_file_replication_options

    @ddboost_file_replication_options.setter
    def ddboost_file_replication_options(self, ddboost_file_replication_options):
        """Sets the ddboost_file_replication_options of this DdboostModify.


        :param ddboost_file_replication_options: The ddboost_file_replication_options of this DdboostModify.  # noqa: E501
        :type: list[DdboostFileReplicationOption]
        """

        self._ddboost_file_replication_options = ddboost_file_replication_options

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
        if issubclass(DdboostModify, dict):
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
        if not isinstance(other, DdboostModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DdboostModify):
            return True

        return self.to_dict() != other.to_dict()
