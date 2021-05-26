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


class SnmpInfo(object):
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
        'status': 'str',
        'general_info': 'SnmpGeneralInfo',
        'v2c_access_hosts': 'list[SnmpAccessHost]',
        'v3_users': 'list[SnmpUserInfo]',
        'v2c_traphosts': 'list[SnmpV2cTrapHost]',
        'v3_traphosts': 'list[SnmpV3TrapHost]',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'status': 'status',
        'general_info': 'general_info',
        'v2c_access_hosts': 'v2c_access_hosts',
        'v3_users': 'v3_users',
        'v2c_traphosts': 'v2c_traphosts',
        'v3_traphosts': 'v3_traphosts',
        'link': 'link'
    }

    def __init__(self, status=None, general_info=None, v2c_access_hosts=None, v3_users=None, v2c_traphosts=None, v3_traphosts=None, link=None, _configuration=None):  # noqa: E501
        """SnmpInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._general_info = None
        self._v2c_access_hosts = None
        self._v3_users = None
        self._v2c_traphosts = None
        self._v3_traphosts = None
        self._link = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if general_info is not None:
            self.general_info = general_info
        if v2c_access_hosts is not None:
            self.v2c_access_hosts = v2c_access_hosts
        if v3_users is not None:
            self.v3_users = v3_users
        if v2c_traphosts is not None:
            self.v2c_traphosts = v2c_traphosts
        if v3_traphosts is not None:
            self.v3_traphosts = v3_traphosts
        if link is not None:
            self.link = link

    @property
    def status(self):
        """Gets the status of this SnmpInfo.  # noqa: E501


        :return: The status of this SnmpInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnmpInfo.


        :param status: The status of this SnmpInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def general_info(self):
        """Gets the general_info of this SnmpInfo.  # noqa: E501


        :return: The general_info of this SnmpInfo.  # noqa: E501
        :rtype: SnmpGeneralInfo
        """
        return self._general_info

    @general_info.setter
    def general_info(self, general_info):
        """Sets the general_info of this SnmpInfo.


        :param general_info: The general_info of this SnmpInfo.  # noqa: E501
        :type: SnmpGeneralInfo
        """

        self._general_info = general_info

    @property
    def v2c_access_hosts(self):
        """Gets the v2c_access_hosts of this SnmpInfo.  # noqa: E501


        :return: The v2c_access_hosts of this SnmpInfo.  # noqa: E501
        :rtype: list[SnmpAccessHost]
        """
        return self._v2c_access_hosts

    @v2c_access_hosts.setter
    def v2c_access_hosts(self, v2c_access_hosts):
        """Sets the v2c_access_hosts of this SnmpInfo.


        :param v2c_access_hosts: The v2c_access_hosts of this SnmpInfo.  # noqa: E501
        :type: list[SnmpAccessHost]
        """

        self._v2c_access_hosts = v2c_access_hosts

    @property
    def v3_users(self):
        """Gets the v3_users of this SnmpInfo.  # noqa: E501


        :return: The v3_users of this SnmpInfo.  # noqa: E501
        :rtype: list[SnmpUserInfo]
        """
        return self._v3_users

    @v3_users.setter
    def v3_users(self, v3_users):
        """Sets the v3_users of this SnmpInfo.


        :param v3_users: The v3_users of this SnmpInfo.  # noqa: E501
        :type: list[SnmpUserInfo]
        """

        self._v3_users = v3_users

    @property
    def v2c_traphosts(self):
        """Gets the v2c_traphosts of this SnmpInfo.  # noqa: E501


        :return: The v2c_traphosts of this SnmpInfo.  # noqa: E501
        :rtype: list[SnmpV2cTrapHost]
        """
        return self._v2c_traphosts

    @v2c_traphosts.setter
    def v2c_traphosts(self, v2c_traphosts):
        """Sets the v2c_traphosts of this SnmpInfo.


        :param v2c_traphosts: The v2c_traphosts of this SnmpInfo.  # noqa: E501
        :type: list[SnmpV2cTrapHost]
        """

        self._v2c_traphosts = v2c_traphosts

    @property
    def v3_traphosts(self):
        """Gets the v3_traphosts of this SnmpInfo.  # noqa: E501


        :return: The v3_traphosts of this SnmpInfo.  # noqa: E501
        :rtype: list[SnmpV3TrapHost]
        """
        return self._v3_traphosts

    @v3_traphosts.setter
    def v3_traphosts(self, v3_traphosts):
        """Sets the v3_traphosts of this SnmpInfo.


        :param v3_traphosts: The v3_traphosts of this SnmpInfo.  # noqa: E501
        :type: list[SnmpV3TrapHost]
        """

        self._v3_traphosts = v3_traphosts

    @property
    def link(self):
        """Gets the link of this SnmpInfo.  # noqa: E501


        :return: The link of this SnmpInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SnmpInfo.


        :param link: The link of this SnmpInfo.  # noqa: E501
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
        if issubclass(SnmpInfo, dict):
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
        if not isinstance(other, SnmpInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnmpInfo):
            return True

        return self.to_dict() != other.to_dict()