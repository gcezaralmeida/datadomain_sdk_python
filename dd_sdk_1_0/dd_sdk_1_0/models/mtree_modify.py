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


class MtreeModify(object):
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
        'tenant_unit': 'str',
        'quota_config': 'QuotaConfig',
        'retention': 'RetentionLockSet'
    }

    attribute_map = {
        'tenant_unit': 'tenant_unit',
        'quota_config': 'quota_config',
        'retention': 'retention'
    }

    def __init__(self, tenant_unit=None, quota_config=None, retention=None, _configuration=None):  # noqa: E501
        """MtreeModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tenant_unit = None
        self._quota_config = None
        self._retention = None
        self.discriminator = None

        if tenant_unit is not None:
            self.tenant_unit = tenant_unit
        if quota_config is not None:
            self.quota_config = quota_config
        if retention is not None:
            self.retention = retention

    @property
    def tenant_unit(self):
        """Gets the tenant_unit of this MtreeModify.  # noqa: E501

        \"none\" or tenant unit name  # noqa: E501

        :return: The tenant_unit of this MtreeModify.  # noqa: E501
        :rtype: str
        """
        return self._tenant_unit

    @tenant_unit.setter
    def tenant_unit(self, tenant_unit):
        """Sets the tenant_unit of this MtreeModify.

        \"none\" or tenant unit name  # noqa: E501

        :param tenant_unit: The tenant_unit of this MtreeModify.  # noqa: E501
        :type: str
        """

        self._tenant_unit = tenant_unit

    @property
    def quota_config(self):
        """Gets the quota_config of this MtreeModify.  # noqa: E501

        set the value as 0 for resetting the hard limit or soft limit.  # noqa: E501

        :return: The quota_config of this MtreeModify.  # noqa: E501
        :rtype: QuotaConfig
        """
        return self._quota_config

    @quota_config.setter
    def quota_config(self, quota_config):
        """Sets the quota_config of this MtreeModify.

        set the value as 0 for resetting the hard limit or soft limit.  # noqa: E501

        :param quota_config: The quota_config of this MtreeModify.  # noqa: E501
        :type: QuotaConfig
        """

        self._quota_config = quota_config

    @property
    def retention(self):
        """Gets the retention of this MtreeModify.  # noqa: E501


        :return: The retention of this MtreeModify.  # noqa: E501
        :rtype: RetentionLockSet
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this MtreeModify.


        :param retention: The retention of this MtreeModify.  # noqa: E501
        :type: RetentionLockSet
        """

        self._retention = retention

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
        if issubclass(MtreeModify, dict):
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
        if not isinstance(other, MtreeModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MtreeModify):
            return True

        return self.to_dict() != other.to_dict()
