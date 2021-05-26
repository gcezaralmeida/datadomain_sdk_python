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


class AwsInfoCreate20(object):
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
        'region': 'AwsRegion',
        'storage_class': 'AwsClass'
    }

    attribute_map = {
        'region': 'region',
        'storage_class': 'storage_class'
    }

    def __init__(self, region=None, storage_class=None, _configuration=None):  # noqa: E501
        """AwsInfoCreate20 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._region = None
        self._storage_class = None
        self.discriminator = None

        self.region = region
        if storage_class is not None:
            self.storage_class = storage_class

    @property
    def region(self):
        """Gets the region of this AwsInfoCreate20.  # noqa: E501


        :return: The region of this AwsInfoCreate20.  # noqa: E501
        :rtype: AwsRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsInfoCreate20.


        :param region: The region of this AwsInfoCreate20.  # noqa: E501
        :type: AwsRegion
        """
        if self._configuration.client_side_validation and region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def storage_class(self):
        """Gets the storage_class of this AwsInfoCreate20.  # noqa: E501


        :return: The storage_class of this AwsInfoCreate20.  # noqa: E501
        :rtype: AwsClass
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this AwsInfoCreate20.


        :param storage_class: The storage_class of this AwsInfoCreate20.  # noqa: E501
        :type: AwsClass
        """

        self._storage_class = storage_class

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
        if issubclass(AwsInfoCreate20, dict):
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
        if not isinstance(other, AwsInfoCreate20):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsInfoCreate20):
            return True

        return self.to_dict() != other.to_dict()