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


class RegistrationInfo(object):
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
        'client_secret': 'str',
        'client_id': 'str',
        'client_name': 'str',
        'token_endpoint_auth_method': 'str',
        'auto_config_uri': 'str',
        'id_token_signed_response_alg': 'str',
        'redirect_uris': 'list[str]',
        'registration_client_uri': 'str',
        'application_type': 'str',
        'scope': 'str',
        'response_types': 'list[str]',
        'grant_types': 'list[str]',
        'data': 'RegistrationData'
    }

    attribute_map = {
        'client_secret': 'client_secret',
        'client_id': 'client_id',
        'client_name': 'client_name',
        'token_endpoint_auth_method': 'token_endpoint_auth_method',
        'auto_config_uri': 'auto_config_uri',
        'id_token_signed_response_alg': 'id_token_signed_response_alg',
        'redirect_uris': 'redirect_uris',
        'registration_client_uri': 'registration_client_uri',
        'application_type': 'application_type',
        'scope': 'scope',
        'response_types': 'response_types',
        'grant_types': 'grant_types',
        'data': 'data'
    }

    def __init__(self, client_secret=None, client_id=None, client_name=None, token_endpoint_auth_method=None, auto_config_uri=None, id_token_signed_response_alg=None, redirect_uris=None, registration_client_uri=None, application_type=None, scope=None, response_types=None, grant_types=None, data=None, _configuration=None):  # noqa: E501
        """RegistrationInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_secret = None
        self._client_id = None
        self._client_name = None
        self._token_endpoint_auth_method = None
        self._auto_config_uri = None
        self._id_token_signed_response_alg = None
        self._redirect_uris = None
        self._registration_client_uri = None
        self._application_type = None
        self._scope = None
        self._response_types = None
        self._grant_types = None
        self._data = None
        self.discriminator = None

        self.client_secret = client_secret
        self.client_id = client_id
        self.client_name = client_name
        if token_endpoint_auth_method is not None:
            self.token_endpoint_auth_method = token_endpoint_auth_method
        self.auto_config_uri = auto_config_uri
        if id_token_signed_response_alg is not None:
            self.id_token_signed_response_alg = id_token_signed_response_alg
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        if registration_client_uri is not None:
            self.registration_client_uri = registration_client_uri
        if application_type is not None:
            self.application_type = application_type
        if scope is not None:
            self.scope = scope
        if response_types is not None:
            self.response_types = response_types
        if grant_types is not None:
            self.grant_types = grant_types
        if data is not None:
            self.data = data

    @property
    def client_secret(self):
        """Gets the client_secret of this RegistrationInfo.  # noqa: E501


        :return: The client_secret of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this RegistrationInfo.


        :param client_secret: The client_secret of this RegistrationInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def client_id(self):
        """Gets the client_id of this RegistrationInfo.  # noqa: E501


        :return: The client_id of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RegistrationInfo.


        :param client_id: The client_id of this RegistrationInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this RegistrationInfo.  # noqa: E501


        :return: The client_name of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this RegistrationInfo.


        :param client_name: The client_name of this RegistrationInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_name is None:
            raise ValueError("Invalid value for `client_name`, must not be `None`")  # noqa: E501

        self._client_name = client_name

    @property
    def token_endpoint_auth_method(self):
        """Gets the token_endpoint_auth_method of this RegistrationInfo.  # noqa: E501


        :return: The token_endpoint_auth_method of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._token_endpoint_auth_method

    @token_endpoint_auth_method.setter
    def token_endpoint_auth_method(self, token_endpoint_auth_method):
        """Sets the token_endpoint_auth_method of this RegistrationInfo.


        :param token_endpoint_auth_method: The token_endpoint_auth_method of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._token_endpoint_auth_method = token_endpoint_auth_method

    @property
    def auto_config_uri(self):
        """Gets the auto_config_uri of this RegistrationInfo.  # noqa: E501


        :return: The auto_config_uri of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._auto_config_uri

    @auto_config_uri.setter
    def auto_config_uri(self, auto_config_uri):
        """Sets the auto_config_uri of this RegistrationInfo.


        :param auto_config_uri: The auto_config_uri of this RegistrationInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and auto_config_uri is None:
            raise ValueError("Invalid value for `auto_config_uri`, must not be `None`")  # noqa: E501

        self._auto_config_uri = auto_config_uri

    @property
    def id_token_signed_response_alg(self):
        """Gets the id_token_signed_response_alg of this RegistrationInfo.  # noqa: E501


        :return: The id_token_signed_response_alg of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._id_token_signed_response_alg

    @id_token_signed_response_alg.setter
    def id_token_signed_response_alg(self, id_token_signed_response_alg):
        """Sets the id_token_signed_response_alg of this RegistrationInfo.


        :param id_token_signed_response_alg: The id_token_signed_response_alg of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._id_token_signed_response_alg = id_token_signed_response_alg

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this RegistrationInfo.  # noqa: E501


        :return: The redirect_uris of this RegistrationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this RegistrationInfo.


        :param redirect_uris: The redirect_uris of this RegistrationInfo.  # noqa: E501
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def registration_client_uri(self):
        """Gets the registration_client_uri of this RegistrationInfo.  # noqa: E501


        :return: The registration_client_uri of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._registration_client_uri

    @registration_client_uri.setter
    def registration_client_uri(self, registration_client_uri):
        """Sets the registration_client_uri of this RegistrationInfo.


        :param registration_client_uri: The registration_client_uri of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._registration_client_uri = registration_client_uri

    @property
    def application_type(self):
        """Gets the application_type of this RegistrationInfo.  # noqa: E501


        :return: The application_type of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this RegistrationInfo.


        :param application_type: The application_type of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._application_type = application_type

    @property
    def scope(self):
        """Gets the scope of this RegistrationInfo.  # noqa: E501


        :return: The scope of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this RegistrationInfo.


        :param scope: The scope of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def response_types(self):
        """Gets the response_types of this RegistrationInfo.  # noqa: E501


        :return: The response_types of this RegistrationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        """Sets the response_types of this RegistrationInfo.


        :param response_types: The response_types of this RegistrationInfo.  # noqa: E501
        :type: list[str]
        """

        self._response_types = response_types

    @property
    def grant_types(self):
        """Gets the grant_types of this RegistrationInfo.  # noqa: E501


        :return: The grant_types of this RegistrationInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this RegistrationInfo.


        :param grant_types: The grant_types of this RegistrationInfo.  # noqa: E501
        :type: list[str]
        """

        self._grant_types = grant_types

    @property
    def data(self):
        """Gets the data of this RegistrationInfo.  # noqa: E501


        :return: The data of this RegistrationInfo.  # noqa: E501
        :rtype: RegistrationData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RegistrationInfo.


        :param data: The data of this RegistrationInfo.  # noqa: E501
        :type: RegistrationData
        """

        self._data = data

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
        if issubclass(RegistrationInfo, dict):
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
        if not isinstance(other, RegistrationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistrationInfo):
            return True

        return self.to_dict() != other.to_dict()
