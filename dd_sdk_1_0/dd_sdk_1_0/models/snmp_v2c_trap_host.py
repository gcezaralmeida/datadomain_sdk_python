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


class SnmpV2cTrapHost(object):
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
        'trap_host': 'HostPortPair',
        'community': 'str'
    }

    attribute_map = {
        'trap_host': 'trap_host',
        'community': 'community'
    }

    def __init__(self, trap_host=None, community=None, _configuration=None):  # noqa: E501
        """SnmpV2cTrapHost - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._trap_host = None
        self._community = None
        self.discriminator = None

        self.trap_host = trap_host
        self.community = community

    @property
    def trap_host(self):
        """Gets the trap_host of this SnmpV2cTrapHost.  # noqa: E501


        :return: The trap_host of this SnmpV2cTrapHost.  # noqa: E501
        :rtype: HostPortPair
        """
        return self._trap_host

    @trap_host.setter
    def trap_host(self, trap_host):
        """Sets the trap_host of this SnmpV2cTrapHost.


        :param trap_host: The trap_host of this SnmpV2cTrapHost.  # noqa: E501
        :type: HostPortPair
        """
        if self._configuration.client_side_validation and trap_host is None:
            raise ValueError("Invalid value for `trap_host`, must not be `None`")  # noqa: E501

        self._trap_host = trap_host

    @property
    def community(self):
        """Gets the community of this SnmpV2cTrapHost.  # noqa: E501


        :return: The community of this SnmpV2cTrapHost.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SnmpV2cTrapHost.


        :param community: The community of this SnmpV2cTrapHost.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and community is None:
            raise ValueError("Invalid value for `community`, must not be `None`")  # noqa: E501

        self._community = community

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
        if issubclass(SnmpV2cTrapHost, dict):
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
        if not isinstance(other, SnmpV2cTrapHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnmpV2cTrapHost):
            return True

        return self.to_dict() != other.to_dict()