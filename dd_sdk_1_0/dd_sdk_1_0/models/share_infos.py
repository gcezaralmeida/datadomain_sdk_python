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


class ShareInfos(object):
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
        'share': 'list[ShareInfo]',
        'paging_info': 'Paging'
    }

    attribute_map = {
        'share': 'share',
        'paging_info': 'paging_info'
    }

    def __init__(self, share=None, paging_info=None, _configuration=None):  # noqa: E501
        """ShareInfos - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._share = None
        self._paging_info = None
        self.discriminator = None

        if share is not None:
            self.share = share
        if paging_info is not None:
            self.paging_info = paging_info

    @property
    def share(self):
        """Gets the share of this ShareInfos.  # noqa: E501


        :return: The share of this ShareInfos.  # noqa: E501
        :rtype: list[ShareInfo]
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this ShareInfos.


        :param share: The share of this ShareInfos.  # noqa: E501
        :type: list[ShareInfo]
        """

        self._share = share

    @property
    def paging_info(self):
        """Gets the paging_info of this ShareInfos.  # noqa: E501


        :return: The paging_info of this ShareInfos.  # noqa: E501
        :rtype: Paging
        """
        return self._paging_info

    @paging_info.setter
    def paging_info(self, paging_info):
        """Sets the paging_info of this ShareInfos.


        :param paging_info: The paging_info of this ShareInfos.  # noqa: E501
        :type: Paging
        """

        self._paging_info = paging_info

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
        if issubclass(ShareInfos, dict):
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
        if not isinstance(other, ShareInfos):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareInfos):
            return True

        return self.to_dict() != other.to_dict()
