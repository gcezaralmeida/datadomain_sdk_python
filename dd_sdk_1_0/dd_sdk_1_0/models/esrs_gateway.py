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


class EsrsGateway(object):
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
        'gateway': 'str',
        'serial_number': 'str',
        'device_key': 'str',
        'device_type': 'str',
        'transfer_type': 'str'
    }

    attribute_map = {
        'gateway': 'gateway',
        'serial_number': 'serial_number',
        'device_key': 'device_key',
        'device_type': 'device_type',
        'transfer_type': 'transfer_type'
    }

    def __init__(self, gateway=None, serial_number=None, device_key=None, device_type=None, transfer_type=None, _configuration=None):  # noqa: E501
        """EsrsGateway - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._gateway = None
        self._serial_number = None
        self._device_key = None
        self._device_type = None
        self._transfer_type = None
        self.discriminator = None

        if gateway is not None:
            self.gateway = gateway
        if serial_number is not None:
            self.serial_number = serial_number
        if device_key is not None:
            self.device_key = device_key
        if device_type is not None:
            self.device_type = device_type
        if transfer_type is not None:
            self.transfer_type = transfer_type

    @property
    def gateway(self):
        """Gets the gateway of this EsrsGateway.  # noqa: E501


        :return: The gateway of this EsrsGateway.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this EsrsGateway.


        :param gateway: The gateway of this EsrsGateway.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def serial_number(self):
        """Gets the serial_number of this EsrsGateway.  # noqa: E501


        :return: The serial_number of this EsrsGateway.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this EsrsGateway.


        :param serial_number: The serial_number of this EsrsGateway.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def device_key(self):
        """Gets the device_key of this EsrsGateway.  # noqa: E501


        :return: The device_key of this EsrsGateway.  # noqa: E501
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """Sets the device_key of this EsrsGateway.


        :param device_key: The device_key of this EsrsGateway.  # noqa: E501
        :type: str
        """

        self._device_key = device_key

    @property
    def device_type(self):
        """Gets the device_type of this EsrsGateway.  # noqa: E501


        :return: The device_type of this EsrsGateway.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this EsrsGateway.


        :param device_type: The device_type of this EsrsGateway.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def transfer_type(self):
        """Gets the transfer_type of this EsrsGateway.  # noqa: E501


        :return: The transfer_type of this EsrsGateway.  # noqa: E501
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        """Sets the transfer_type of this EsrsGateway.


        :param transfer_type: The transfer_type of this EsrsGateway.  # noqa: E501
        :type: str
        """

        self._transfer_type = transfer_type

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
        if issubclass(EsrsGateway, dict):
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
        if not isinstance(other, EsrsGateway):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EsrsGateway):
            return True

        return self.to_dict() != other.to_dict()
