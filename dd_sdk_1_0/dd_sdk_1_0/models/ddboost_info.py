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


class DdboostInfo(object):
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
        'ddboost_status': 'DdboostStatus',
        'ddboost_options': 'list[KeyValuePair]',
        'ddboost_file_replication_options': 'list[KeyValuePair]',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'ddboost_status': 'ddboost_status',
        'ddboost_options': 'ddboost_options',
        'ddboost_file_replication_options': 'ddboost_file_replication_options',
        'link': 'link'
    }

    def __init__(self, ddboost_status=None, ddboost_options=None, ddboost_file_replication_options=None, link=None, _configuration=None):  # noqa: E501
        """DdboostInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ddboost_status = None
        self._ddboost_options = None
        self._ddboost_file_replication_options = None
        self._link = None
        self.discriminator = None

        self.ddboost_status = ddboost_status
        if ddboost_options is not None:
            self.ddboost_options = ddboost_options
        if ddboost_file_replication_options is not None:
            self.ddboost_file_replication_options = ddboost_file_replication_options
        if link is not None:
            self.link = link

    @property
    def ddboost_status(self):
        """Gets the ddboost_status of this DdboostInfo.  # noqa: E501


        :return: The ddboost_status of this DdboostInfo.  # noqa: E501
        :rtype: DdboostStatus
        """
        return self._ddboost_status

    @ddboost_status.setter
    def ddboost_status(self, ddboost_status):
        """Sets the ddboost_status of this DdboostInfo.


        :param ddboost_status: The ddboost_status of this DdboostInfo.  # noqa: E501
        :type: DdboostStatus
        """
        if self._configuration.client_side_validation and ddboost_status is None:
            raise ValueError("Invalid value for `ddboost_status`, must not be `None`")  # noqa: E501

        self._ddboost_status = ddboost_status

    @property
    def ddboost_options(self):
        """Gets the ddboost_options of this DdboostInfo.  # noqa: E501


        :return: The ddboost_options of this DdboostInfo.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._ddboost_options

    @ddboost_options.setter
    def ddboost_options(self, ddboost_options):
        """Sets the ddboost_options of this DdboostInfo.


        :param ddboost_options: The ddboost_options of this DdboostInfo.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._ddboost_options = ddboost_options

    @property
    def ddboost_file_replication_options(self):
        """Gets the ddboost_file_replication_options of this DdboostInfo.  # noqa: E501


        :return: The ddboost_file_replication_options of this DdboostInfo.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._ddboost_file_replication_options

    @ddboost_file_replication_options.setter
    def ddboost_file_replication_options(self, ddboost_file_replication_options):
        """Sets the ddboost_file_replication_options of this DdboostInfo.


        :param ddboost_file_replication_options: The ddboost_file_replication_options of this DdboostInfo.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._ddboost_file_replication_options = ddboost_file_replication_options

    @property
    def link(self):
        """Gets the link of this DdboostInfo.  # noqa: E501


        :return: The link of this DdboostInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DdboostInfo.


        :param link: The link of this DdboostInfo.  # noqa: E501
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
        if issubclass(DdboostInfo, dict):
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
        if not isinstance(other, DdboostInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DdboostInfo):
            return True

        return self.to_dict() != other.to_dict()