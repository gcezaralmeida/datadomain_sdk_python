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


class VdiskPoolModify(object):
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
        'name': 'str',
        'user': 'str',
        'tenant_unit': 'str',
        'quota_config': 'QuotaConfig',
        '_property': 'list[KeyValuePairModify]'
    }

    attribute_map = {
        'name': 'name',
        'user': 'user',
        'tenant_unit': 'tenant_unit',
        'quota_config': 'quota_config',
        '_property': 'property'
    }

    def __init__(self, name=None, user=None, tenant_unit=None, quota_config=None, _property=None, _configuration=None):  # noqa: E501
        """VdiskPoolModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._user = None
        self._tenant_unit = None
        self._quota_config = None
        self.__property = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user is not None:
            self.user = user
        if tenant_unit is not None:
            self.tenant_unit = tenant_unit
        if quota_config is not None:
            self.quota_config = quota_config
        if _property is not None:
            self._property = _property

    @property
    def name(self):
        """Gets the name of this VdiskPoolModify.  # noqa: E501

        rename pool name  # noqa: E501

        :return: The name of this VdiskPoolModify.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VdiskPoolModify.

        rename pool name  # noqa: E501

        :param name: The name of this VdiskPoolModify.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user(self):
        """Gets the user of this VdiskPoolModify.  # noqa: E501

        change vdisk user  # noqa: E501

        :return: The user of this VdiskPoolModify.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VdiskPoolModify.

        change vdisk user  # noqa: E501

        :param user: The user of this VdiskPoolModify.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def tenant_unit(self):
        """Gets the tenant_unit of this VdiskPoolModify.  # noqa: E501

        Tenant unit name or \"none\" to reset the tenant unit.  # noqa: E501

        :return: The tenant_unit of this VdiskPoolModify.  # noqa: E501
        :rtype: str
        """
        return self._tenant_unit

    @tenant_unit.setter
    def tenant_unit(self, tenant_unit):
        """Sets the tenant_unit of this VdiskPoolModify.

        Tenant unit name or \"none\" to reset the tenant unit.  # noqa: E501

        :param tenant_unit: The tenant_unit of this VdiskPoolModify.  # noqa: E501
        :type: str
        """

        self._tenant_unit = tenant_unit

    @property
    def quota_config(self):
        """Gets the quota_config of this VdiskPoolModify.  # noqa: E501


        :return: The quota_config of this VdiskPoolModify.  # noqa: E501
        :rtype: QuotaConfig
        """
        return self._quota_config

    @quota_config.setter
    def quota_config(self, quota_config):
        """Sets the quota_config of this VdiskPoolModify.


        :param quota_config: The quota_config of this VdiskPoolModify.  # noqa: E501
        :type: QuotaConfig
        """

        self._quota_config = quota_config

    @property
    def _property(self):
        """Gets the _property of this VdiskPoolModify.  # noqa: E501

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :return: The _property of this VdiskPoolModify.  # noqa: E501
        :rtype: list[KeyValuePairModify]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VdiskPoolModify.

        if value is not set, the property will be deleted. Otherwise, it will be added.  # noqa: E501

        :param _property: The _property of this VdiskPoolModify.  # noqa: E501
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
        if issubclass(VdiskPoolModify, dict):
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
        if not isinstance(other, VdiskPoolModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskPoolModify):
            return True

        return self.to_dict() != other.to_dict()
