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


class SettingsInfo20(object):
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
        'admin_email': 'str',
        'admin_host': 'str',
        'location': 'str',
        'mail_server': 'str',
        'timezone': 'str',
        'supported_time_zones': 'list[str]',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'admin_email': 'admin_email',
        'admin_host': 'admin_host',
        'location': 'location',
        'mail_server': 'mail_server',
        'timezone': 'timezone',
        'supported_time_zones': 'supported_time_zones',
        'link': 'link'
    }

    def __init__(self, admin_email=None, admin_host=None, location=None, mail_server=None, timezone=None, supported_time_zones=None, link=None, _configuration=None):  # noqa: E501
        """SettingsInfo20 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin_email = None
        self._admin_host = None
        self._location = None
        self._mail_server = None
        self._timezone = None
        self._supported_time_zones = None
        self._link = None
        self.discriminator = None

        self.admin_email = admin_email
        if admin_host is not None:
            self.admin_host = admin_host
        if location is not None:
            self.location = location
        if mail_server is not None:
            self.mail_server = mail_server
        if timezone is not None:
            self.timezone = timezone
        if supported_time_zones is not None:
            self.supported_time_zones = supported_time_zones
        if link is not None:
            self.link = link

    @property
    def admin_email(self):
        """Gets the admin_email of this SettingsInfo20.  # noqa: E501


        :return: The admin_email of this SettingsInfo20.  # noqa: E501
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this SettingsInfo20.


        :param admin_email: The admin_email of this SettingsInfo20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and admin_email is None:
            raise ValueError("Invalid value for `admin_email`, must not be `None`")  # noqa: E501

        self._admin_email = admin_email

    @property
    def admin_host(self):
        """Gets the admin_host of this SettingsInfo20.  # noqa: E501


        :return: The admin_host of this SettingsInfo20.  # noqa: E501
        :rtype: str
        """
        return self._admin_host

    @admin_host.setter
    def admin_host(self, admin_host):
        """Sets the admin_host of this SettingsInfo20.


        :param admin_host: The admin_host of this SettingsInfo20.  # noqa: E501
        :type: str
        """

        self._admin_host = admin_host

    @property
    def location(self):
        """Gets the location of this SettingsInfo20.  # noqa: E501


        :return: The location of this SettingsInfo20.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SettingsInfo20.


        :param location: The location of this SettingsInfo20.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def mail_server(self):
        """Gets the mail_server of this SettingsInfo20.  # noqa: E501


        :return: The mail_server of this SettingsInfo20.  # noqa: E501
        :rtype: str
        """
        return self._mail_server

    @mail_server.setter
    def mail_server(self, mail_server):
        """Sets the mail_server of this SettingsInfo20.


        :param mail_server: The mail_server of this SettingsInfo20.  # noqa: E501
        :type: str
        """

        self._mail_server = mail_server

    @property
    def timezone(self):
        """Gets the timezone of this SettingsInfo20.  # noqa: E501


        :return: The timezone of this SettingsInfo20.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SettingsInfo20.


        :param timezone: The timezone of this SettingsInfo20.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def supported_time_zones(self):
        """Gets the supported_time_zones of this SettingsInfo20.  # noqa: E501


        :return: The supported_time_zones of this SettingsInfo20.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_time_zones

    @supported_time_zones.setter
    def supported_time_zones(self, supported_time_zones):
        """Sets the supported_time_zones of this SettingsInfo20.


        :param supported_time_zones: The supported_time_zones of this SettingsInfo20.  # noqa: E501
        :type: list[str]
        """

        self._supported_time_zones = supported_time_zones

    @property
    def link(self):
        """Gets the link of this SettingsInfo20.  # noqa: E501


        :return: The link of this SettingsInfo20.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SettingsInfo20.


        :param link: The link of this SettingsInfo20.  # noqa: E501
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
        if issubclass(SettingsInfo20, dict):
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
        if not isinstance(other, SettingsInfo20):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsInfo20):
            return True

        return self.to_dict() != other.to_dict()
