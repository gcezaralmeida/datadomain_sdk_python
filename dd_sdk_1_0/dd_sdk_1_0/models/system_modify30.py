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


class SystemModify30(object):
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
        'operation': 'SystemModifyOps',
        'pphrase_request': 'SystemPphraseRequest',
        'cluster_id': 'str',
        'power_action_request': 'PowerActionRequest',
        'headswap_request': 'HeadswapRequest',
        'adopt_type': 'AdoptType',
        'adopt_value': 'str',
        'management': 'IpRanges',
        'interconnect': 'IpRanges',
        'data': 'IpRanges',
        'replacing_host': 'str',
        'number_of_nodes': 'int',
        'with_cloud_tier_enabled': 'bool',
        'disaster_recovery_config_info': 'list[DrConfigInfo]',
        'repair_request': 'SystemNodeRepairRequest'
    }

    attribute_map = {
        'operation': 'operation',
        'pphrase_request': 'pphrase_request',
        'cluster_id': 'cluster_id',
        'power_action_request': 'power_action_request',
        'headswap_request': 'headswap_request',
        'adopt_type': 'adopt_type',
        'adopt_value': 'adopt_value',
        'management': 'management',
        'interconnect': 'interconnect',
        'data': 'data',
        'replacing_host': 'replacing_host',
        'number_of_nodes': 'number_of_nodes',
        'with_cloud_tier_enabled': 'with_cloud_tier_enabled',
        'disaster_recovery_config_info': 'disaster_recovery_config_info',
        'repair_request': 'repair_request'
    }

    def __init__(self, operation=None, pphrase_request=None, cluster_id=None, power_action_request=None, headswap_request=None, adopt_type=None, adopt_value=None, management=None, interconnect=None, data=None, replacing_host=None, number_of_nodes=None, with_cloud_tier_enabled=None, disaster_recovery_config_info=None, repair_request=None, _configuration=None):  # noqa: E501
        """SystemModify30 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation = None
        self._pphrase_request = None
        self._cluster_id = None
        self._power_action_request = None
        self._headswap_request = None
        self._adopt_type = None
        self._adopt_value = None
        self._management = None
        self._interconnect = None
        self._data = None
        self._replacing_host = None
        self._number_of_nodes = None
        self._with_cloud_tier_enabled = None
        self._disaster_recovery_config_info = None
        self._repair_request = None
        self.discriminator = None

        self.operation = operation
        if pphrase_request is not None:
            self.pphrase_request = pphrase_request
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if power_action_request is not None:
            self.power_action_request = power_action_request
        if headswap_request is not None:
            self.headswap_request = headswap_request
        if adopt_type is not None:
            self.adopt_type = adopt_type
        if adopt_value is not None:
            self.adopt_value = adopt_value
        if management is not None:
            self.management = management
        if interconnect is not None:
            self.interconnect = interconnect
        if data is not None:
            self.data = data
        if replacing_host is not None:
            self.replacing_host = replacing_host
        if number_of_nodes is not None:
            self.number_of_nodes = number_of_nodes
        if with_cloud_tier_enabled is not None:
            self.with_cloud_tier_enabled = with_cloud_tier_enabled
        if disaster_recovery_config_info is not None:
            self.disaster_recovery_config_info = disaster_recovery_config_info
        if repair_request is not None:
            self.repair_request = repair_request

    @property
    def operation(self):
        """Gets the operation of this SystemModify30.  # noqa: E501


        :return: The operation of this SystemModify30.  # noqa: E501
        :rtype: SystemModifyOps
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this SystemModify30.


        :param operation: The operation of this SystemModify30.  # noqa: E501
        :type: SystemModifyOps
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def pphrase_request(self):
        """Gets the pphrase_request of this SystemModify30.  # noqa: E501


        :return: The pphrase_request of this SystemModify30.  # noqa: E501
        :rtype: SystemPphraseRequest
        """
        return self._pphrase_request

    @pphrase_request.setter
    def pphrase_request(self, pphrase_request):
        """Sets the pphrase_request of this SystemModify30.


        :param pphrase_request: The pphrase_request of this SystemModify30.  # noqa: E501
        :type: SystemPphraseRequest
        """

        self._pphrase_request = pphrase_request

    @property
    def cluster_id(self):
        """Gets the cluster_id of this SystemModify30.  # noqa: E501


        :return: The cluster_id of this SystemModify30.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this SystemModify30.


        :param cluster_id: The cluster_id of this SystemModify30.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def power_action_request(self):
        """Gets the power_action_request of this SystemModify30.  # noqa: E501


        :return: The power_action_request of this SystemModify30.  # noqa: E501
        :rtype: PowerActionRequest
        """
        return self._power_action_request

    @power_action_request.setter
    def power_action_request(self, power_action_request):
        """Sets the power_action_request of this SystemModify30.


        :param power_action_request: The power_action_request of this SystemModify30.  # noqa: E501
        :type: PowerActionRequest
        """

        self._power_action_request = power_action_request

    @property
    def headswap_request(self):
        """Gets the headswap_request of this SystemModify30.  # noqa: E501


        :return: The headswap_request of this SystemModify30.  # noqa: E501
        :rtype: HeadswapRequest
        """
        return self._headswap_request

    @headswap_request.setter
    def headswap_request(self, headswap_request):
        """Sets the headswap_request of this SystemModify30.


        :param headswap_request: The headswap_request of this SystemModify30.  # noqa: E501
        :type: HeadswapRequest
        """

        self._headswap_request = headswap_request

    @property
    def adopt_type(self):
        """Gets the adopt_type of this SystemModify30.  # noqa: E501


        :return: The adopt_type of this SystemModify30.  # noqa: E501
        :rtype: AdoptType
        """
        return self._adopt_type

    @adopt_type.setter
    def adopt_type(self, adopt_type):
        """Sets the adopt_type of this SystemModify30.


        :param adopt_type: The adopt_type of this SystemModify30.  # noqa: E501
        :type: AdoptType
        """

        self._adopt_type = adopt_type

    @property
    def adopt_value(self):
        """Gets the adopt_value of this SystemModify30.  # noqa: E501


        :return: The adopt_value of this SystemModify30.  # noqa: E501
        :rtype: str
        """
        return self._adopt_value

    @adopt_value.setter
    def adopt_value(self, adopt_value):
        """Sets the adopt_value of this SystemModify30.


        :param adopt_value: The adopt_value of this SystemModify30.  # noqa: E501
        :type: str
        """

        self._adopt_value = adopt_value

    @property
    def management(self):
        """Gets the management of this SystemModify30.  # noqa: E501


        :return: The management of this SystemModify30.  # noqa: E501
        :rtype: IpRanges
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this SystemModify30.


        :param management: The management of this SystemModify30.  # noqa: E501
        :type: IpRanges
        """

        self._management = management

    @property
    def interconnect(self):
        """Gets the interconnect of this SystemModify30.  # noqa: E501


        :return: The interconnect of this SystemModify30.  # noqa: E501
        :rtype: IpRanges
        """
        return self._interconnect

    @interconnect.setter
    def interconnect(self, interconnect):
        """Sets the interconnect of this SystemModify30.


        :param interconnect: The interconnect of this SystemModify30.  # noqa: E501
        :type: IpRanges
        """

        self._interconnect = interconnect

    @property
    def data(self):
        """Gets the data of this SystemModify30.  # noqa: E501


        :return: The data of this SystemModify30.  # noqa: E501
        :rtype: IpRanges
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SystemModify30.


        :param data: The data of this SystemModify30.  # noqa: E501
        :type: IpRanges
        """

        self._data = data

    @property
    def replacing_host(self):
        """Gets the replacing_host of this SystemModify30.  # noqa: E501


        :return: The replacing_host of this SystemModify30.  # noqa: E501
        :rtype: str
        """
        return self._replacing_host

    @replacing_host.setter
    def replacing_host(self, replacing_host):
        """Sets the replacing_host of this SystemModify30.


        :param replacing_host: The replacing_host of this SystemModify30.  # noqa: E501
        :type: str
        """

        self._replacing_host = replacing_host

    @property
    def number_of_nodes(self):
        """Gets the number_of_nodes of this SystemModify30.  # noqa: E501

        number of nodes to deploy  # noqa: E501

        :return: The number_of_nodes of this SystemModify30.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """Sets the number_of_nodes of this SystemModify30.

        number of nodes to deploy  # noqa: E501

        :param number_of_nodes: The number_of_nodes of this SystemModify30.  # noqa: E501
        :type: int
        """

        self._number_of_nodes = number_of_nodes

    @property
    def with_cloud_tier_enabled(self):
        """Gets the with_cloud_tier_enabled of this SystemModify30.  # noqa: E501


        :return: The with_cloud_tier_enabled of this SystemModify30.  # noqa: E501
        :rtype: bool
        """
        return self._with_cloud_tier_enabled

    @with_cloud_tier_enabled.setter
    def with_cloud_tier_enabled(self, with_cloud_tier_enabled):
        """Sets the with_cloud_tier_enabled of this SystemModify30.


        :param with_cloud_tier_enabled: The with_cloud_tier_enabled of this SystemModify30.  # noqa: E501
        :type: bool
        """

        self._with_cloud_tier_enabled = with_cloud_tier_enabled

    @property
    def disaster_recovery_config_info(self):
        """Gets the disaster_recovery_config_info of this SystemModify30.  # noqa: E501


        :return: The disaster_recovery_config_info of this SystemModify30.  # noqa: E501
        :rtype: list[DrConfigInfo]
        """
        return self._disaster_recovery_config_info

    @disaster_recovery_config_info.setter
    def disaster_recovery_config_info(self, disaster_recovery_config_info):
        """Sets the disaster_recovery_config_info of this SystemModify30.


        :param disaster_recovery_config_info: The disaster_recovery_config_info of this SystemModify30.  # noqa: E501
        :type: list[DrConfigInfo]
        """

        self._disaster_recovery_config_info = disaster_recovery_config_info

    @property
    def repair_request(self):
        """Gets the repair_request of this SystemModify30.  # noqa: E501


        :return: The repair_request of this SystemModify30.  # noqa: E501
        :rtype: SystemNodeRepairRequest
        """
        return self._repair_request

    @repair_request.setter
    def repair_request(self, repair_request):
        """Sets the repair_request of this SystemModify30.


        :param repair_request: The repair_request of this SystemModify30.  # noqa: E501
        :type: SystemNodeRepairRequest
        """

        self._repair_request = repair_request

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
        if issubclass(SystemModify30, dict):
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
        if not isinstance(other, SystemModify30):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemModify30):
            return True

        return self.to_dict() != other.to_dict()
