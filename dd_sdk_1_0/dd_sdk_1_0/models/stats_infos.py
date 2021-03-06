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


class StatsInfos(object):
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
        'stats': 'list[StatsInfo]',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'stats': 'stats',
        'link': 'link'
    }

    def __init__(self, stats=None, link=None, _configuration=None):  # noqa: E501
        """StatsInfos - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._stats = None
        self._link = None
        self.discriminator = None

        self.stats = stats
        if link is not None:
            self.link = link

    @property
    def stats(self):
        """Gets the stats of this StatsInfos.  # noqa: E501


        :return: The stats of this StatsInfos.  # noqa: E501
        :rtype: list[StatsInfo]
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this StatsInfos.


        :param stats: The stats of this StatsInfos.  # noqa: E501
        :type: list[StatsInfo]
        """
        if self._configuration.client_side_validation and stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")  # noqa: E501

        self._stats = stats

    @property
    def link(self):
        """Gets the link of this StatsInfos.  # noqa: E501


        :return: The link of this StatsInfos.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this StatsInfos.


        :param link: The link of this StatsInfos.  # noqa: E501
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
        if issubclass(StatsInfos, dict):
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
        if not isinstance(other, StatsInfos):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsInfos):
            return True

        return self.to_dict() != other.to_dict()
