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


class TenantUnitModify(object):
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
        'operation': 'TenantUnitModifyOperation',
        'name': 'str',
        'tenant_name': 'str',
        'local_data_ip': 'str',
        'remote_data_ip': 'str',
        'gateway_ip': 'str',
        'hostname': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'name': 'name',
        'tenant_name': 'tenant_name',
        'local_data_ip': 'local_data_ip',
        'remote_data_ip': 'remote_data_ip',
        'gateway_ip': 'gateway_ip',
        'hostname': 'hostname'
    }

    def __init__(self, operation=None, name=None, tenant_name=None, local_data_ip=None, remote_data_ip=None, gateway_ip=None, hostname=None, _configuration=None):  # noqa: E501
        """TenantUnitModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation = None
        self._name = None
        self._tenant_name = None
        self._local_data_ip = None
        self._remote_data_ip = None
        self._gateway_ip = None
        self._hostname = None
        self.discriminator = None

        self.operation = operation
        if name is not None:
            self.name = name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if local_data_ip is not None:
            self.local_data_ip = local_data_ip
        if remote_data_ip is not None:
            self.remote_data_ip = remote_data_ip
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if hostname is not None:
            self.hostname = hostname

    @property
    def operation(self):
        """Gets the operation of this TenantUnitModify.  # noqa: E501


        :return: The operation of this TenantUnitModify.  # noqa: E501
        :rtype: TenantUnitModifyOperation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this TenantUnitModify.


        :param operation: The operation of this TenantUnitModify.  # noqa: E501
        :type: TenantUnitModifyOperation
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def name(self):
        """Gets the name of this TenantUnitModify.  # noqa: E501

        new Tenant Unit name; used with \"rename\" operation  # noqa: E501

        :return: The name of this TenantUnitModify.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantUnitModify.

        new Tenant Unit name; used with \"rename\" operation  # noqa: E501

        :param name: The name of this TenantUnitModify.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tenant_name(self):
        """Gets the tenant_name of this TenantUnitModify.  # noqa: E501

        Tenant to assign this Tenant Unit to; used with \"assign_tenant\" or \"unassign_tenant\" operation  # noqa: E501

        :return: The tenant_name of this TenantUnitModify.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this TenantUnitModify.

        Tenant to assign this Tenant Unit to; used with \"assign_tenant\" or \"unassign_tenant\" operation  # noqa: E501

        :param tenant_name: The tenant_name of this TenantUnitModify.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def local_data_ip(self):
        """Gets the local_data_ip of this TenantUnitModify.  # noqa: E501


        :return: The local_data_ip of this TenantUnitModify.  # noqa: E501
        :rtype: str
        """
        return self._local_data_ip

    @local_data_ip.setter
    def local_data_ip(self, local_data_ip):
        """Sets the local_data_ip of this TenantUnitModify.


        :param local_data_ip: The local_data_ip of this TenantUnitModify.  # noqa: E501
        :type: str
        """

        self._local_data_ip = local_data_ip

    @property
    def remote_data_ip(self):
        """Gets the remote_data_ip of this TenantUnitModify.  # noqa: E501


        :return: The remote_data_ip of this TenantUnitModify.  # noqa: E501
        :rtype: str
        """
        return self._remote_data_ip

    @remote_data_ip.setter
    def remote_data_ip(self, remote_data_ip):
        """Sets the remote_data_ip of this TenantUnitModify.


        :param remote_data_ip: The remote_data_ip of this TenantUnitModify.  # noqa: E501
        :type: str
        """

        self._remote_data_ip = remote_data_ip

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this TenantUnitModify.  # noqa: E501


        :return: The gateway_ip of this TenantUnitModify.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this TenantUnitModify.


        :param gateway_ip: The gateway_ip of this TenantUnitModify.  # noqa: E501
        :type: str
        """

        self._gateway_ip = gateway_ip

    @property
    def hostname(self):
        """Gets the hostname of this TenantUnitModify.  # noqa: E501


        :return: The hostname of this TenantUnitModify.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TenantUnitModify.


        :param hostname: The hostname of this TenantUnitModify.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

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
        if issubclass(TenantUnitModify, dict):
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
        if not isinstance(other, TenantUnitModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantUnitModify):
            return True

        return self.to_dict() != other.to_dict()