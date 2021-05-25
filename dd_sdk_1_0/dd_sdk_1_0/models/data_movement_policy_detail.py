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


class DataMovementPolicyDetail(object):
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
        'id': 'str',
        'mtree_name': 'str',
        'cloud_unit_name': 'str',
        'data_movement_policy_type': 'PolicyType',
        'age_threshold_days': 'int',
        'min_age_days': 'int',
        'max_age_days': 'int',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'id': 'id',
        'mtree_name': 'mtree_name',
        'cloud_unit_name': 'cloud_unit_name',
        'data_movement_policy_type': 'data_movement_policy_type',
        'age_threshold_days': 'age_threshold_days',
        'min_age_days': 'min_age_days',
        'max_age_days': 'max_age_days',
        'link': 'link'
    }

    def __init__(self, id=None, mtree_name=None, cloud_unit_name=None, data_movement_policy_type=None, age_threshold_days=None, min_age_days=None, max_age_days=None, link=None, _configuration=None):  # noqa: E501
        """DataMovementPolicyDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._mtree_name = None
        self._cloud_unit_name = None
        self._data_movement_policy_type = None
        self._age_threshold_days = None
        self._min_age_days = None
        self._max_age_days = None
        self._link = None
        self.discriminator = None

        self.id = id
        self.mtree_name = mtree_name
        self.cloud_unit_name = cloud_unit_name
        self.data_movement_policy_type = data_movement_policy_type
        if age_threshold_days is not None:
            self.age_threshold_days = age_threshold_days
        if min_age_days is not None:
            self.min_age_days = min_age_days
        if max_age_days is not None:
            self.max_age_days = max_age_days
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this DataMovementPolicyDetail.  # noqa: E501

        Data Movement Policy id  # noqa: E501

        :return: The id of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataMovementPolicyDetail.

        Data Movement Policy id  # noqa: E501

        :param id: The id of this DataMovementPolicyDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def mtree_name(self):
        """Gets the mtree_name of this DataMovementPolicyDetail.  # noqa: E501


        :return: The mtree_name of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: str
        """
        return self._mtree_name

    @mtree_name.setter
    def mtree_name(self, mtree_name):
        """Sets the mtree_name of this DataMovementPolicyDetail.


        :param mtree_name: The mtree_name of this DataMovementPolicyDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mtree_name is None:
            raise ValueError("Invalid value for `mtree_name`, must not be `None`")  # noqa: E501

        self._mtree_name = mtree_name

    @property
    def cloud_unit_name(self):
        """Gets the cloud_unit_name of this DataMovementPolicyDetail.  # noqa: E501


        :return: The cloud_unit_name of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: str
        """
        return self._cloud_unit_name

    @cloud_unit_name.setter
    def cloud_unit_name(self, cloud_unit_name):
        """Sets the cloud_unit_name of this DataMovementPolicyDetail.


        :param cloud_unit_name: The cloud_unit_name of this DataMovementPolicyDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cloud_unit_name is None:
            raise ValueError("Invalid value for `cloud_unit_name`, must not be `None`")  # noqa: E501

        self._cloud_unit_name = cloud_unit_name

    @property
    def data_movement_policy_type(self):
        """Gets the data_movement_policy_type of this DataMovementPolicyDetail.  # noqa: E501


        :return: The data_movement_policy_type of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: PolicyType
        """
        return self._data_movement_policy_type

    @data_movement_policy_type.setter
    def data_movement_policy_type(self, data_movement_policy_type):
        """Sets the data_movement_policy_type of this DataMovementPolicyDetail.


        :param data_movement_policy_type: The data_movement_policy_type of this DataMovementPolicyDetail.  # noqa: E501
        :type: PolicyType
        """
        if self._configuration.client_side_validation and data_movement_policy_type is None:
            raise ValueError("Invalid value for `data_movement_policy_type`, must not be `None`")  # noqa: E501

        self._data_movement_policy_type = data_movement_policy_type

    @property
    def age_threshold_days(self):
        """Gets the age_threshold_days of this DataMovementPolicyDetail.  # noqa: E501


        :return: The age_threshold_days of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: int
        """
        return self._age_threshold_days

    @age_threshold_days.setter
    def age_threshold_days(self, age_threshold_days):
        """Sets the age_threshold_days of this DataMovementPolicyDetail.


        :param age_threshold_days: The age_threshold_days of this DataMovementPolicyDetail.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                age_threshold_days is not None and age_threshold_days < 0):  # noqa: E501
            raise ValueError("Invalid value for `age_threshold_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age_threshold_days = age_threshold_days

    @property
    def min_age_days(self):
        """Gets the min_age_days of this DataMovementPolicyDetail.  # noqa: E501


        :return: The min_age_days of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: int
        """
        return self._min_age_days

    @min_age_days.setter
    def min_age_days(self, min_age_days):
        """Sets the min_age_days of this DataMovementPolicyDetail.


        :param min_age_days: The min_age_days of this DataMovementPolicyDetail.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                min_age_days is not None and min_age_days < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_age_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_age_days = min_age_days

    @property
    def max_age_days(self):
        """Gets the max_age_days of this DataMovementPolicyDetail.  # noqa: E501


        :return: The max_age_days of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: int
        """
        return self._max_age_days

    @max_age_days.setter
    def max_age_days(self, max_age_days):
        """Sets the max_age_days of this DataMovementPolicyDetail.


        :param max_age_days: The max_age_days of this DataMovementPolicyDetail.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                max_age_days is not None and max_age_days < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_age_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_age_days = max_age_days

    @property
    def link(self):
        """Gets the link of this DataMovementPolicyDetail.  # noqa: E501


        :return: The link of this DataMovementPolicyDetail.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DataMovementPolicyDetail.


        :param link: The link of this DataMovementPolicyDetail.  # noqa: E501
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
        if issubclass(DataMovementPolicyDetail, dict):
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
        if not isinstance(other, DataMovementPolicyDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataMovementPolicyDetail):
            return True

        return self.to_dict() != other.to_dict()
