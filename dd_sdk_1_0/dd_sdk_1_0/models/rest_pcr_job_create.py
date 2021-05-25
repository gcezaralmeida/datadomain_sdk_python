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


class RestPcrJobCreate(object):
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
        'description': 'str',
        'exclude_dir_with_filename': 'str',
        'file_begin_mtime_epoch': 'int',
        'file_end_mtime_epoch': 'int',
        'min_file_size_bytes': 'int',
        'max_run_time_secs': 'int',
        'include_paths': 'list[RestPcrPath]',
        'exclude_paths': 'list[str]',
        'exclude_file_with_extensions': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'exclude_dir_with_filename': 'exclude_dir_with_filename',
        'file_begin_mtime_epoch': 'file_begin_mtime_epoch',
        'file_end_mtime_epoch': 'file_end_mtime_epoch',
        'min_file_size_bytes': 'min_file_size_bytes',
        'max_run_time_secs': 'max_run_time_secs',
        'include_paths': 'include_paths',
        'exclude_paths': 'exclude_paths',
        'exclude_file_with_extensions': 'exclude_file_with_extensions'
    }

    def __init__(self, description=None, exclude_dir_with_filename=None, file_begin_mtime_epoch=None, file_end_mtime_epoch=None, min_file_size_bytes=None, max_run_time_secs=None, include_paths=None, exclude_paths=None, exclude_file_with_extensions=None, _configuration=None):  # noqa: E501
        """RestPcrJobCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._exclude_dir_with_filename = None
        self._file_begin_mtime_epoch = None
        self._file_end_mtime_epoch = None
        self._min_file_size_bytes = None
        self._max_run_time_secs = None
        self._include_paths = None
        self._exclude_paths = None
        self._exclude_file_with_extensions = None
        self.discriminator = None

        self.description = description
        if exclude_dir_with_filename is not None:
            self.exclude_dir_with_filename = exclude_dir_with_filename
        if file_begin_mtime_epoch is not None:
            self.file_begin_mtime_epoch = file_begin_mtime_epoch
        if file_end_mtime_epoch is not None:
            self.file_end_mtime_epoch = file_end_mtime_epoch
        if min_file_size_bytes is not None:
            self.min_file_size_bytes = min_file_size_bytes
        if max_run_time_secs is not None:
            self.max_run_time_secs = max_run_time_secs
        self.include_paths = include_paths
        if exclude_paths is not None:
            self.exclude_paths = exclude_paths
        if exclude_file_with_extensions is not None:
            self.exclude_file_with_extensions = exclude_file_with_extensions

    @property
    def description(self):
        """Gets the description of this RestPcrJobCreate.  # noqa: E501


        :return: The description of this RestPcrJobCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RestPcrJobCreate.


        :param description: The description of this RestPcrJobCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def exclude_dir_with_filename(self):
        """Gets the exclude_dir_with_filename of this RestPcrJobCreate.  # noqa: E501


        :return: The exclude_dir_with_filename of this RestPcrJobCreate.  # noqa: E501
        :rtype: str
        """
        return self._exclude_dir_with_filename

    @exclude_dir_with_filename.setter
    def exclude_dir_with_filename(self, exclude_dir_with_filename):
        """Sets the exclude_dir_with_filename of this RestPcrJobCreate.


        :param exclude_dir_with_filename: The exclude_dir_with_filename of this RestPcrJobCreate.  # noqa: E501
        :type: str
        """

        self._exclude_dir_with_filename = exclude_dir_with_filename

    @property
    def file_begin_mtime_epoch(self):
        """Gets the file_begin_mtime_epoch of this RestPcrJobCreate.  # noqa: E501


        :return: The file_begin_mtime_epoch of this RestPcrJobCreate.  # noqa: E501
        :rtype: int
        """
        return self._file_begin_mtime_epoch

    @file_begin_mtime_epoch.setter
    def file_begin_mtime_epoch(self, file_begin_mtime_epoch):
        """Sets the file_begin_mtime_epoch of this RestPcrJobCreate.


        :param file_begin_mtime_epoch: The file_begin_mtime_epoch of this RestPcrJobCreate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                file_begin_mtime_epoch is not None and file_begin_mtime_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `file_begin_mtime_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._file_begin_mtime_epoch = file_begin_mtime_epoch

    @property
    def file_end_mtime_epoch(self):
        """Gets the file_end_mtime_epoch of this RestPcrJobCreate.  # noqa: E501


        :return: The file_end_mtime_epoch of this RestPcrJobCreate.  # noqa: E501
        :rtype: int
        """
        return self._file_end_mtime_epoch

    @file_end_mtime_epoch.setter
    def file_end_mtime_epoch(self, file_end_mtime_epoch):
        """Sets the file_end_mtime_epoch of this RestPcrJobCreate.


        :param file_end_mtime_epoch: The file_end_mtime_epoch of this RestPcrJobCreate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                file_end_mtime_epoch is not None and file_end_mtime_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `file_end_mtime_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._file_end_mtime_epoch = file_end_mtime_epoch

    @property
    def min_file_size_bytes(self):
        """Gets the min_file_size_bytes of this RestPcrJobCreate.  # noqa: E501


        :return: The min_file_size_bytes of this RestPcrJobCreate.  # noqa: E501
        :rtype: int
        """
        return self._min_file_size_bytes

    @min_file_size_bytes.setter
    def min_file_size_bytes(self, min_file_size_bytes):
        """Sets the min_file_size_bytes of this RestPcrJobCreate.


        :param min_file_size_bytes: The min_file_size_bytes of this RestPcrJobCreate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                min_file_size_bytes is not None and min_file_size_bytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_file_size_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_file_size_bytes = min_file_size_bytes

    @property
    def max_run_time_secs(self):
        """Gets the max_run_time_secs of this RestPcrJobCreate.  # noqa: E501


        :return: The max_run_time_secs of this RestPcrJobCreate.  # noqa: E501
        :rtype: int
        """
        return self._max_run_time_secs

    @max_run_time_secs.setter
    def max_run_time_secs(self, max_run_time_secs):
        """Sets the max_run_time_secs of this RestPcrJobCreate.


        :param max_run_time_secs: The max_run_time_secs of this RestPcrJobCreate.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                max_run_time_secs is not None and max_run_time_secs < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_run_time_secs`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_run_time_secs = max_run_time_secs

    @property
    def include_paths(self):
        """Gets the include_paths of this RestPcrJobCreate.  # noqa: E501


        :return: The include_paths of this RestPcrJobCreate.  # noqa: E501
        :rtype: list[RestPcrPath]
        """
        return self._include_paths

    @include_paths.setter
    def include_paths(self, include_paths):
        """Sets the include_paths of this RestPcrJobCreate.


        :param include_paths: The include_paths of this RestPcrJobCreate.  # noqa: E501
        :type: list[RestPcrPath]
        """
        if self._configuration.client_side_validation and include_paths is None:
            raise ValueError("Invalid value for `include_paths`, must not be `None`")  # noqa: E501

        self._include_paths = include_paths

    @property
    def exclude_paths(self):
        """Gets the exclude_paths of this RestPcrJobCreate.  # noqa: E501


        :return: The exclude_paths of this RestPcrJobCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_paths

    @exclude_paths.setter
    def exclude_paths(self, exclude_paths):
        """Sets the exclude_paths of this RestPcrJobCreate.


        :param exclude_paths: The exclude_paths of this RestPcrJobCreate.  # noqa: E501
        :type: list[str]
        """

        self._exclude_paths = exclude_paths

    @property
    def exclude_file_with_extensions(self):
        """Gets the exclude_file_with_extensions of this RestPcrJobCreate.  # noqa: E501


        :return: The exclude_file_with_extensions of this RestPcrJobCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_file_with_extensions

    @exclude_file_with_extensions.setter
    def exclude_file_with_extensions(self, exclude_file_with_extensions):
        """Sets the exclude_file_with_extensions of this RestPcrJobCreate.


        :param exclude_file_with_extensions: The exclude_file_with_extensions of this RestPcrJobCreate.  # noqa: E501
        :type: list[str]
        """

        self._exclude_file_with_extensions = exclude_file_with_extensions

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
        if issubclass(RestPcrJobCreate, dict):
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
        if not isinstance(other, RestPcrJobCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestPcrJobCreate):
            return True

        return self.to_dict() != other.to_dict()
