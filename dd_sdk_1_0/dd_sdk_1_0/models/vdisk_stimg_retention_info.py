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


class VdiskStimgRetentionInfo(object):
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
        'mode': 'str',
        'enable': 'str',
        'state': 'str',
        'expiration_date': 'int'
    }

    attribute_map = {
        'mode': 'mode',
        'enable': 'enable',
        'state': 'state',
        'expiration_date': 'expiration_date'
    }

    def __init__(self, mode=None, enable=None, state=None, expiration_date=None, _configuration=None):  # noqa: E501
        """VdiskStimgRetentionInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mode = None
        self._enable = None
        self._state = None
        self._expiration_date = None
        self.discriminator = None

        self.mode = mode
        self.enable = enable
        self.state = state
        self.expiration_date = expiration_date

    @property
    def mode(self):
        """Gets the mode of this VdiskStimgRetentionInfo.  # noqa: E501


        :return: The mode of this VdiskStimgRetentionInfo.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this VdiskStimgRetentionInfo.


        :param mode: The mode of this VdiskStimgRetentionInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def enable(self):
        """Gets the enable of this VdiskStimgRetentionInfo.  # noqa: E501


        :return: The enable of this VdiskStimgRetentionInfo.  # noqa: E501
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this VdiskStimgRetentionInfo.


        :param enable: The enable of this VdiskStimgRetentionInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and enable is None:
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def state(self):
        """Gets the state of this VdiskStimgRetentionInfo.  # noqa: E501


        :return: The state of this VdiskStimgRetentionInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VdiskStimgRetentionInfo.


        :param state: The state of this VdiskStimgRetentionInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def expiration_date(self):
        """Gets the expiration_date of this VdiskStimgRetentionInfo.  # noqa: E501


        :return: The expiration_date of this VdiskStimgRetentionInfo.  # noqa: E501
        :rtype: int
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this VdiskStimgRetentionInfo.


        :param expiration_date: The expiration_date of this VdiskStimgRetentionInfo.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                expiration_date is not None and expiration_date < 0):  # noqa: E501
            raise ValueError("Invalid value for `expiration_date`, must be a value greater than or equal to `0`")  # noqa: E501

        self._expiration_date = expiration_date

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
        if issubclass(VdiskStimgRetentionInfo, dict):
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
        if not isinstance(other, VdiskStimgRetentionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskStimgRetentionInfo):
            return True

        return self.to_dict() != other.to_dict()
