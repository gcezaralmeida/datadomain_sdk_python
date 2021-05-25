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


class SystemSpaceStatsInfo(object):
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
        'stats_epoch_details': 'SystemSpaceStatsDetails'
    }

    attribute_map = {
        'collection_epoch': 'collection_epoch',
        'stats_epoch_details': 'stats_epoch_details'
    }

    def __init__(self, collection_epoch=None, stats_epoch_details=None, _configuration=None):  # noqa: E501
        """SystemSpaceStatsInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collection_epoch = None
        self._stats_epoch_details = None
        self.discriminator = None

        if collection_epoch is not None:
            self.collection_epoch = collection_epoch
        if stats_epoch_details is not None:
            self.stats_epoch_details = stats_epoch_details

    @property
    def collection_epoch(self):
        """Gets the collection_epoch of this SystemSpaceStatsInfo.  # noqa: E501


        :return: The collection_epoch of this SystemSpaceStatsInfo.  # noqa: E501
        :rtype: int
        """
        return self._collection_epoch

    @collection_epoch.setter
    def collection_epoch(self, collection_epoch):
        """Sets the collection_epoch of this SystemSpaceStatsInfo.


        :param collection_epoch: The collection_epoch of this SystemSpaceStatsInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                collection_epoch is not None and collection_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `collection_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._collection_epoch = collection_epoch

    @property
    def stats_epoch_details(self):
        """Gets the stats_epoch_details of this SystemSpaceStatsInfo.  # noqa: E501


        :return: The stats_epoch_details of this SystemSpaceStatsInfo.  # noqa: E501
        :rtype: SystemSpaceStatsDetails
        """
        return self._stats_epoch_details

    @stats_epoch_details.setter
    def stats_epoch_details(self, stats_epoch_details):
        """Sets the stats_epoch_details of this SystemSpaceStatsInfo.


        :param stats_epoch_details: The stats_epoch_details of this SystemSpaceStatsInfo.  # noqa: E501
        :type: SystemSpaceStatsDetails
        """

        self._stats_epoch_details = stats_epoch_details

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
        if issubclass(SystemSpaceStatsInfo, dict):
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
        if not isinstance(other, SystemSpaceStatsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemSpaceStatsInfo):
            return True

        return self.to_dict() != other.to_dict()
