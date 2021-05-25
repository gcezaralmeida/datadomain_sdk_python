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


class MdtagServiceInfo(object):
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
        'admin_state': 'MdtagAdminState',
        'process_state': 'MdtagProcessState'
    }

    attribute_map = {
        'admin_state': 'admin_state',
        'process_state': 'process_state'
    }

    def __init__(self, admin_state=None, process_state=None, _configuration=None):  # noqa: E501
        """MdtagServiceInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin_state = None
        self._process_state = None
        self.discriminator = None

        self.admin_state = admin_state
        self.process_state = process_state

    @property
    def admin_state(self):
        """Gets the admin_state of this MdtagServiceInfo.  # noqa: E501


        :return: The admin_state of this MdtagServiceInfo.  # noqa: E501
        :rtype: MdtagAdminState
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this MdtagServiceInfo.


        :param admin_state: The admin_state of this MdtagServiceInfo.  # noqa: E501
        :type: MdtagAdminState
        """
        if self._configuration.client_side_validation and admin_state is None:
            raise ValueError("Invalid value for `admin_state`, must not be `None`")  # noqa: E501

        self._admin_state = admin_state

    @property
    def process_state(self):
        """Gets the process_state of this MdtagServiceInfo.  # noqa: E501


        :return: The process_state of this MdtagServiceInfo.  # noqa: E501
        :rtype: MdtagProcessState
        """
        return self._process_state

    @process_state.setter
    def process_state(self, process_state):
        """Sets the process_state of this MdtagServiceInfo.


        :param process_state: The process_state of this MdtagServiceInfo.  # noqa: E501
        :type: MdtagProcessState
        """
        if self._configuration.client_side_validation and process_state is None:
            raise ValueError("Invalid value for `process_state`, must not be `None`")  # noqa: E501

        self._process_state = process_state

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
        if issubclass(MdtagServiceInfo, dict):
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
        if not isinstance(other, MdtagServiceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MdtagServiceInfo):
            return True

        return self.to_dict() != other.to_dict()
