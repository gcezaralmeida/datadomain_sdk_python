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


class VdiskStimgsModifyItem(object):
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
        'guid': 'str',
        'device_wwnn': 'str',
        '_property': 'list[KeyValuePairModify]'
    }

    attribute_map = {
        'guid': 'guid',
        'device_wwnn': 'device_wwnn',
        '_property': 'property'
    }

    def __init__(self, guid=None, device_wwnn=None, _property=None, _configuration=None):  # noqa: E501
        """VdiskStimgsModifyItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._device_wwnn = None
        self.__property = None
        self.discriminator = None

        self.guid = guid
        if device_wwnn is not None:
            self.device_wwnn = device_wwnn
        if _property is not None:
            self._property = _property

    @property
    def guid(self):
        """Gets the guid of this VdiskStimgsModifyItem.  # noqa: E501


        :return: The guid of this VdiskStimgsModifyItem.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this VdiskStimgsModifyItem.


        :param guid: The guid of this VdiskStimgsModifyItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501

        self._guid = guid

    @property
    def device_wwnn(self):
        """Gets the device_wwnn of this VdiskStimgsModifyItem.  # noqa: E501

        Attach this static image to the object, specified by guid or wwnn.  # noqa: E501

        :return: The device_wwnn of this VdiskStimgsModifyItem.  # noqa: E501
        :rtype: str
        """
        return self._device_wwnn

    @device_wwnn.setter
    def device_wwnn(self, device_wwnn):
        """Sets the device_wwnn of this VdiskStimgsModifyItem.

        Attach this static image to the object, specified by guid or wwnn.  # noqa: E501

        :param device_wwnn: The device_wwnn of this VdiskStimgsModifyItem.  # noqa: E501
        :type: str
        """

        self._device_wwnn = device_wwnn

    @property
    def _property(self):
        """Gets the _property of this VdiskStimgsModifyItem.  # noqa: E501

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :return: The _property of this VdiskStimgsModifyItem.  # noqa: E501
        :rtype: list[KeyValuePairModify]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VdiskStimgsModifyItem.

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :param _property: The _property of this VdiskStimgsModifyItem.  # noqa: E501
        :type: list[KeyValuePairModify]
        """

        self.__property = _property

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
        if issubclass(VdiskStimgsModifyItem, dict):
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
        if not isinstance(other, VdiskStimgsModifyItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskStimgsModifyItem):
            return True

        return self.to_dict() != other.to_dict()
