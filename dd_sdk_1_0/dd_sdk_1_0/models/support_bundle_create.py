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


class SupportBundleCreate(object):
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
        'bundle_type': 'BundleType',
        'nodes': 'list[str]',
        'files': 'list[str]'
    }

    attribute_map = {
        'bundle_type': 'bundle_type',
        'nodes': 'nodes',
        'files': 'files'
    }

    def __init__(self, bundle_type=None, nodes=None, files=None, _configuration=None):  # noqa: E501
        """SupportBundleCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bundle_type = None
        self._nodes = None
        self._files = None
        self.discriminator = None

        if bundle_type is not None:
            self.bundle_type = bundle_type
        if nodes is not None:
            self.nodes = nodes
        if files is not None:
            self.files = files

    @property
    def bundle_type(self):
        """Gets the bundle_type of this SupportBundleCreate.  # noqa: E501


        :return: The bundle_type of this SupportBundleCreate.  # noqa: E501
        :rtype: BundleType
        """
        return self._bundle_type

    @bundle_type.setter
    def bundle_type(self, bundle_type):
        """Sets the bundle_type of this SupportBundleCreate.


        :param bundle_type: The bundle_type of this SupportBundleCreate.  # noqa: E501
        :type: BundleType
        """

        self._bundle_type = bundle_type

    @property
    def nodes(self):
        """Gets the nodes of this SupportBundleCreate.  # noqa: E501


        :return: The nodes of this SupportBundleCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this SupportBundleCreate.


        :param nodes: The nodes of this SupportBundleCreate.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def files(self):
        """Gets the files of this SupportBundleCreate.  # noqa: E501


        :return: The files of this SupportBundleCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SupportBundleCreate.


        :param files: The files of this SupportBundleCreate.  # noqa: E501
        :type: list[str]
        """

        self._files = files

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
        if issubclass(SupportBundleCreate, dict):
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
        if not isinstance(other, SupportBundleCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportBundleCreate):
            return True

        return self.to_dict() != other.to_dict()
