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


class FileReplicationDetails(object):
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
        'id': 'str',
        'active_files': 'int',
        'logical_replicated': 'int',
        'last_sync_time': 'str',
        'logical_compression_bytes': 'int',
        'network_bytes': 'int',
        'repl_status': 'FileReplStatus',
        'direction': 'FileReplDirection',
        'last_24hrs': 'FileReplicationLast24hrsDetails',
        'local_system': 'FileReplicationLocalSystemDetails',
        'remote_system': 'FileReplicationRemoteSystemDetails',
        'timestamp': 'int',
        'compression_ratio': 'str',
        'link': 'RestLinkRep'
    }

    attribute_map = {
        'id': 'id',
        'active_files': 'active_files',
        'logical_replicated': 'logical_replicated',
        'last_sync_time': 'last_sync_time',
        'logical_compression_bytes': 'logical_compression_bytes',
        'network_bytes': 'network_bytes',
        'repl_status': 'repl_status',
        'direction': 'direction',
        'last_24hrs': 'last_24hrs',
        'local_system': 'local_system',
        'remote_system': 'remote_system',
        'timestamp': 'timestamp',
        'compression_ratio': 'compression_ratio',
        'link': 'link'
    }

    def __init__(self, id=None, active_files=None, logical_replicated=None, last_sync_time=None, logical_compression_bytes=None, network_bytes=None, repl_status=None, direction=None, last_24hrs=None, local_system=None, remote_system=None, timestamp=None, compression_ratio=None, link=None, _configuration=None):  # noqa: E501
        """FileReplicationDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._active_files = None
        self._logical_replicated = None
        self._last_sync_time = None
        self._logical_compression_bytes = None
        self._network_bytes = None
        self._repl_status = None
        self._direction = None
        self._last_24hrs = None
        self._local_system = None
        self._remote_system = None
        self._timestamp = None
        self._compression_ratio = None
        self._link = None
        self.discriminator = None

        self.id = id
        self.active_files = active_files
        self.logical_replicated = logical_replicated
        self.last_sync_time = last_sync_time
        self.logical_compression_bytes = logical_compression_bytes
        self.network_bytes = network_bytes
        self.repl_status = repl_status
        self.direction = direction
        self.last_24hrs = last_24hrs
        self.local_system = local_system
        self.remote_system = remote_system
        self.timestamp = timestamp
        self.compression_ratio = compression_ratio
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this FileReplicationDetails.  # noqa: E501


        :return: The id of this FileReplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileReplicationDetails.


        :param id: The id of this FileReplicationDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def active_files(self):
        """Gets the active_files of this FileReplicationDetails.  # noqa: E501


        :return: The active_files of this FileReplicationDetails.  # noqa: E501
        :rtype: int
        """
        return self._active_files

    @active_files.setter
    def active_files(self, active_files):
        """Sets the active_files of this FileReplicationDetails.


        :param active_files: The active_files of this FileReplicationDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and active_files is None:
            raise ValueError("Invalid value for `active_files`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                active_files is not None and active_files < 0):  # noqa: E501
            raise ValueError("Invalid value for `active_files`, must be a value greater than or equal to `0`")  # noqa: E501

        self._active_files = active_files

    @property
    def logical_replicated(self):
        """Gets the logical_replicated of this FileReplicationDetails.  # noqa: E501


        :return: The logical_replicated of this FileReplicationDetails.  # noqa: E501
        :rtype: int
        """
        return self._logical_replicated

    @logical_replicated.setter
    def logical_replicated(self, logical_replicated):
        """Sets the logical_replicated of this FileReplicationDetails.


        :param logical_replicated: The logical_replicated of this FileReplicationDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and logical_replicated is None:
            raise ValueError("Invalid value for `logical_replicated`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_replicated is not None and logical_replicated < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_replicated`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_replicated = logical_replicated

    @property
    def last_sync_time(self):
        """Gets the last_sync_time of this FileReplicationDetails.  # noqa: E501


        :return: The last_sync_time of this FileReplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._last_sync_time

    @last_sync_time.setter
    def last_sync_time(self, last_sync_time):
        """Sets the last_sync_time of this FileReplicationDetails.


        :param last_sync_time: The last_sync_time of this FileReplicationDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_sync_time is None:
            raise ValueError("Invalid value for `last_sync_time`, must not be `None`")  # noqa: E501

        self._last_sync_time = last_sync_time

    @property
    def logical_compression_bytes(self):
        """Gets the logical_compression_bytes of this FileReplicationDetails.  # noqa: E501


        :return: The logical_compression_bytes of this FileReplicationDetails.  # noqa: E501
        :rtype: int
        """
        return self._logical_compression_bytes

    @logical_compression_bytes.setter
    def logical_compression_bytes(self, logical_compression_bytes):
        """Sets the logical_compression_bytes of this FileReplicationDetails.


        :param logical_compression_bytes: The logical_compression_bytes of this FileReplicationDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and logical_compression_bytes is None:
            raise ValueError("Invalid value for `logical_compression_bytes`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_compression_bytes is not None and logical_compression_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_compression_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_compression_bytes = logical_compression_bytes

    @property
    def network_bytes(self):
        """Gets the network_bytes of this FileReplicationDetails.  # noqa: E501


        :return: The network_bytes of this FileReplicationDetails.  # noqa: E501
        :rtype: int
        """
        return self._network_bytes

    @network_bytes.setter
    def network_bytes(self, network_bytes):
        """Sets the network_bytes of this FileReplicationDetails.


        :param network_bytes: The network_bytes of this FileReplicationDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and network_bytes is None:
            raise ValueError("Invalid value for `network_bytes`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                network_bytes is not None and network_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `network_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._network_bytes = network_bytes

    @property
    def repl_status(self):
        """Gets the repl_status of this FileReplicationDetails.  # noqa: E501


        :return: The repl_status of this FileReplicationDetails.  # noqa: E501
        :rtype: FileReplStatus
        """
        return self._repl_status

    @repl_status.setter
    def repl_status(self, repl_status):
        """Sets the repl_status of this FileReplicationDetails.


        :param repl_status: The repl_status of this FileReplicationDetails.  # noqa: E501
        :type: FileReplStatus
        """
        if self._configuration.client_side_validation and repl_status is None:
            raise ValueError("Invalid value for `repl_status`, must not be `None`")  # noqa: E501

        self._repl_status = repl_status

    @property
    def direction(self):
        """Gets the direction of this FileReplicationDetails.  # noqa: E501


        :return: The direction of this FileReplicationDetails.  # noqa: E501
        :rtype: FileReplDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this FileReplicationDetails.


        :param direction: The direction of this FileReplicationDetails.  # noqa: E501
        :type: FileReplDirection
        """
        if self._configuration.client_side_validation and direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def last_24hrs(self):
        """Gets the last_24hrs of this FileReplicationDetails.  # noqa: E501


        :return: The last_24hrs of this FileReplicationDetails.  # noqa: E501
        :rtype: FileReplicationLast24hrsDetails
        """
        return self._last_24hrs

    @last_24hrs.setter
    def last_24hrs(self, last_24hrs):
        """Sets the last_24hrs of this FileReplicationDetails.


        :param last_24hrs: The last_24hrs of this FileReplicationDetails.  # noqa: E501
        :type: FileReplicationLast24hrsDetails
        """
        if self._configuration.client_side_validation and last_24hrs is None:
            raise ValueError("Invalid value for `last_24hrs`, must not be `None`")  # noqa: E501

        self._last_24hrs = last_24hrs

    @property
    def local_system(self):
        """Gets the local_system of this FileReplicationDetails.  # noqa: E501


        :return: The local_system of this FileReplicationDetails.  # noqa: E501
        :rtype: FileReplicationLocalSystemDetails
        """
        return self._local_system

    @local_system.setter
    def local_system(self, local_system):
        """Sets the local_system of this FileReplicationDetails.


        :param local_system: The local_system of this FileReplicationDetails.  # noqa: E501
        :type: FileReplicationLocalSystemDetails
        """
        if self._configuration.client_side_validation and local_system is None:
            raise ValueError("Invalid value for `local_system`, must not be `None`")  # noqa: E501

        self._local_system = local_system

    @property
    def remote_system(self):
        """Gets the remote_system of this FileReplicationDetails.  # noqa: E501


        :return: The remote_system of this FileReplicationDetails.  # noqa: E501
        :rtype: FileReplicationRemoteSystemDetails
        """
        return self._remote_system

    @remote_system.setter
    def remote_system(self, remote_system):
        """Sets the remote_system of this FileReplicationDetails.


        :param remote_system: The remote_system of this FileReplicationDetails.  # noqa: E501
        :type: FileReplicationRemoteSystemDetails
        """
        if self._configuration.client_side_validation and remote_system is None:
            raise ValueError("Invalid value for `remote_system`, must not be `None`")  # noqa: E501

        self._remote_system = remote_system

    @property
    def timestamp(self):
        """Gets the timestamp of this FileReplicationDetails.  # noqa: E501


        :return: The timestamp of this FileReplicationDetails.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this FileReplicationDetails.


        :param timestamp: The timestamp of this FileReplicationDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                timestamp is not None and timestamp < 0):  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `0`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def compression_ratio(self):
        """Gets the compression_ratio of this FileReplicationDetails.  # noqa: E501


        :return: The compression_ratio of this FileReplicationDetails.  # noqa: E501
        :rtype: str
        """
        return self._compression_ratio

    @compression_ratio.setter
    def compression_ratio(self, compression_ratio):
        """Sets the compression_ratio of this FileReplicationDetails.


        :param compression_ratio: The compression_ratio of this FileReplicationDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and compression_ratio is None:
            raise ValueError("Invalid value for `compression_ratio`, must not be `None`")  # noqa: E501

        self._compression_ratio = compression_ratio

    @property
    def link(self):
        """Gets the link of this FileReplicationDetails.  # noqa: E501


        :return: The link of this FileReplicationDetails.  # noqa: E501
        :rtype: RestLinkRep
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this FileReplicationDetails.


        :param link: The link of this FileReplicationDetails.  # noqa: E501
        :type: RestLinkRep
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
        if issubclass(FileReplicationDetails, dict):
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
        if not isinstance(other, FileReplicationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileReplicationDetails):
            return True

        return self.to_dict() != other.to_dict()
