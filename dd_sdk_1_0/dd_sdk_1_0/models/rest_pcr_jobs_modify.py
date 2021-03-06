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


class RestPcrJobsModify(object):
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
        'measurements': 'RestPcrJobIds',
        'options': 'RestPcrJobOptions'
    }

    attribute_map = {
        'measurements': 'measurements',
        'options': 'options'
    }

    def __init__(self, measurements=None, options=None, _configuration=None):  # noqa: E501
        """RestPcrJobsModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._measurements = None
        self._options = None
        self.discriminator = None

        self.measurements = measurements
        if options is not None:
            self.options = options

    @property
    def measurements(self):
        """Gets the measurements of this RestPcrJobsModify.  # noqa: E501


        :return: The measurements of this RestPcrJobsModify.  # noqa: E501
        :rtype: RestPcrJobIds
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        """Sets the measurements of this RestPcrJobsModify.


        :param measurements: The measurements of this RestPcrJobsModify.  # noqa: E501
        :type: RestPcrJobIds
        """
        if self._configuration.client_side_validation and measurements is None:
            raise ValueError("Invalid value for `measurements`, must not be `None`")  # noqa: E501

        self._measurements = measurements

    @property
    def options(self):
        """Gets the options of this RestPcrJobsModify.  # noqa: E501


        :return: The options of this RestPcrJobsModify.  # noqa: E501
        :rtype: RestPcrJobOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this RestPcrJobsModify.


        :param options: The options of this RestPcrJobsModify.  # noqa: E501
        :type: RestPcrJobOptions
        """

        self._options = options

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
        if issubclass(RestPcrJobsModify, dict):
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
        if not isinstance(other, RestPcrJobsModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestPcrJobsModify):
            return True

        return self.to_dict() != other.to_dict()
