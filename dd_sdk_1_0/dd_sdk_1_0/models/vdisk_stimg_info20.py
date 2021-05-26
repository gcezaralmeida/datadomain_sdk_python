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


class VdiskStimgInfo20(object):
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
        'guid': 'str',
        'name': 'str',
        'retention_info': 'VdiskStimgRetentionInfo',
        'tier_info': 'VdiskStimgTierInfo',
        'link': 'RestLinkRep'
    }

    attribute_map = {
        'id': 'id',
        'guid': 'guid',
        'name': 'name',
        'retention_info': 'retention_info',
        'tier_info': 'tier_info',
        'link': 'link'
    }

    def __init__(self, id=None, guid=None, name=None, retention_info=None, tier_info=None, link=None, _configuration=None):  # noqa: E501
        """VdiskStimgInfo20 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._guid = None
        self._name = None
        self._retention_info = None
        self._tier_info = None
        self._link = None
        self.discriminator = None

        self.id = id
        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if retention_info is not None:
            self.retention_info = retention_info
        if tier_info is not None:
            self.tier_info = tier_info
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this VdiskStimgInfo20.  # noqa: E501

        urlencoded GUID  # noqa: E501

        :return: The id of this VdiskStimgInfo20.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VdiskStimgInfo20.

        urlencoded GUID  # noqa: E501

        :param id: The id of this VdiskStimgInfo20.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def guid(self):
        """Gets the guid of this VdiskStimgInfo20.  # noqa: E501


        :return: The guid of this VdiskStimgInfo20.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this VdiskStimgInfo20.


        :param guid: The guid of this VdiskStimgInfo20.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this VdiskStimgInfo20.  # noqa: E501


        :return: The name of this VdiskStimgInfo20.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VdiskStimgInfo20.


        :param name: The name of this VdiskStimgInfo20.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def retention_info(self):
        """Gets the retention_info of this VdiskStimgInfo20.  # noqa: E501


        :return: The retention_info of this VdiskStimgInfo20.  # noqa: E501
        :rtype: VdiskStimgRetentionInfo
        """
        return self._retention_info

    @retention_info.setter
    def retention_info(self, retention_info):
        """Sets the retention_info of this VdiskStimgInfo20.


        :param retention_info: The retention_info of this VdiskStimgInfo20.  # noqa: E501
        :type: VdiskStimgRetentionInfo
        """

        self._retention_info = retention_info

    @property
    def tier_info(self):
        """Gets the tier_info of this VdiskStimgInfo20.  # noqa: E501


        :return: The tier_info of this VdiskStimgInfo20.  # noqa: E501
        :rtype: VdiskStimgTierInfo
        """
        return self._tier_info

    @tier_info.setter
    def tier_info(self, tier_info):
        """Sets the tier_info of this VdiskStimgInfo20.


        :param tier_info: The tier_info of this VdiskStimgInfo20.  # noqa: E501
        :type: VdiskStimgTierInfo
        """

        self._tier_info = tier_info

    @property
    def link(self):
        """Gets the link of this VdiskStimgInfo20.  # noqa: E501


        :return: The link of this VdiskStimgInfo20.  # noqa: E501
        :rtype: RestLinkRep
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this VdiskStimgInfo20.


        :param link: The link of this VdiskStimgInfo20.  # noqa: E501
        :type: RestLinkRep
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
        if issubclass(VdiskStimgInfo20, dict):
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
        if not isinstance(other, VdiskStimgInfo20):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdiskStimgInfo20):
            return True

        return self.to_dict() != other.to_dict()