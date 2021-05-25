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


class TaskResourceRep(object):
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
        'op_id': 'str',
        'description': 'str',
        'state': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'service_status': 'ServiceStatus',
        'resource': 'RelatedResourceRep',
        'link': 'RestLinkRep'
    }

    attribute_map = {
        'op_id': 'op_id',
        'description': 'description',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'service_status': 'service_status',
        'resource': 'resource',
        'link': 'link'
    }

    def __init__(self, op_id=None, description=None, state=None, start_time=None, end_time=None, service_status=None, resource=None, link=None, _configuration=None):  # noqa: E501
        """TaskResourceRep - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._op_id = None
        self._description = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._service_status = None
        self._resource = None
        self._link = None
        self.discriminator = None

        if op_id is not None:
            self.op_id = op_id
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if service_status is not None:
            self.service_status = service_status
        if resource is not None:
            self.resource = resource
        if link is not None:
            self.link = link

    @property
    def op_id(self):
        """Gets the op_id of this TaskResourceRep.  # noqa: E501


        :return: The op_id of this TaskResourceRep.  # noqa: E501
        :rtype: str
        """
        return self._op_id

    @op_id.setter
    def op_id(self, op_id):
        """Sets the op_id of this TaskResourceRep.


        :param op_id: The op_id of this TaskResourceRep.  # noqa: E501
        :type: str
        """

        self._op_id = op_id

    @property
    def description(self):
        """Gets the description of this TaskResourceRep.  # noqa: E501


        :return: The description of this TaskResourceRep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskResourceRep.


        :param description: The description of this TaskResourceRep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def state(self):
        """Gets the state of this TaskResourceRep.  # noqa: E501


        :return: The state of this TaskResourceRep.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskResourceRep.


        :param state: The state of this TaskResourceRep.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this TaskResourceRep.  # noqa: E501


        :return: The start_time of this TaskResourceRep.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskResourceRep.


        :param start_time: The start_time of this TaskResourceRep.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskResourceRep.  # noqa: E501


        :return: The end_time of this TaskResourceRep.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskResourceRep.


        :param end_time: The end_time of this TaskResourceRep.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def service_status(self):
        """Gets the service_status of this TaskResourceRep.  # noqa: E501


        :return: The service_status of this TaskResourceRep.  # noqa: E501
        :rtype: ServiceStatus
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this TaskResourceRep.


        :param service_status: The service_status of this TaskResourceRep.  # noqa: E501
        :type: ServiceStatus
        """

        self._service_status = service_status

    @property
    def resource(self):
        """Gets the resource of this TaskResourceRep.  # noqa: E501


        :return: The resource of this TaskResourceRep.  # noqa: E501
        :rtype: RelatedResourceRep
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this TaskResourceRep.


        :param resource: The resource of this TaskResourceRep.  # noqa: E501
        :type: RelatedResourceRep
        """

        self._resource = resource

    @property
    def link(self):
        """Gets the link of this TaskResourceRep.  # noqa: E501


        :return: The link of this TaskResourceRep.  # noqa: E501
        :rtype: RestLinkRep
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TaskResourceRep.


        :param link: The link of this TaskResourceRep.  # noqa: E501
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
        if issubclass(TaskResourceRep, dict):
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
        if not isinstance(other, TaskResourceRep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskResourceRep):
            return True

        return self.to_dict() != other.to_dict()
