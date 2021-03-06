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


class VdiskStimgRecallStatus(object):
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
        'bytes_copied': 'int',
        'phase': 'VdiskStimgRecallPhase',
        'is_complete': 'bool'
    }

    attribute_map = {
        'bytes_copied': 'bytes_copied',
        'phase': 'phase',
        'is_complete': 'is_complete'
    }

    def __init__(self, bytes_copied=None, phase=None, is_complete=None, _configuration=None):  # noqa: E501
        """VdiskStimgRecallStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bytes_copied = None
        self._phase = None
        self._is_complete = None
        self.discriminator = None

        self.bytes_copied = bytes_copied
        if phase is not None:
            self.phase = phase
        self.is_complete = is_complete

    @property
    def bytes_copied(self):
        """Gets the bytes_copied of this VdiskStimgRecallStatus.  # noqa: E501


        :return: The bytes_copied of this VdiskStimgRecallStatus.  # noqa: E501
        :rtype: int
        """
        return self._bytes_copied

    @bytes_copied.setter
    def bytes_copied(self, bytes_copied):
        """Sets the bytes_copied of this VdiskStimgRecallStatus.


        :param bytes_copied: The bytes_copied of this VdiskStimgRecallStatus.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and bytes_copied is None:
            raise ValueError("Invalid value for `bytes_copied`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bytes_copied is not None and bytes_copied < 0):  # noqa: E501
            raise ValueError("Invalid value for `bytes_copied`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bytes_copied = bytes_copied

    @property
    def phase(self):
        """Gets the phase of this VdiskStimgRecallStatus.  # noqa: E501


        :return: The phase of this VdiskStimgRecallStatus.  # noqa: E501
        :rtype: VdiskStimgRecallPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this VdiskStimgRecallStatus.


        :param phase: The phase of this VdiskStimgRecallStatus.  # noqa: E501
        :type: VdiskStimgRecallPhase
        """

        self._phase = phase

    @property
    def is_complete(self):
        """Gets the is_complete of this VdiskStimgRecallStatus.  # noqa: E501


        :return: The is_complete of this VdiskStimgRecallStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this VdiskStimgRecallStatus.


        :param is_complete: The is_complete of this VdiskStimgRecallStatus.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_complete is None:
            raise ValueError("Invalid value for `is_complete`, must not be `None`")  # noqa: E501

        self._is_complete = is_complete

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
        if issubclass(VdiskStimgRecallStatus, dict):
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
        if not isinstance(other, VdiskStimgRecallStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskStimgRecallStatus):
            return True

        return self.to_dict() != other.to_dict()
