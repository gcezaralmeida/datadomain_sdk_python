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


class CsrContents(object):
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
        'csr_key_strength': 'int',
        'csr_country': 'str',
        'csr_state': 'str',
        'csr_city': 'str',
        'csr_org_name': 'str',
        'csr_org_unit': 'str',
        'csr_common_name': 'str',
        'csr_basic_constraint': 'str',
        'csr_key_usage': 'str',
        'csr_extended_key_usage': 'str',
        'csr_subject_alt_name': 'str'
    }

    attribute_map = {
        'csr_key_strength': 'csr_key_strength',
        'csr_country': 'csr_country',
        'csr_state': 'csr_state',
        'csr_city': 'csr_city',
        'csr_org_name': 'csr_org_name',
        'csr_org_unit': 'csr_org_unit',
        'csr_common_name': 'csr_common_name',
        'csr_basic_constraint': 'csr_basic_constraint',
        'csr_key_usage': 'csr_key_usage',
        'csr_extended_key_usage': 'csr_extended_key_usage',
        'csr_subject_alt_name': 'csr_subject_alt_name'
    }

    def __init__(self, csr_key_strength=None, csr_country=None, csr_state=None, csr_city=None, csr_org_name=None, csr_org_unit=None, csr_common_name=None, csr_basic_constraint=None, csr_key_usage=None, csr_extended_key_usage=None, csr_subject_alt_name=None, _configuration=None):  # noqa: E501
        """CsrContents - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._csr_key_strength = None
        self._csr_country = None
        self._csr_state = None
        self._csr_city = None
        self._csr_org_name = None
        self._csr_org_unit = None
        self._csr_common_name = None
        self._csr_basic_constraint = None
        self._csr_key_usage = None
        self._csr_extended_key_usage = None
        self._csr_subject_alt_name = None
        self.discriminator = None

        if csr_key_strength is not None:
            self.csr_key_strength = csr_key_strength
        if csr_country is not None:
            self.csr_country = csr_country
        if csr_state is not None:
            self.csr_state = csr_state
        if csr_city is not None:
            self.csr_city = csr_city
        if csr_org_name is not None:
            self.csr_org_name = csr_org_name
        if csr_org_unit is not None:
            self.csr_org_unit = csr_org_unit
        if csr_common_name is not None:
            self.csr_common_name = csr_common_name
        if csr_basic_constraint is not None:
            self.csr_basic_constraint = csr_basic_constraint
        if csr_key_usage is not None:
            self.csr_key_usage = csr_key_usage
        if csr_extended_key_usage is not None:
            self.csr_extended_key_usage = csr_extended_key_usage
        if csr_subject_alt_name is not None:
            self.csr_subject_alt_name = csr_subject_alt_name

    @property
    def csr_key_strength(self):
        """Gets the csr_key_strength of this CsrContents.  # noqa: E501


        :return: The csr_key_strength of this CsrContents.  # noqa: E501
        :rtype: int
        """
        return self._csr_key_strength

    @csr_key_strength.setter
    def csr_key_strength(self, csr_key_strength):
        """Sets the csr_key_strength of this CsrContents.


        :param csr_key_strength: The csr_key_strength of this CsrContents.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                csr_key_strength is not None and csr_key_strength < 0):  # noqa: E501
            raise ValueError("Invalid value for `csr_key_strength`, must be a value greater than or equal to `0`")  # noqa: E501

        self._csr_key_strength = csr_key_strength

    @property
    def csr_country(self):
        """Gets the csr_country of this CsrContents.  # noqa: E501


        :return: The csr_country of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_country

    @csr_country.setter
    def csr_country(self, csr_country):
        """Sets the csr_country of this CsrContents.


        :param csr_country: The csr_country of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_country = csr_country

    @property
    def csr_state(self):
        """Gets the csr_state of this CsrContents.  # noqa: E501


        :return: The csr_state of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_state

    @csr_state.setter
    def csr_state(self, csr_state):
        """Sets the csr_state of this CsrContents.


        :param csr_state: The csr_state of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_state = csr_state

    @property
    def csr_city(self):
        """Gets the csr_city of this CsrContents.  # noqa: E501


        :return: The csr_city of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_city

    @csr_city.setter
    def csr_city(self, csr_city):
        """Sets the csr_city of this CsrContents.


        :param csr_city: The csr_city of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_city = csr_city

    @property
    def csr_org_name(self):
        """Gets the csr_org_name of this CsrContents.  # noqa: E501


        :return: The csr_org_name of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_org_name

    @csr_org_name.setter
    def csr_org_name(self, csr_org_name):
        """Sets the csr_org_name of this CsrContents.


        :param csr_org_name: The csr_org_name of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_org_name = csr_org_name

    @property
    def csr_org_unit(self):
        """Gets the csr_org_unit of this CsrContents.  # noqa: E501


        :return: The csr_org_unit of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_org_unit

    @csr_org_unit.setter
    def csr_org_unit(self, csr_org_unit):
        """Sets the csr_org_unit of this CsrContents.


        :param csr_org_unit: The csr_org_unit of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_org_unit = csr_org_unit

    @property
    def csr_common_name(self):
        """Gets the csr_common_name of this CsrContents.  # noqa: E501


        :return: The csr_common_name of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_common_name

    @csr_common_name.setter
    def csr_common_name(self, csr_common_name):
        """Sets the csr_common_name of this CsrContents.


        :param csr_common_name: The csr_common_name of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_common_name = csr_common_name

    @property
    def csr_basic_constraint(self):
        """Gets the csr_basic_constraint of this CsrContents.  # noqa: E501


        :return: The csr_basic_constraint of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_basic_constraint

    @csr_basic_constraint.setter
    def csr_basic_constraint(self, csr_basic_constraint):
        """Sets the csr_basic_constraint of this CsrContents.


        :param csr_basic_constraint: The csr_basic_constraint of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_basic_constraint = csr_basic_constraint

    @property
    def csr_key_usage(self):
        """Gets the csr_key_usage of this CsrContents.  # noqa: E501


        :return: The csr_key_usage of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_key_usage

    @csr_key_usage.setter
    def csr_key_usage(self, csr_key_usage):
        """Sets the csr_key_usage of this CsrContents.


        :param csr_key_usage: The csr_key_usage of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_key_usage = csr_key_usage

    @property
    def csr_extended_key_usage(self):
        """Gets the csr_extended_key_usage of this CsrContents.  # noqa: E501


        :return: The csr_extended_key_usage of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_extended_key_usage

    @csr_extended_key_usage.setter
    def csr_extended_key_usage(self, csr_extended_key_usage):
        """Sets the csr_extended_key_usage of this CsrContents.


        :param csr_extended_key_usage: The csr_extended_key_usage of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_extended_key_usage = csr_extended_key_usage

    @property
    def csr_subject_alt_name(self):
        """Gets the csr_subject_alt_name of this CsrContents.  # noqa: E501


        :return: The csr_subject_alt_name of this CsrContents.  # noqa: E501
        :rtype: str
        """
        return self._csr_subject_alt_name

    @csr_subject_alt_name.setter
    def csr_subject_alt_name(self, csr_subject_alt_name):
        """Sets the csr_subject_alt_name of this CsrContents.


        :param csr_subject_alt_name: The csr_subject_alt_name of this CsrContents.  # noqa: E501
        :type: str
        """

        self._csr_subject_alt_name = csr_subject_alt_name

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
        if issubclass(CsrContents, dict):
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
        if not isinstance(other, CsrContents):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CsrContents):
            return True

        return self.to_dict() != other.to_dict()