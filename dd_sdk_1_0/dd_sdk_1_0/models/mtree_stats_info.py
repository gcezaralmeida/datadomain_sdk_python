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


class MtreeStatsInfo(object):
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
        'mtree_integrated_usage': 'MtreeIntegratedUsage',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'mtree_integrated_usage': 'mtree_integrated_usage',
        'link': 'link'
    }

    def __init__(self, mtree_integrated_usage=None, link=None, _configuration=None):  # noqa: E501
        """MtreeStatsInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mtree_integrated_usage = None
        self._link = None
        self.discriminator = None

        if mtree_integrated_usage is not None:
            self.mtree_integrated_usage = mtree_integrated_usage
        if link is not None:
            self.link = link

    @property
    def mtree_integrated_usage(self):
        """Gets the mtree_integrated_usage of this MtreeStatsInfo.  # noqa: E501


        :return: The mtree_integrated_usage of this MtreeStatsInfo.  # noqa: E501
        :rtype: MtreeIntegratedUsage
        """
        return self._mtree_integrated_usage

    @mtree_integrated_usage.setter
    def mtree_integrated_usage(self, mtree_integrated_usage):
        """Sets the mtree_integrated_usage of this MtreeStatsInfo.


        :param mtree_integrated_usage: The mtree_integrated_usage of this MtreeStatsInfo.  # noqa: E501
        :type: MtreeIntegratedUsage
        """

        self._mtree_integrated_usage = mtree_integrated_usage

    @property
    def link(self):
        """Gets the link of this MtreeStatsInfo.  # noqa: E501


        :return: The link of this MtreeStatsInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this MtreeStatsInfo.


        :param link: The link of this MtreeStatsInfo.  # noqa: E501
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
        if issubclass(MtreeStatsInfo, dict):
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
        if not isinstance(other, MtreeStatsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MtreeStatsInfo):
            return True

        return self.to_dict() != other.to_dict()