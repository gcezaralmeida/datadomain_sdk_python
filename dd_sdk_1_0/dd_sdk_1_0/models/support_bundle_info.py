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


class SupportBundleInfo(object):
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
        'hostname': 'str',
        'size_in_bytes': 'int',
        'time_created_epoch': 'int',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'hostname': 'hostname',
        'size_in_bytes': 'size_in_bytes',
        'time_created_epoch': 'time_created_epoch',
        'link': 'link'
    }

    def __init__(self, id=None, name=None, hostname=None, size_in_bytes=None, time_created_epoch=None, link=None, _configuration=None):  # noqa: E501
        """SupportBundleInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._hostname = None
        self._size_in_bytes = None
        self._time_created_epoch = None
        self._link = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if hostname is not None:
            self.hostname = hostname
        if size_in_bytes is not None:
            self.size_in_bytes = size_in_bytes
        if time_created_epoch is not None:
            self.time_created_epoch = time_created_epoch
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this SupportBundleInfo.  # noqa: E501


        :return: The id of this SupportBundleInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupportBundleInfo.


        :param id: The id of this SupportBundleInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SupportBundleInfo.  # noqa: E501


        :return: The name of this SupportBundleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupportBundleInfo.


        :param name: The name of this SupportBundleInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this SupportBundleInfo.  # noqa: E501


        :return: The hostname of this SupportBundleInfo.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SupportBundleInfo.


        :param hostname: The hostname of this SupportBundleInfo.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def size_in_bytes(self):
        """Gets the size_in_bytes of this SupportBundleInfo.  # noqa: E501


        :return: The size_in_bytes of this SupportBundleInfo.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """Sets the size_in_bytes of this SupportBundleInfo.


        :param size_in_bytes: The size_in_bytes of this SupportBundleInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                size_in_bytes is not None and size_in_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `size_in_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size_in_bytes = size_in_bytes

    @property
    def time_created_epoch(self):
        """Gets the time_created_epoch of this SupportBundleInfo.  # noqa: E501


        :return: The time_created_epoch of this SupportBundleInfo.  # noqa: E501
        :rtype: int
        """
        return self._time_created_epoch

    @time_created_epoch.setter
    def time_created_epoch(self, time_created_epoch):
        """Sets the time_created_epoch of this SupportBundleInfo.


        :param time_created_epoch: The time_created_epoch of this SupportBundleInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                time_created_epoch is not None and time_created_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `time_created_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time_created_epoch = time_created_epoch

    @property
    def link(self):
        """Gets the link of this SupportBundleInfo.  # noqa: E501


        :return: The link of this SupportBundleInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SupportBundleInfo.


        :param link: The link of this SupportBundleInfo.  # noqa: E501
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
        if issubclass(SupportBundleInfo, dict):
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
        if not isinstance(other, SupportBundleInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportBundleInfo):
            return True

        return self.to_dict() != other.to_dict()
