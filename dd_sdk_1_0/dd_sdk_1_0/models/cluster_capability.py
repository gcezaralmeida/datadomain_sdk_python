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


class ClusterCapability(object):
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
        'capacity': 'int',
        'storage': 'int',
        'num_of_nodes': 'int'
    }

    attribute_map = {
        'capacity': 'capacity',
        'storage': 'storage',
        'num_of_nodes': 'num_of_nodes'
    }

    def __init__(self, capacity=None, storage=None, num_of_nodes=None, _configuration=None):  # noqa: E501
        """ClusterCapability - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._capacity = None
        self._storage = None
        self._num_of_nodes = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if storage is not None:
            self.storage = storage
        if num_of_nodes is not None:
            self.num_of_nodes = num_of_nodes

    @property
    def capacity(self):
        """Gets the capacity of this ClusterCapability.  # noqa: E501


        :return: The capacity of this ClusterCapability.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ClusterCapability.


        :param capacity: The capacity of this ClusterCapability.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                capacity is not None and capacity < 0):  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity = capacity

    @property
    def storage(self):
        """Gets the storage of this ClusterCapability.  # noqa: E501


        :return: The storage of this ClusterCapability.  # noqa: E501
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ClusterCapability.


        :param storage: The storage of this ClusterCapability.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                storage is not None and storage < 0):  # noqa: E501
            raise ValueError("Invalid value for `storage`, must be a value greater than or equal to `0`")  # noqa: E501

        self._storage = storage

    @property
    def num_of_nodes(self):
        """Gets the num_of_nodes of this ClusterCapability.  # noqa: E501


        :return: The num_of_nodes of this ClusterCapability.  # noqa: E501
        :rtype: int
        """
        return self._num_of_nodes

    @num_of_nodes.setter
    def num_of_nodes(self, num_of_nodes):
        """Sets the num_of_nodes of this ClusterCapability.


        :param num_of_nodes: The num_of_nodes of this ClusterCapability.  # noqa: E501
        :type: int
        """

        self._num_of_nodes = num_of_nodes

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
        if issubclass(ClusterCapability, dict):
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
        if not isinstance(other, ClusterCapability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterCapability):
            return True

        return self.to_dict() != other.to_dict()
