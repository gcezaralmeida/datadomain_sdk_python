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


class VdiskDevicesModify(object):
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
        'item': 'list[VdiskDevicesModifyItem]',
        'common_property': 'list[KeyValuePairModify]'
    }

    attribute_map = {
        'item': 'item',
        'common_property': 'common_property'
    }

    def __init__(self, item=None, common_property=None, _configuration=None):  # noqa: E501
        """VdiskDevicesModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._item = None
        self._common_property = None
        self.discriminator = None

        self.item = item
        if common_property is not None:
            self.common_property = common_property

    @property
    def item(self):
        """Gets the item of this VdiskDevicesModify.  # noqa: E501


        :return: The item of this VdiskDevicesModify.  # noqa: E501
        :rtype: list[VdiskDevicesModifyItem]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this VdiskDevicesModify.


        :param item: The item of this VdiskDevicesModify.  # noqa: E501
        :type: list[VdiskDevicesModifyItem]
        """
        if self._configuration.client_side_validation and item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501

        self._item = item

    @property
    def common_property(self):
        """Gets the common_property of this VdiskDevicesModify.  # noqa: E501

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :return: The common_property of this VdiskDevicesModify.  # noqa: E501
        :rtype: list[KeyValuePairModify]
        """
        return self._common_property

    @common_property.setter
    def common_property(self, common_property):
        """Sets the common_property of this VdiskDevicesModify.

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :param common_property: The common_property of this VdiskDevicesModify.  # noqa: E501
        :type: list[KeyValuePairModify]
        """

        self._common_property = common_property

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
        if issubclass(VdiskDevicesModify, dict):
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
        if not isinstance(other, VdiskDevicesModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskDevicesModify):
            return True

        return self.to_dict() != other.to_dict()
