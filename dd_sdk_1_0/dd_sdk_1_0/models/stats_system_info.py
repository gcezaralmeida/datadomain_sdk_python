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


class StatsSystemInfo(object):
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
        'name': 'str',
        'type': 'str',
        'version': 'str',
        'serialno': 'str',
        'model': 'str',
        'uptime': 'str',
        'state': 'str',
        'status': 'str',
        'added_epoch': 'int',
        'hd_sync_epoch': 'int',
        'cd_sync_epoch': 'int',
        'admin_email': 'str',
        'admin_host': 'str',
        'mem_size': 'int',
        'partition_size': 'int',
        'time_zone': 'str',
        'physical_capacity': 'Capacity',
        'logical_capacity': 'Capacity',
        'compression_factor': 'float',
        'capacity_usage_details': 'list[CapacityUsageDetails]',
        'subscribed_capacity': 'int',
        'license': 'list[LicenseInfo]',
        'location': 'str',
        'uuid': 'str',
        'system_status': 'str',
        'link': 'list[RestLinkRep]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'serialno': 'serialno',
        'model': 'model',
        'uptime': 'uptime',
        'state': 'state',
        'status': 'status',
        'added_epoch': 'added_epoch',
        'hd_sync_epoch': 'hd_sync_epoch',
        'cd_sync_epoch': 'cd_sync_epoch',
        'admin_email': 'admin_email',
        'admin_host': 'admin_host',
        'mem_size': 'mem_size',
        'partition_size': 'partition_size',
        'time_zone': 'time_zone',
        'physical_capacity': 'physical_capacity',
        'logical_capacity': 'logical_capacity',
        'compression_factor': 'compression_factor',
        'capacity_usage_details': 'capacity_usage_details',
        'subscribed_capacity': 'subscribed_capacity',
        'license': 'license',
        'location': 'location',
        'uuid': 'uuid',
        'system_status': 'system_status',
        'link': 'link'
    }

    def __init__(self, id=None, name=None, type=None, version=None, serialno=None, model=None, uptime=None, state=None, status=None, added_epoch=None, hd_sync_epoch=None, cd_sync_epoch=None, admin_email=None, admin_host=None, mem_size=None, partition_size=None, time_zone=None, physical_capacity=None, logical_capacity=None, compression_factor=None, capacity_usage_details=None, subscribed_capacity=None, license=None, location=None, uuid=None, system_status=None, link=None, _configuration=None):  # noqa: E501
        """StatsSystemInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._type = None
        self._version = None
        self._serialno = None
        self._model = None
        self._uptime = None
        self._state = None
        self._status = None
        self._added_epoch = None
        self._hd_sync_epoch = None
        self._cd_sync_epoch = None
        self._admin_email = None
        self._admin_host = None
        self._mem_size = None
        self._partition_size = None
        self._time_zone = None
        self._physical_capacity = None
        self._logical_capacity = None
        self._compression_factor = None
        self._capacity_usage_details = None
        self._subscribed_capacity = None
        self._license = None
        self._location = None
        self._uuid = None
        self._system_status = None
        self._link = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if serialno is not None:
            self.serialno = serialno
        if model is not None:
            self.model = model
        if uptime is not None:
            self.uptime = uptime
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if added_epoch is not None:
            self.added_epoch = added_epoch
        if hd_sync_epoch is not None:
            self.hd_sync_epoch = hd_sync_epoch
        if cd_sync_epoch is not None:
            self.cd_sync_epoch = cd_sync_epoch
        if admin_email is not None:
            self.admin_email = admin_email
        if admin_host is not None:
            self.admin_host = admin_host
        if mem_size is not None:
            self.mem_size = mem_size
        if partition_size is not None:
            self.partition_size = partition_size
        if time_zone is not None:
            self.time_zone = time_zone
        if physical_capacity is not None:
            self.physical_capacity = physical_capacity
        if logical_capacity is not None:
            self.logical_capacity = logical_capacity
        if compression_factor is not None:
            self.compression_factor = compression_factor
        if capacity_usage_details is not None:
            self.capacity_usage_details = capacity_usage_details
        if subscribed_capacity is not None:
            self.subscribed_capacity = subscribed_capacity
        if license is not None:
            self.license = license
        if location is not None:
            self.location = location
        if uuid is not None:
            self.uuid = uuid
        if system_status is not None:
            self.system_status = system_status
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this StatsSystemInfo.  # noqa: E501

        url-encoded system uuid  # noqa: E501

        :return: The id of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatsSystemInfo.

        url-encoded system uuid  # noqa: E501

        :param id: The id of this StatsSystemInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this StatsSystemInfo.  # noqa: E501


        :return: The name of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatsSystemInfo.


        :param name: The name of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this StatsSystemInfo.  # noqa: E501

        Possible values: standalone, HA  # noqa: E501

        :return: The type of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatsSystemInfo.

        Possible values: standalone, HA  # noqa: E501

        :param type: The type of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this StatsSystemInfo.  # noqa: E501


        :return: The version of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StatsSystemInfo.


        :param version: The version of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def serialno(self):
        """Gets the serialno of this StatsSystemInfo.  # noqa: E501


        :return: The serialno of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._serialno

    @serialno.setter
    def serialno(self, serialno):
        """Sets the serialno of this StatsSystemInfo.


        :param serialno: The serialno of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._serialno = serialno

    @property
    def model(self):
        """Gets the model of this StatsSystemInfo.  # noqa: E501


        :return: The model of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this StatsSystemInfo.


        :param model: The model of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def uptime(self):
        """Gets the uptime of this StatsSystemInfo.  # noqa: E501


        :return: The uptime of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this StatsSystemInfo.


        :param uptime: The uptime of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._uptime = uptime

    @property
    def state(self):
        """Gets the state of this StatsSystemInfo.  # noqa: E501

        Possible values: adding, managed, suspended, unmanaged, deleting  # noqa: E501

        :return: The state of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StatsSystemInfo.

        Possible values: adding, managed, suspended, unmanaged, deleting  # noqa: E501

        :param state: The state of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this StatsSystemInfo.  # noqa: E501

        Possible values: online, not-responding, not-transmitting, upgrading  # noqa: E501

        :return: The status of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatsSystemInfo.

        Possible values: online, not-responding, not-transmitting, upgrading  # noqa: E501

        :param status: The status of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def added_epoch(self):
        """Gets the added_epoch of this StatsSystemInfo.  # noqa: E501


        :return: The added_epoch of this StatsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._added_epoch

    @added_epoch.setter
    def added_epoch(self, added_epoch):
        """Sets the added_epoch of this StatsSystemInfo.


        :param added_epoch: The added_epoch of this StatsSystemInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                added_epoch is not None and added_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `added_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._added_epoch = added_epoch

    @property
    def hd_sync_epoch(self):
        """Gets the hd_sync_epoch of this StatsSystemInfo.  # noqa: E501


        :return: The hd_sync_epoch of this StatsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._hd_sync_epoch

    @hd_sync_epoch.setter
    def hd_sync_epoch(self, hd_sync_epoch):
        """Sets the hd_sync_epoch of this StatsSystemInfo.


        :param hd_sync_epoch: The hd_sync_epoch of this StatsSystemInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                hd_sync_epoch is not None and hd_sync_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `hd_sync_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._hd_sync_epoch = hd_sync_epoch

    @property
    def cd_sync_epoch(self):
        """Gets the cd_sync_epoch of this StatsSystemInfo.  # noqa: E501


        :return: The cd_sync_epoch of this StatsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._cd_sync_epoch

    @cd_sync_epoch.setter
    def cd_sync_epoch(self, cd_sync_epoch):
        """Sets the cd_sync_epoch of this StatsSystemInfo.


        :param cd_sync_epoch: The cd_sync_epoch of this StatsSystemInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                cd_sync_epoch is not None and cd_sync_epoch < 0):  # noqa: E501
            raise ValueError("Invalid value for `cd_sync_epoch`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cd_sync_epoch = cd_sync_epoch

    @property
    def admin_email(self):
        """Gets the admin_email of this StatsSystemInfo.  # noqa: E501


        :return: The admin_email of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this StatsSystemInfo.


        :param admin_email: The admin_email of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._admin_email = admin_email

    @property
    def admin_host(self):
        """Gets the admin_host of this StatsSystemInfo.  # noqa: E501


        :return: The admin_host of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._admin_host

    @admin_host.setter
    def admin_host(self, admin_host):
        """Sets the admin_host of this StatsSystemInfo.


        :param admin_host: The admin_host of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._admin_host = admin_host

    @property
    def mem_size(self):
        """Gets the mem_size of this StatsSystemInfo.  # noqa: E501


        :return: The mem_size of this StatsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._mem_size

    @mem_size.setter
    def mem_size(self, mem_size):
        """Sets the mem_size of this StatsSystemInfo.


        :param mem_size: The mem_size of this StatsSystemInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                mem_size is not None and mem_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `mem_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._mem_size = mem_size

    @property
    def partition_size(self):
        """Gets the partition_size of this StatsSystemInfo.  # noqa: E501


        :return: The partition_size of this StatsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._partition_size

    @partition_size.setter
    def partition_size(self, partition_size):
        """Sets the partition_size of this StatsSystemInfo.


        :param partition_size: The partition_size of this StatsSystemInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                partition_size is not None and partition_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `partition_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._partition_size = partition_size

    @property
    def time_zone(self):
        """Gets the time_zone of this StatsSystemInfo.  # noqa: E501


        :return: The time_zone of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this StatsSystemInfo.


        :param time_zone: The time_zone of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def physical_capacity(self):
        """Gets the physical_capacity of this StatsSystemInfo.  # noqa: E501


        :return: The physical_capacity of this StatsSystemInfo.  # noqa: E501
        :rtype: Capacity
        """
        return self._physical_capacity

    @physical_capacity.setter
    def physical_capacity(self, physical_capacity):
        """Sets the physical_capacity of this StatsSystemInfo.


        :param physical_capacity: The physical_capacity of this StatsSystemInfo.  # noqa: E501
        :type: Capacity
        """

        self._physical_capacity = physical_capacity

    @property
    def logical_capacity(self):
        """Gets the logical_capacity of this StatsSystemInfo.  # noqa: E501


        :return: The logical_capacity of this StatsSystemInfo.  # noqa: E501
        :rtype: Capacity
        """
        return self._logical_capacity

    @logical_capacity.setter
    def logical_capacity(self, logical_capacity):
        """Sets the logical_capacity of this StatsSystemInfo.


        :param logical_capacity: The logical_capacity of this StatsSystemInfo.  # noqa: E501
        :type: Capacity
        """

        self._logical_capacity = logical_capacity

    @property
    def compression_factor(self):
        """Gets the compression_factor of this StatsSystemInfo.  # noqa: E501


        :return: The compression_factor of this StatsSystemInfo.  # noqa: E501
        :rtype: float
        """
        return self._compression_factor

    @compression_factor.setter
    def compression_factor(self, compression_factor):
        """Sets the compression_factor of this StatsSystemInfo.


        :param compression_factor: The compression_factor of this StatsSystemInfo.  # noqa: E501
        :type: float
        """

        self._compression_factor = compression_factor

    @property
    def capacity_usage_details(self):
        """Gets the capacity_usage_details of this StatsSystemInfo.  # noqa: E501

        include tier information  # noqa: E501

        :return: The capacity_usage_details of this StatsSystemInfo.  # noqa: E501
        :rtype: list[CapacityUsageDetails]
        """
        return self._capacity_usage_details

    @capacity_usage_details.setter
    def capacity_usage_details(self, capacity_usage_details):
        """Sets the capacity_usage_details of this StatsSystemInfo.

        include tier information  # noqa: E501

        :param capacity_usage_details: The capacity_usage_details of this StatsSystemInfo.  # noqa: E501
        :type: list[CapacityUsageDetails]
        """

        self._capacity_usage_details = capacity_usage_details

    @property
    def subscribed_capacity(self):
        """Gets the subscribed_capacity of this StatsSystemInfo.  # noqa: E501


        :return: The subscribed_capacity of this StatsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._subscribed_capacity

    @subscribed_capacity.setter
    def subscribed_capacity(self, subscribed_capacity):
        """Sets the subscribed_capacity of this StatsSystemInfo.


        :param subscribed_capacity: The subscribed_capacity of this StatsSystemInfo.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                subscribed_capacity is not None and subscribed_capacity < 0):  # noqa: E501
            raise ValueError("Invalid value for `subscribed_capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._subscribed_capacity = subscribed_capacity

    @property
    def license(self):
        """Gets the license of this StatsSystemInfo.  # noqa: E501


        :return: The license of this StatsSystemInfo.  # noqa: E501
        :rtype: list[LicenseInfo]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this StatsSystemInfo.


        :param license: The license of this StatsSystemInfo.  # noqa: E501
        :type: list[LicenseInfo]
        """

        self._license = license

    @property
    def location(self):
        """Gets the location of this StatsSystemInfo.  # noqa: E501


        :return: The location of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this StatsSystemInfo.


        :param location: The location of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def uuid(self):
        """Gets the uuid of this StatsSystemInfo.  # noqa: E501


        :return: The uuid of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StatsSystemInfo.


        :param uuid: The uuid of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def system_status(self):
        """Gets the system_status of this StatsSystemInfo.  # noqa: E501

        HA system status.  # noqa: E501

        :return: The system_status of this StatsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_status

    @system_status.setter
    def system_status(self, system_status):
        """Sets the system_status of this StatsSystemInfo.

        HA system status.  # noqa: E501

        :param system_status: The system_status of this StatsSystemInfo.  # noqa: E501
        :type: str
        """

        self._system_status = system_status

    @property
    def link(self):
        """Gets the link of this StatsSystemInfo.  # noqa: E501


        :return: The link of this StatsSystemInfo.  # noqa: E501
        :rtype: list[RestLinkRep]
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this StatsSystemInfo.


        :param link: The link of this StatsSystemInfo.  # noqa: E501
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
        if issubclass(StatsSystemInfo, dict):
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
        if not isinstance(other, StatsSystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsSystemInfo):
            return True

        return self.to_dict() != other.to_dict()
