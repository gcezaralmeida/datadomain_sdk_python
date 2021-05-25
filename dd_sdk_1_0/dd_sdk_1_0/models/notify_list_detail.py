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


class NotifyListDetail(object):
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
        '_property': 'NotifyListProperty',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        '_property': 'property',
        'link': 'link'
    }

    def __init__(self, id=None, name=None, _property=None, link=None, _configuration=None):  # noqa: E501
        """NotifyListDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self.__property = None
        self._link = None
        self.discriminator = None

        self.id = id
        self.name = name
        self._property = _property
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this NotifyListDetail.  # noqa: E501

        urlencoded name  # noqa: E501

        :return: The id of this NotifyListDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotifyListDetail.

        urlencoded name  # noqa: E501

        :param id: The id of this NotifyListDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this NotifyListDetail.  # noqa: E501


        :return: The name of this NotifyListDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotifyListDetail.


        :param name: The name of this NotifyListDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def _property(self):
        """Gets the _property of this NotifyListDetail.  # noqa: E501


        :return: The _property of this NotifyListDetail.  # noqa: E501
        :rtype: NotifyListProperty
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this NotifyListDetail.


        :param _property: The _property of this NotifyListDetail.  # noqa: E501
        :type: NotifyListProperty
        """
        if self._configuration.client_side_validation and _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

    @property
    def link(self):
        """Gets the link of this NotifyListDetail.  # noqa: E501


        :return: The link of this NotifyListDetail.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this NotifyListDetail.


        :param link: The link of this NotifyListDetail.  # noqa: E501
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
        if issubclass(NotifyListDetail, dict):
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
        if not isinstance(other, NotifyListDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotifyListDetail):
            return True

        return self.to_dict() != other.to_dict()
