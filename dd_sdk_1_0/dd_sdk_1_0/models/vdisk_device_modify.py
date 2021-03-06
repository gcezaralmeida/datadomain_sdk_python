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


class VdiskDeviceModify(object):
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
        'static_image_guid': 'str',
        'state': 'VdiskDeviceState',
        '_property': 'list[KeyValuePairModify]'
    }

    attribute_map = {
        'static_image_guid': 'static_image_guid',
        'state': 'state',
        '_property': 'property'
    }

    def __init__(self, static_image_guid=None, state=None, _property=None, _configuration=None):  # noqa: E501
        """VdiskDeviceModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._static_image_guid = None
        self._state = None
        self.__property = None
        self.discriminator = None

        if static_image_guid is not None:
            self.static_image_guid = static_image_guid
        if state is not None:
            self.state = state
        if _property is not None:
            self._property = _property

    @property
    def static_image_guid(self):
        """Gets the static_image_guid of this VdiskDeviceModify.  # noqa: E501


        :return: The static_image_guid of this VdiskDeviceModify.  # noqa: E501
        :rtype: str
        """
        return self._static_image_guid

    @static_image_guid.setter
    def static_image_guid(self, static_image_guid):
        """Sets the static_image_guid of this VdiskDeviceModify.


        :param static_image_guid: The static_image_guid of this VdiskDeviceModify.  # noqa: E501
        :type: str
        """

        self._static_image_guid = static_image_guid

    @property
    def state(self):
        """Gets the state of this VdiskDeviceModify.  # noqa: E501


        :return: The state of this VdiskDeviceModify.  # noqa: E501
        :rtype: VdiskDeviceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VdiskDeviceModify.


        :param state: The state of this VdiskDeviceModify.  # noqa: E501
        :type: VdiskDeviceState
        """

        self._state = state

    @property
    def _property(self):
        """Gets the _property of this VdiskDeviceModify.  # noqa: E501

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :return: The _property of this VdiskDeviceModify.  # noqa: E501
        :rtype: list[KeyValuePairModify]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VdiskDeviceModify.

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :param _property: The _property of this VdiskDeviceModify.  # noqa: E501
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
        if issubclass(VdiskDeviceModify, dict):
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
        if not isinstance(other, VdiskDeviceModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskDeviceModify):
            return True

        return self.to_dict() != other.to_dict()
