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


class PowerActionRequest(object):
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
        'targets': 'list[str]',
        'all_nodes': 'bool',
        'precheck_only': 'bool'
    }

    attribute_map = {
        'targets': 'targets',
        'all_nodes': 'all_nodes',
        'precheck_only': 'precheck_only'
    }

    def __init__(self, targets=None, all_nodes=None, precheck_only=None, _configuration=None):  # noqa: E501
        """PowerActionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._targets = None
        self._all_nodes = None
        self._precheck_only = None
        self.discriminator = None

        if targets is not None:
            self.targets = targets
        if all_nodes is not None:
            self.all_nodes = all_nodes
        if precheck_only is not None:
            self.precheck_only = precheck_only

    @property
    def targets(self):
        """Gets the targets of this PowerActionRequest.  # noqa: E501


        :return: The targets of this PowerActionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this PowerActionRequest.


        :param targets: The targets of this PowerActionRequest.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

    @property
    def all_nodes(self):
        """Gets the all_nodes of this PowerActionRequest.  # noqa: E501


        :return: The all_nodes of this PowerActionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._all_nodes

    @all_nodes.setter
    def all_nodes(self, all_nodes):
        """Sets the all_nodes of this PowerActionRequest.


        :param all_nodes: The all_nodes of this PowerActionRequest.  # noqa: E501
        :type: bool
        """

        self._all_nodes = all_nodes

    @property
    def precheck_only(self):
        """Gets the precheck_only of this PowerActionRequest.  # noqa: E501


        :return: The precheck_only of this PowerActionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._precheck_only

    @precheck_only.setter
    def precheck_only(self, precheck_only):
        """Sets the precheck_only of this PowerActionRequest.


        :param precheck_only: The precheck_only of this PowerActionRequest.  # noqa: E501
        :type: bool
        """

        self._precheck_only = precheck_only

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
        if issubclass(PowerActionRequest, dict):
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
        if not isinstance(other, PowerActionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerActionRequest):
            return True

        return self.to_dict() != other.to_dict()
