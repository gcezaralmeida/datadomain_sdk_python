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


class NetworkModify20(object):
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
        'operation': 'NetworkModifyOps',
        'domain_name': 'str',
        'host_name': 'str',
        'dns_servers': 'list[str]'
    }

    attribute_map = {
        'operation': 'operation',
        'domain_name': 'domain_name',
        'host_name': 'host_name',
        'dns_servers': 'dns_servers'
    }

    def __init__(self, operation=None, domain_name=None, host_name=None, dns_servers=None, _configuration=None):  # noqa: E501
        """NetworkModify20 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation = None
        self._domain_name = None
        self._host_name = None
        self._dns_servers = None
        self.discriminator = None

        self.operation = operation
        if domain_name is not None:
            self.domain_name = domain_name
        if host_name is not None:
            self.host_name = host_name
        if dns_servers is not None:
            self.dns_servers = dns_servers

    @property
    def operation(self):
        """Gets the operation of this NetworkModify20.  # noqa: E501


        :return: The operation of this NetworkModify20.  # noqa: E501
        :rtype: NetworkModifyOps
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this NetworkModify20.


        :param operation: The operation of this NetworkModify20.  # noqa: E501
        :type: NetworkModifyOps
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def domain_name(self):
        """Gets the domain_name of this NetworkModify20.  # noqa: E501


        :return: The domain_name of this NetworkModify20.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this NetworkModify20.


        :param domain_name: The domain_name of this NetworkModify20.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def host_name(self):
        """Gets the host_name of this NetworkModify20.  # noqa: E501


        :return: The host_name of this NetworkModify20.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this NetworkModify20.


        :param host_name: The host_name of this NetworkModify20.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def dns_servers(self):
        """Gets the dns_servers of this NetworkModify20.  # noqa: E501


        :return: The dns_servers of this NetworkModify20.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this NetworkModify20.


        :param dns_servers: The dns_servers of this NetworkModify20.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

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
        if issubclass(NetworkModify20, dict):
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
        if not isinstance(other, NetworkModify20):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkModify20):
            return True

        return self.to_dict() != other.to_dict()
