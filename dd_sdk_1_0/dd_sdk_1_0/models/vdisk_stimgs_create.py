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


class VdiskStimgsCreate(object):
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
        'stimg_create': 'list[VdiskStimgCreate]',
        'common_property': 'list[KeyValuePair]'
    }

    attribute_map = {
        'stimg_create': 'stimg_create',
        'common_property': 'common_property'
    }

    def __init__(self, stimg_create=None, common_property=None, _configuration=None):  # noqa: E501
        """VdiskStimgsCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._stimg_create = None
        self._common_property = None
        self.discriminator = None

        self.stimg_create = stimg_create
        if common_property is not None:
            self.common_property = common_property

    @property
    def stimg_create(self):
        """Gets the stimg_create of this VdiskStimgsCreate.  # noqa: E501

        creation for each static image  # noqa: E501

        :return: The stimg_create of this VdiskStimgsCreate.  # noqa: E501
        :rtype: list[VdiskStimgCreate]
        """
        return self._stimg_create

    @stimg_create.setter
    def stimg_create(self, stimg_create):
        """Sets the stimg_create of this VdiskStimgsCreate.

        creation for each static image  # noqa: E501

        :param stimg_create: The stimg_create of this VdiskStimgsCreate.  # noqa: E501
        :type: list[VdiskStimgCreate]
        """
        if self._configuration.client_side_validation and stimg_create is None:
            raise ValueError("Invalid value for `stimg_create`, must not be `None`")  # noqa: E501

        self._stimg_create = stimg_create

    @property
    def common_property(self):
        """Gets the common_property of this VdiskStimgsCreate.  # noqa: E501


        :return: The common_property of this VdiskStimgsCreate.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._common_property

    @common_property.setter
    def common_property(self, common_property):
        """Sets the common_property of this VdiskStimgsCreate.


        :param common_property: The common_property of this VdiskStimgsCreate.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._common_property = common_property

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
        if issubclass(VdiskStimgsCreate, dict):
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
        if not isinstance(other, VdiskStimgsCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskStimgsCreate):
            return True

        return self.to_dict() != other.to_dict()
