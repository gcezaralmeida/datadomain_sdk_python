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


class StatsPerfInfo20(object):
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
        'collection_epoch': 'int',
        'cpu_stats': 'CpuStats',
        'network_throughput': 'list[NetworkThroughput]',
        'filesys_stats': 'FilesysStats',
        'backup_stats': 'DataInOutStats',
        'repl_stats': 'DataInOutStats'
    }

    attribute_map = {
        'collection_epoch': 'collection_epoch',
        'cpu_stats': 'cpu_stats',
        'network_throughput': 'network_throughput',
        'filesys_stats': 'filesys_stats',
        'backup_stats': 'backup_stats',
        'repl_stats': 'repl_stats'
    }

    def __init__(self, collection_epoch=None, cpu_stats=None, network_throughput=None, filesys_stats=None, backup_stats=None, repl_stats=None, _configuration=None):  # noqa: E501
        """StatsPerfInfo20 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collection_epoch = None
        self._cpu_stats = None
        self._network_throughput = None
        self._filesys_stats = None
        self._backup_stats = None
        self._repl_stats = None
        self.discriminator = None

        self.collection_epoch = collection_epoch
        if cpu_stats is not None:
            self.cpu_stats = cpu_stats
        if network_throughput is not None:
            self.network_throughput = network_throughput
        if filesys_stats is not None:
            self.filesys_stats = filesys_stats
        if backup_stats is not None:
            self.backup_stats = backup_stats
        if repl_stats is not None:
            self.repl_stats = repl_stats

    @property
    def collection_epoch(self):
        """Gets the collection_epoch of this StatsPerfInfo20.  # noqa: E501


        :return: The collection_epoch of this StatsPerfInfo20.  # noqa: E501
        :rtype: int
        """
        return self._collection_epoch

    @collection_epoch.setter
    def collection_epoch(self, collection_epoch):
        """Sets the collection_epoch of this StatsPerfInfo20.


        :param collection_epoch: The collection_epoch of this StatsPerfInfo20.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and collection_epoch is None:
            raise ValueError("Invalid value for `collection_epoch`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                collection_epoch is not None and collection_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `collection_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._collection_epoch = collection_epoch

    @property
    def cpu_stats(self):
        """Gets the cpu_stats of this StatsPerfInfo20.  # noqa: E501


        :return: The cpu_stats of this StatsPerfInfo20.  # noqa: E501
        :rtype: CpuStats
        """
        return self._cpu_stats

    @cpu_stats.setter
    def cpu_stats(self, cpu_stats):
        """Sets the cpu_stats of this StatsPerfInfo20.


        :param cpu_stats: The cpu_stats of this StatsPerfInfo20.  # noqa: E501
        :type: CpuStats
        """

        self._cpu_stats = cpu_stats

    @property
    def network_throughput(self):
        """Gets the network_throughput of this StatsPerfInfo20.  # noqa: E501


        :return: The network_throughput of this StatsPerfInfo20.  # noqa: E501
        :rtype: list[NetworkThroughput]
        """
        return self._network_throughput

    @network_throughput.setter
    def network_throughput(self, network_throughput):
        """Sets the network_throughput of this StatsPerfInfo20.


        :param network_throughput: The network_throughput of this StatsPerfInfo20.  # noqa: E501
        :type: list[NetworkThroughput]
        """

        self._network_throughput = network_throughput

    @property
    def filesys_stats(self):
        """Gets the filesys_stats of this StatsPerfInfo20.  # noqa: E501


        :return: The filesys_stats of this StatsPerfInfo20.  # noqa: E501
        :rtype: FilesysStats
        """
        return self._filesys_stats

    @filesys_stats.setter
    def filesys_stats(self, filesys_stats):
        """Sets the filesys_stats of this StatsPerfInfo20.


        :param filesys_stats: The filesys_stats of this StatsPerfInfo20.  # noqa: E501
        :type: FilesysStats
        """

        self._filesys_stats = filesys_stats

    @property
    def backup_stats(self):
        """Gets the backup_stats of this StatsPerfInfo20.  # noqa: E501


        :return: The backup_stats of this StatsPerfInfo20.  # noqa: E501
        :rtype: DataInOutStats
        """
        return self._backup_stats

    @backup_stats.setter
    def backup_stats(self, backup_stats):
        """Sets the backup_stats of this StatsPerfInfo20.


        :param backup_stats: The backup_stats of this StatsPerfInfo20.  # noqa: E501
        :type: DataInOutStats
        """

        self._backup_stats = backup_stats

    @property
    def repl_stats(self):
        """Gets the repl_stats of this StatsPerfInfo20.  # noqa: E501


        :return: The repl_stats of this StatsPerfInfo20.  # noqa: E501
        :rtype: DataInOutStats
        """
        return self._repl_stats

    @repl_stats.setter
    def repl_stats(self, repl_stats):
        """Sets the repl_stats of this StatsPerfInfo20.


        :param repl_stats: The repl_stats of this StatsPerfInfo20.  # noqa: E501
        :type: DataInOutStats
        """

        self._repl_stats = repl_stats

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
        if issubclass(StatsPerfInfo20, dict):
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
        if not isinstance(other, StatsPerfInfo20):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsPerfInfo20):
            return True

        return self.to_dict() != other.to_dict()
