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


class FileReplicationHistoricalStats(object):
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
        'outbound': 'list[FileReplicationHistoricalStatsDetails]',
        'inbound': 'list[FileReplicationHistoricalStatsDetails]',
        'start': 'int',
        'end': 'int',
        'interval': 'StatsIntervalQuery'
    }

    attribute_map = {
        'outbound': 'outbound',
        'inbound': 'inbound',
        'start': 'start',
        'end': 'end',
        'interval': 'interval'
    }

    def __init__(self, outbound=None, inbound=None, start=None, end=None, interval=None, _configuration=None):  # noqa: E501
        """FileReplicationHistoricalStats - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._outbound = None
        self._inbound = None
        self._start = None
        self._end = None
        self._interval = None
        self.discriminator = None

        self.outbound = outbound
        self.inbound = inbound
        self.start = start
        self.end = end
        self.interval = interval

    @property
    def outbound(self):
        """Gets the outbound of this FileReplicationHistoricalStats.  # noqa: E501


        :return: The outbound of this FileReplicationHistoricalStats.  # noqa: E501
        :rtype: list[FileReplicationHistoricalStatsDetails]
        """
        return self._outbound

    @outbound.setter
    def outbound(self, outbound):
        """Sets the outbound of this FileReplicationHistoricalStats.


        :param outbound: The outbound of this FileReplicationHistoricalStats.  # noqa: E501
        :type: list[FileReplicationHistoricalStatsDetails]
        """
        if self._configuration.client_side_validation and outbound is None:
            raise ValueError("Invalid value for `outbound`, must not be `None`")  # noqa: E501

        self._outbound = outbound

    @property
    def inbound(self):
        """Gets the inbound of this FileReplicationHistoricalStats.  # noqa: E501


        :return: The inbound of this FileReplicationHistoricalStats.  # noqa: E501
        :rtype: list[FileReplicationHistoricalStatsDetails]
        """
        return self._inbound

    @inbound.setter
    def inbound(self, inbound):
        """Sets the inbound of this FileReplicationHistoricalStats.


        :param inbound: The inbound of this FileReplicationHistoricalStats.  # noqa: E501
        :type: list[FileReplicationHistoricalStatsDetails]
        """
        if self._configuration.client_side_validation and inbound is None:
            raise ValueError("Invalid value for `inbound`, must not be `None`")  # noqa: E501

        self._inbound = inbound

    @property
    def start(self):
        """Gets the start of this FileReplicationHistoricalStats.  # noqa: E501


        :return: The start of this FileReplicationHistoricalStats.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this FileReplicationHistoricalStats.


        :param start: The start of this FileReplicationHistoricalStats.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                start is not None and start < 0):  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this FileReplicationHistoricalStats.  # noqa: E501


        :return: The end of this FileReplicationHistoricalStats.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this FileReplicationHistoricalStats.


        :param end: The end of this FileReplicationHistoricalStats.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                end is not None and end < 0):  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end = end

    @property
    def interval(self):
        """Gets the interval of this FileReplicationHistoricalStats.  # noqa: E501


        :return: The interval of this FileReplicationHistoricalStats.  # noqa: E501
        :rtype: StatsIntervalQuery
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this FileReplicationHistoricalStats.


        :param interval: The interval of this FileReplicationHistoricalStats.  # noqa: E501
        :type: StatsIntervalQuery
        """
        if self._configuration.client_side_validation and interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

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
        if issubclass(FileReplicationHistoricalStats, dict):
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
        if not isinstance(other, FileReplicationHistoricalStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileReplicationHistoricalStats):
            return True

        return self.to_dict() != other.to_dict()
