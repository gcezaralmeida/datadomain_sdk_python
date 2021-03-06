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


class TenantInfo(object):
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
        'name': 'str',
        'uuid': 'str',
        'number_of_tenant_units': 'int',
        'pre_comp_bytes': 'int',
        'link': 'RestLinkRep'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'uuid': 'uuid',
        'number_of_tenant_units': 'number_of_tenant_units',
        'pre_comp_bytes': 'pre_comp_bytes',
        'link': 'link'
    }

    def __init__(self, id=None, name=None, uuid=None, number_of_tenant_units=None, pre_comp_bytes=None, link=None, _configuration=None):  # noqa: E501
        """TenantInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._uuid = None
        self._number_of_tenant_units = None
        self._pre_comp_bytes = None
        self._link = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.uuid = uuid
        if number_of_tenant_units is not None:
            self.number_of_tenant_units = number_of_tenant_units
        if pre_comp_bytes is not None:
            self.pre_comp_bytes = pre_comp_bytes
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this TenantInfo.  # noqa: E501

        url-encoded name  # noqa: E501

        :return: The id of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantInfo.

        url-encoded name  # noqa: E501

        :param id: The id of this TenantInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TenantInfo.  # noqa: E501


        :return: The name of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantInfo.


        :param name: The name of this TenantInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TenantInfo.  # noqa: E501


        :return: The uuid of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TenantInfo.


        :param uuid: The uuid of this TenantInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def number_of_tenant_units(self):
        """Gets the number_of_tenant_units of this TenantInfo.  # noqa: E501


        :return: The number_of_tenant_units of this TenantInfo.  # noqa: E501
        :rtype: int
        """
        return self._number_of_tenant_units

    @number_of_tenant_units.setter
    def number_of_tenant_units(self, number_of_tenant_units):
        """Sets the number_of_tenant_units of this TenantInfo.


        :param number_of_tenant_units: The number_of_tenant_units of this TenantInfo.  # noqa: E501
        :type: int
        """

        self._number_of_tenant_units = number_of_tenant_units

    @property
    def pre_comp_bytes(self):
        """Gets the pre_comp_bytes of this TenantInfo.  # noqa: E501


        :return: The pre_comp_bytes of this TenantInfo.  # noqa: E501
        :rtype: int
        """
        return self._pre_comp_bytes

    @pre_comp_bytes.setter
    def pre_comp_bytes(self, pre_comp_bytes):
        """Sets the pre_comp_bytes of this TenantInfo.


        :param pre_comp_bytes: The pre_comp_bytes of this TenantInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                pre_comp_bytes is not None and pre_comp_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `pre_comp_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._pre_comp_bytes = pre_comp_bytes

    @property
    def link(self):
        """Gets the link of this TenantInfo.  # noqa: E501


        :return: The link of this TenantInfo.  # noqa: E501
        :rtype: RestLinkRep
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TenantInfo.


        :param link: The link of this TenantInfo.  # noqa: E501
        :type: RestLinkRep
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
        if issubclass(TenantInfo, dict):
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
        if not isinstance(other, TenantInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantInfo):
            return True

        return self.to_dict() != other.to_dict()
