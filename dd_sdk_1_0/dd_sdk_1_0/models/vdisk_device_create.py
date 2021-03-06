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


class VdiskDeviceCreate(object):
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
        'count': 'PositiveInt',
        'capacity_in_bytes': 'int',
        'state': 'VdiskDeviceState',
        'sectors': 'int',
        'geometry': 'GeometryConfig',
        'devgrp_guid': 'str',
        '_property': 'list[KeyValuePair]',
        'devgrp_geometry': 'list[VdiskDeviceCreateDeviceGroupGeometry]'
    }

    attribute_map = {
        'count': 'count',
        'capacity_in_bytes': 'capacity_in_bytes',
        'state': 'state',
        'sectors': 'sectors',
        'geometry': 'geometry',
        'devgrp_guid': 'devgrp_guid',
        '_property': 'property',
        'devgrp_geometry': 'devgrp_geometry'
    }

    def __init__(self, count=None, capacity_in_bytes=None, state=None, sectors=None, geometry=None, devgrp_guid=None, _property=None, devgrp_geometry=None, _configuration=None):  # noqa: E501
        """VdiskDeviceCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._capacity_in_bytes = None
        self._state = None
        self._sectors = None
        self._geometry = None
        self._devgrp_guid = None
        self.__property = None
        self._devgrp_geometry = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if capacity_in_bytes is not None:
            self.capacity_in_bytes = capacity_in_bytes
        if state is not None:
            self.state = state
        if sectors is not None:
            self.sectors = sectors
        if geometry is not None:
            self.geometry = geometry
        if devgrp_guid is not None:
            self.devgrp_guid = devgrp_guid
        if _property is not None:
            self._property = _property
        if devgrp_geometry is not None:
            self.devgrp_geometry = devgrp_geometry

    @property
    def count(self):
        """Gets the count of this VdiskDeviceCreate.  # noqa: E501


        :return: The count of this VdiskDeviceCreate.  # noqa: E501
        :rtype: PositiveInt
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VdiskDeviceCreate.


        :param count: The count of this VdiskDeviceCreate.  # noqa: E501
        :type: PositiveInt
        """

        self._count = count

    @property
    def capacity_in_bytes(self):
        """Gets the capacity_in_bytes of this VdiskDeviceCreate.  # noqa: E501


        :return: The capacity_in_bytes of this VdiskDeviceCreate.  # noqa: E501
        :rtype: int
        """
        return self._capacity_in_bytes

    @capacity_in_bytes.setter
    def capacity_in_bytes(self, capacity_in_bytes):
        """Sets the capacity_in_bytes of this VdiskDeviceCreate.


        :param capacity_in_bytes: The capacity_in_bytes of this VdiskDeviceCreate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                capacity_in_bytes is not None and capacity_in_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `capacity_in_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity_in_bytes = capacity_in_bytes

    @property
    def state(self):
        """Gets the state of this VdiskDeviceCreate.  # noqa: E501


        :return: The state of this VdiskDeviceCreate.  # noqa: E501
        :rtype: VdiskDeviceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VdiskDeviceCreate.


        :param state: The state of this VdiskDeviceCreate.  # noqa: E501
        :type: VdiskDeviceState
        """

        self._state = state

    @property
    def sectors(self):
        """Gets the sectors of this VdiskDeviceCreate.  # noqa: E501


        :return: The sectors of this VdiskDeviceCreate.  # noqa: E501
        :rtype: int
        """
        return self._sectors

    @sectors.setter
    def sectors(self, sectors):
        """Sets the sectors of this VdiskDeviceCreate.


        :param sectors: The sectors of this VdiskDeviceCreate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                sectors is not None and sectors < 0):  # noqa: E501
            raise ValueError("Invalid value for `sectors`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sectors = sectors

    @property
    def geometry(self):
        """Gets the geometry of this VdiskDeviceCreate.  # noqa: E501


        :return: The geometry of this VdiskDeviceCreate.  # noqa: E501
        :rtype: GeometryConfig
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this VdiskDeviceCreate.


        :param geometry: The geometry of this VdiskDeviceCreate.  # noqa: E501
        :type: GeometryConfig
        """

        self._geometry = geometry

    @property
    def devgrp_guid(self):
        """Gets the devgrp_guid of this VdiskDeviceCreate.  # noqa: E501

        GUID  # noqa: E501

        :return: The devgrp_guid of this VdiskDeviceCreate.  # noqa: E501
        :rtype: str
        """
        return self._devgrp_guid

    @devgrp_guid.setter
    def devgrp_guid(self, devgrp_guid):
        """Sets the devgrp_guid of this VdiskDeviceCreate.

        GUID  # noqa: E501

        :param devgrp_guid: The devgrp_guid of this VdiskDeviceCreate.  # noqa: E501
        :type: str
        """

        self._devgrp_guid = devgrp_guid

    @property
    def _property(self):
        """Gets the _property of this VdiskDeviceCreate.  # noqa: E501


        :return: The _property of this VdiskDeviceCreate.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VdiskDeviceCreate.


        :param _property: The _property of this VdiskDeviceCreate.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self.__property = _property

    @property
    def devgrp_geometry(self):
        """Gets the devgrp_geometry of this VdiskDeviceCreate.  # noqa: E501

        geometry  # noqa: E501

        :return: The devgrp_geometry of this VdiskDeviceCreate.  # noqa: E501
        :rtype: list[VdiskDeviceCreateDeviceGroupGeometry]
        """
        return self._devgrp_geometry

    @devgrp_geometry.setter
    def devgrp_geometry(self, devgrp_geometry):
        """Sets the devgrp_geometry of this VdiskDeviceCreate.

        geometry  # noqa: E501

        :param devgrp_geometry: The devgrp_geometry of this VdiskDeviceCreate.  # noqa: E501
        :type: list[VdiskDeviceCreateDeviceGroupGeometry]
        """

        self._devgrp_geometry = devgrp_geometry

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
        if issubclass(VdiskDeviceCreate, dict):
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
        if not isinstance(other, VdiskDeviceCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskDeviceCreate):
            return True

        return self.to_dict() != other.to_dict()
