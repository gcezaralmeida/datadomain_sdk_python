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


class DataMovementInfo(object):
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
        'operation_info': 'str',
        'throttle': 'int',
        'schedule': 'DataMovementSchedule',
        'status': 'DataMovementStatusInfo',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'operation_info': 'operation_info',
        'throttle': 'throttle',
        'schedule': 'schedule',
        'status': 'status',
        'link': 'link'
    }

    def __init__(self, operation_info=None, throttle=None, schedule=None, status=None, link=None, _configuration=None):  # noqa: E501
        """DataMovementInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation_info = None
        self._throttle = None
        self._schedule = None
        self._status = None
        self._link = None
        self.discriminator = None

        self.operation_info = operation_info
        if throttle is not None:
            self.throttle = throttle
        if schedule is not None:
            self.schedule = schedule
        if status is not None:
            self.status = status
        if link is not None:
            self.link = link

    @property
    def operation_info(self):
        """Gets the operation_info of this DataMovementInfo.  # noqa: E501


        :return: The operation_info of this DataMovementInfo.  # noqa: E501
        :rtype: str
        """
        return self._operation_info

    @operation_info.setter
    def operation_info(self, operation_info):
        """Sets the operation_info of this DataMovementInfo.


        :param operation_info: The operation_info of this DataMovementInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and operation_info is None:
            raise ValueError("Invalid value for `operation_info`, must not be `None`")  # noqa: E501

        self._operation_info = operation_info

    @property
    def throttle(self):
        """Gets the throttle of this DataMovementInfo.  # noqa: E501


        :return: The throttle of this DataMovementInfo.  # noqa: E501
        :rtype: int
        """
        return self._throttle

    @throttle.setter
    def throttle(self, throttle):
        """Sets the throttle of this DataMovementInfo.


        :param throttle: The throttle of this DataMovementInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                throttle is not None and throttle < 0):  # noqa: E501
            raise ValueError("Invalid value for `throttle`, must be a value greater than or equal to `0`")  # noqa: E501

        self._throttle = throttle

    @property
    def schedule(self):
        """Gets the schedule of this DataMovementInfo.  # noqa: E501


        :return: The schedule of this DataMovementInfo.  # noqa: E501
        :rtype: DataMovementSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DataMovementInfo.


        :param schedule: The schedule of this DataMovementInfo.  # noqa: E501
        :type: DataMovementSchedule
        """

        self._schedule = schedule

    @property
    def status(self):
        """Gets the status of this DataMovementInfo.  # noqa: E501


        :return: The status of this DataMovementInfo.  # noqa: E501
        :rtype: DataMovementStatusInfo
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataMovementInfo.


        :param status: The status of this DataMovementInfo.  # noqa: E501
        :type: DataMovementStatusInfo
        """

        self._status = status

    @property
    def link(self):
        """Gets the link of this DataMovementInfo.  # noqa: E501


        :return: The link of this DataMovementInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DataMovementInfo.


        :param link: The link of this DataMovementInfo.  # noqa: E501
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
        if issubclass(DataMovementInfo, dict):
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
        if not isinstance(other, DataMovementInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataMovementInfo):
            return True

        return self.to_dict() != other.to_dict()
