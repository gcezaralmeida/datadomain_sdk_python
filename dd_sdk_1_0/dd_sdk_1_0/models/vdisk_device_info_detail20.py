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


class VdiskDeviceInfoDetail20(object):
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
        'id': 'str',
        'guid': 'str',
        'wwnn': 'str',
        'name': 'str',
        'capacity_in_bytes': 'int',
        'state': 'str',
        'geometry': 'GeometryConfig',
        'devgrp_name': 'str',
        'devgrp_guid': 'str',
        'pool_name': 'str',
        'pool_guid': 'str',
        '_property': 'list[KeyValuePair]',
        'lock_info': 'VdiskLockInfo',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'id': 'id',
        'guid': 'guid',
        'wwnn': 'wwnn',
        'name': 'name',
        'capacity_in_bytes': 'capacity_in_bytes',
        'state': 'state',
        'geometry': 'geometry',
        'devgrp_name': 'devgrp_name',
        'devgrp_guid': 'devgrp_guid',
        'pool_name': 'pool_name',
        'pool_guid': 'pool_guid',
        '_property': 'property',
        'lock_info': 'lock_info',
        'link': 'link'
    }

    def __init__(self, id=None, guid=None, wwnn=None, name=None, capacity_in_bytes=None, state=None, geometry=None, devgrp_name=None, devgrp_guid=None, pool_name=None, pool_guid=None, _property=None, lock_info=None, link=None, _configuration=None):  # noqa: E501
        """VdiskDeviceInfoDetail20 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._guid = None
        self._wwnn = None
        self._name = None
        self._capacity_in_bytes = None
        self._state = None
        self._geometry = None
        self._devgrp_name = None
        self._devgrp_guid = None
        self._pool_name = None
        self._pool_guid = None
        self.__property = None
        self._lock_info = None
        self._link = None
        self.discriminator = None

        self.id = id
        self.guid = guid
        self.wwnn = wwnn
        if name is not None:
            self.name = name
        if capacity_in_bytes is not None:
            self.capacity_in_bytes = capacity_in_bytes
        if state is not None:
            self.state = state
        if geometry is not None:
            self.geometry = geometry
        if devgrp_name is not None:
            self.devgrp_name = devgrp_name
        self.devgrp_guid = devgrp_guid
        if pool_name is not None:
            self.pool_name = pool_name
        self.pool_guid = pool_guid
        if _property is not None:
            self._property = _property
        if lock_info is not None:
            self.lock_info = lock_info
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this VdiskDeviceInfoDetail20.  # noqa: E501

        urlencoded GUID  # noqa: E501

        :return: The id of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VdiskDeviceInfoDetail20.

        urlencoded GUID  # noqa: E501

        :param id: The id of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def guid(self):
        """Gets the guid of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The guid of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this VdiskDeviceInfoDetail20.


        :param guid: The guid of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501

        self._guid = guid

    @property
    def wwnn(self):
        """Gets the wwnn of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The wwnn of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """Sets the wwnn of this VdiskDeviceInfoDetail20.


        :param wwnn: The wwnn of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and wwnn is None:
            raise ValueError("Invalid value for `wwnn`, must not be `None`")  # noqa: E501

        self._wwnn = wwnn

    @property
    def name(self):
        """Gets the name of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The name of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VdiskDeviceInfoDetail20.


        :param name: The name of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def capacity_in_bytes(self):
        """Gets the capacity_in_bytes of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The capacity_in_bytes of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: int
        """
        return self._capacity_in_bytes

    @capacity_in_bytes.setter
    def capacity_in_bytes(self, capacity_in_bytes):
        """Sets the capacity_in_bytes of this VdiskDeviceInfoDetail20.


        :param capacity_in_bytes: The capacity_in_bytes of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                capacity_in_bytes is not None and capacity_in_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `capacity_in_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity_in_bytes = capacity_in_bytes

    @property
    def state(self):
        """Gets the state of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The state of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VdiskDeviceInfoDetail20.


        :param state: The state of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def geometry(self):
        """Gets the geometry of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The geometry of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: GeometryConfig
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this VdiskDeviceInfoDetail20.


        :param geometry: The geometry of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: GeometryConfig
        """

        self._geometry = geometry

    @property
    def devgrp_name(self):
        """Gets the devgrp_name of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The devgrp_name of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._devgrp_name

    @devgrp_name.setter
    def devgrp_name(self, devgrp_name):
        """Sets the devgrp_name of this VdiskDeviceInfoDetail20.


        :param devgrp_name: The devgrp_name of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """

        self._devgrp_name = devgrp_name

    @property
    def devgrp_guid(self):
        """Gets the devgrp_guid of this VdiskDeviceInfoDetail20.  # noqa: E501

        urlencoded GUID  # noqa: E501

        :return: The devgrp_guid of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._devgrp_guid

    @devgrp_guid.setter
    def devgrp_guid(self, devgrp_guid):
        """Sets the devgrp_guid of this VdiskDeviceInfoDetail20.

        urlencoded GUID  # noqa: E501

        :param devgrp_guid: The devgrp_guid of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and devgrp_guid is None:
            raise ValueError("Invalid value for `devgrp_guid`, must not be `None`")  # noqa: E501

        self._devgrp_guid = devgrp_guid

    @property
    def pool_name(self):
        """Gets the pool_name of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The pool_name of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this VdiskDeviceInfoDetail20.


        :param pool_name: The pool_name of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """

        self._pool_name = pool_name

    @property
    def pool_guid(self):
        """Gets the pool_guid of this VdiskDeviceInfoDetail20.  # noqa: E501

        urlencoded GUID  # noqa: E501

        :return: The pool_guid of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: str
        """
        return self._pool_guid

    @pool_guid.setter
    def pool_guid(self, pool_guid):
        """Sets the pool_guid of this VdiskDeviceInfoDetail20.

        urlencoded GUID  # noqa: E501

        :param pool_guid: The pool_guid of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and pool_guid is None:
            raise ValueError("Invalid value for `pool_guid`, must not be `None`")  # noqa: E501

        self._pool_guid = pool_guid

    @property
    def _property(self):
        """Gets the _property of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The _property of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VdiskDeviceInfoDetail20.


        :param _property: The _property of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self.__property = _property

    @property
    def lock_info(self):
        """Gets the lock_info of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The lock_info of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: VdiskLockInfo
        """
        return self._lock_info

    @lock_info.setter
    def lock_info(self, lock_info):
        """Sets the lock_info of this VdiskDeviceInfoDetail20.


        :param lock_info: The lock_info of this VdiskDeviceInfoDetail20.  # noqa: E501
        :type: VdiskLockInfo
        """

        self._lock_info = lock_info

    @property
    def link(self):
        """Gets the link of this VdiskDeviceInfoDetail20.  # noqa: E501


        :return: The link of this VdiskDeviceInfoDetail20.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this VdiskDeviceInfoDetail20.


        :param link: The link of this VdiskDeviceInfoDetail20.  # noqa: E501
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
        if issubclass(VdiskDeviceInfoDetail20, dict):
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
        if not isinstance(other, VdiskDeviceInfoDetail20):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskDeviceInfoDetail20):
            return True

        return self.to_dict() != other.to_dict()
