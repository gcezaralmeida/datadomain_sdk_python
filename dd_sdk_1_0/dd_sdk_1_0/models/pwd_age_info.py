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


class PwdAgeInfo(object):
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
        'last_change_days': 'int',
        'min_days_between_change': 'int',
        'max_days_between_change': 'int',
        'warn_days_before_expire': 'int',
        'disable_days_after_expire': 'int',
        'disable_date_days': 'int',
        'acct_status': 'int'
    }

    attribute_map = {
        'last_change_days': 'last_change_days',
        'min_days_between_change': 'min_days_between_change',
        'max_days_between_change': 'max_days_between_change',
        'warn_days_before_expire': 'warn_days_before_expire',
        'disable_days_after_expire': 'disable_days_after_expire',
        'disable_date_days': 'disable_date_days',
        'acct_status': 'acct_status'
    }

    def __init__(self, last_change_days=None, min_days_between_change=None, max_days_between_change=None, warn_days_before_expire=None, disable_days_after_expire=None, disable_date_days=None, acct_status=None, _configuration=None):  # noqa: E501
        """PwdAgeInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_change_days = None
        self._min_days_between_change = None
        self._max_days_between_change = None
        self._warn_days_before_expire = None
        self._disable_days_after_expire = None
        self._disable_date_days = None
        self._acct_status = None
        self.discriminator = None

        if last_change_days is not None:
            self.last_change_days = last_change_days
        if min_days_between_change is not None:
            self.min_days_between_change = min_days_between_change
        if max_days_between_change is not None:
            self.max_days_between_change = max_days_between_change
        if warn_days_before_expire is not None:
            self.warn_days_before_expire = warn_days_before_expire
        if disable_days_after_expire is not None:
            self.disable_days_after_expire = disable_days_after_expire
        if disable_date_days is not None:
            self.disable_date_days = disable_date_days
        if acct_status is not None:
            self.acct_status = acct_status

    @property
    def last_change_days(self):
        """Gets the last_change_days of this PwdAgeInfo.  # noqa: E501


        :return: The last_change_days of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_change_days

    @last_change_days.setter
    def last_change_days(self, last_change_days):
        """Sets the last_change_days of this PwdAgeInfo.


        :param last_change_days: The last_change_days of this PwdAgeInfo.  # noqa: E501
        :type: int
        """

        self._last_change_days = last_change_days

    @property
    def min_days_between_change(self):
        """Gets the min_days_between_change of this PwdAgeInfo.  # noqa: E501


        :return: The min_days_between_change of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._min_days_between_change

    @min_days_between_change.setter
    def min_days_between_change(self, min_days_between_change):
        """Sets the min_days_between_change of this PwdAgeInfo.


        :param min_days_between_change: The min_days_between_change of this PwdAgeInfo.  # noqa: E501
        :type: int
        """

        self._min_days_between_change = min_days_between_change

    @property
    def max_days_between_change(self):
        """Gets the max_days_between_change of this PwdAgeInfo.  # noqa: E501


        :return: The max_days_between_change of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_days_between_change

    @max_days_between_change.setter
    def max_days_between_change(self, max_days_between_change):
        """Sets the max_days_between_change of this PwdAgeInfo.


        :param max_days_between_change: The max_days_between_change of this PwdAgeInfo.  # noqa: E501
        :type: int
        """

        self._max_days_between_change = max_days_between_change

    @property
    def warn_days_before_expire(self):
        """Gets the warn_days_before_expire of this PwdAgeInfo.  # noqa: E501


        :return: The warn_days_before_expire of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._warn_days_before_expire

    @warn_days_before_expire.setter
    def warn_days_before_expire(self, warn_days_before_expire):
        """Sets the warn_days_before_expire of this PwdAgeInfo.


        :param warn_days_before_expire: The warn_days_before_expire of this PwdAgeInfo.  # noqa: E501
        :type: int
        """

        self._warn_days_before_expire = warn_days_before_expire

    @property
    def disable_days_after_expire(self):
        """Gets the disable_days_after_expire of this PwdAgeInfo.  # noqa: E501


        :return: The disable_days_after_expire of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._disable_days_after_expire

    @disable_days_after_expire.setter
    def disable_days_after_expire(self, disable_days_after_expire):
        """Sets the disable_days_after_expire of this PwdAgeInfo.


        :param disable_days_after_expire: The disable_days_after_expire of this PwdAgeInfo.  # noqa: E501
        :type: int
        """

        self._disable_days_after_expire = disable_days_after_expire

    @property
    def disable_date_days(self):
        """Gets the disable_date_days of this PwdAgeInfo.  # noqa: E501


        :return: The disable_date_days of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._disable_date_days

    @disable_date_days.setter
    def disable_date_days(self, disable_date_days):
        """Sets the disable_date_days of this PwdAgeInfo.


        :param disable_date_days: The disable_date_days of this PwdAgeInfo.  # noqa: E501
        :type: int
        """

        self._disable_date_days = disable_date_days

    @property
    def acct_status(self):
        """Gets the acct_status of this PwdAgeInfo.  # noqa: E501


        :return: The acct_status of this PwdAgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._acct_status

    @acct_status.setter
    def acct_status(self, acct_status):
        """Sets the acct_status of this PwdAgeInfo.


        :param acct_status: The acct_status of this PwdAgeInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                acct_status is not None and acct_status < 0):  # noqa: E501
            raise ValueError("Invalid value for `acct_status`, must be a value greater than or equal to `0`")  # noqa: E501

        self._acct_status = acct_status

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
        if issubclass(PwdAgeInfo, dict):
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
        if not isinstance(other, PwdAgeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PwdAgeInfo):
            return True

        return self.to_dict() != other.to_dict()