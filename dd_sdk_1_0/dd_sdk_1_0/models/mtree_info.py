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


class MtreeInfo(object):
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
        'data_access_ip': 'str',
        'link': 'RestLinkRep'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'data_access_ip': 'data_access_ip',
        'link': 'link'
    }

    def __init__(self, id=None, name=None, data_access_ip=None, link=None, _configuration=None):  # noqa: E501
        """MtreeInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._data_access_ip = None
        self._link = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if data_access_ip is not None:
            self.data_access_ip = data_access_ip
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this MtreeInfo.  # noqa: E501


        :return: The id of this MtreeInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MtreeInfo.


        :param id: The id of this MtreeInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this MtreeInfo.  # noqa: E501


        :return: The name of this MtreeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MtreeInfo.


        :param name: The name of this MtreeInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_access_ip(self):
        """Gets the data_access_ip of this MtreeInfo.  # noqa: E501


        :return: The data_access_ip of this MtreeInfo.  # noqa: E501
        :rtype: str
        """
        return self._data_access_ip

    @data_access_ip.setter
    def data_access_ip(self, data_access_ip):
        """Sets the data_access_ip of this MtreeInfo.


        :param data_access_ip: The data_access_ip of this MtreeInfo.  # noqa: E501
        :type: str
        """

        self._data_access_ip = data_access_ip

    @property
    def link(self):
        """Gets the link of this MtreeInfo.  # noqa: E501


        :return: The link of this MtreeInfo.  # noqa: E501
        :rtype: RestLinkRep
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this MtreeInfo.


        :param link: The link of this MtreeInfo.  # noqa: E501
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
        if issubclass(MtreeInfo, dict):
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
        if not isinstance(other, MtreeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MtreeInfo):
            return True

        return self.to_dict() != other.to_dict()
