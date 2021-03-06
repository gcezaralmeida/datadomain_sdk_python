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


class SupportSettingInputs(object):
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
        'operation': 'SupportOps',
        'notification_method': 'NotificationTypes',
        'gateway_details': 'EsrsGateway'
    }

    attribute_map = {
        'operation': 'operation',
        'notification_method': 'notification_method',
        'gateway_details': 'gateway_details'
    }

    def __init__(self, operation=None, notification_method=None, gateway_details=None, _configuration=None):  # noqa: E501
        """SupportSettingInputs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation = None
        self._notification_method = None
        self._gateway_details = None
        self.discriminator = None

        self.operation = operation
        if notification_method is not None:
            self.notification_method = notification_method
        if gateway_details is not None:
            self.gateway_details = gateway_details

    @property
    def operation(self):
        """Gets the operation of this SupportSettingInputs.  # noqa: E501


        :return: The operation of this SupportSettingInputs.  # noqa: E501
        :rtype: SupportOps
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this SupportSettingInputs.


        :param operation: The operation of this SupportSettingInputs.  # noqa: E501
        :type: SupportOps
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def notification_method(self):
        """Gets the notification_method of this SupportSettingInputs.  # noqa: E501


        :return: The notification_method of this SupportSettingInputs.  # noqa: E501
        :rtype: NotificationTypes
        """
        return self._notification_method

    @notification_method.setter
    def notification_method(self, notification_method):
        """Sets the notification_method of this SupportSettingInputs.


        :param notification_method: The notification_method of this SupportSettingInputs.  # noqa: E501
        :type: NotificationTypes
        """

        self._notification_method = notification_method

    @property
    def gateway_details(self):
        """Gets the gateway_details of this SupportSettingInputs.  # noqa: E501


        :return: The gateway_details of this SupportSettingInputs.  # noqa: E501
        :rtype: EsrsGateway
        """
        return self._gateway_details

    @gateway_details.setter
    def gateway_details(self, gateway_details):
        """Sets the gateway_details of this SupportSettingInputs.


        :param gateway_details: The gateway_details of this SupportSettingInputs.  # noqa: E501
        :type: EsrsGateway
        """

        self._gateway_details = gateway_details

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
        if issubclass(SupportSettingInputs, dict):
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
        if not isinstance(other, SupportSettingInputs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportSettingInputs):
            return True

        return self.to_dict() != other.to_dict()
