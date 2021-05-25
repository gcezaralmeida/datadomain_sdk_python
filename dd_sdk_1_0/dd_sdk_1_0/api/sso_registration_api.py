# coding: utf-8

"""
    DataDomain Rest API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dd_sdk_1_0.api_client import ApiClient


class SsoRegistrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rest_v10_sso_registration_id_delete(self, id, **kwargs):  # noqa: E501
        """Delete OIDC provider info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_sso_registration_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: SSO client identifier.  @#$type=xs:string (required)
        :return: RegistrationDeleteStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_sso_registration_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_sso_registration_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def rest_v10_sso_registration_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete OIDC provider info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_sso_registration_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: SSO client identifier.  @#$type=xs:string (required)
        :return: RegistrationDeleteStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_sso_registration_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `rest_v10_sso_registration_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/sso-registration/{ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegistrationDeleteStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v10_sso_registration_id_put(self, id, registration_info, **kwargs):  # noqa: E501
        """Update OIDC provider info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_sso_registration_id_put(id, registration_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: SSO client identifier.  @#$type=xs:string (required)
        :param RegistrationInfo registration_info: (required)
        :return: RegistrationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_sso_registration_id_put_with_http_info(id, registration_info, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_sso_registration_id_put_with_http_info(id, registration_info, **kwargs)  # noqa: E501
            return data

    def rest_v10_sso_registration_id_put_with_http_info(self, id, registration_info, **kwargs):  # noqa: E501
        """Update OIDC provider info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_sso_registration_id_put_with_http_info(id, registration_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: SSO client identifier.  @#$type=xs:string (required)
        :param RegistrationInfo registration_info: (required)
        :return: RegistrationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'registration_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_sso_registration_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `rest_v10_sso_registration_id_put`")  # noqa: E501
        # verify the required parameter 'registration_info' is set
        if self.api_client.client_side_validation and ('registration_info' not in params or
                                                       params['registration_info'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `registration_info` when calling `rest_v10_sso_registration_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'registration_info' in params:
            body_params = params['registration_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/sso-registration/{ID}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegistrationStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v10_sso_registration_post(self, registration_info, **kwargs):  # noqa: E501
        """Register DDR to OIDC provider.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_sso_registration_post(registration_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegistrationInfo registration_info: (required)
        :return: RegistrationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_sso_registration_post_with_http_info(registration_info, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_sso_registration_post_with_http_info(registration_info, **kwargs)  # noqa: E501
            return data

    def rest_v10_sso_registration_post_with_http_info(self, registration_info, **kwargs):  # noqa: E501
        """Register DDR to OIDC provider.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_sso_registration_post_with_http_info(registration_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegistrationInfo registration_info: (required)
        :return: RegistrationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registration_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_sso_registration_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registration_info' is set
        if self.api_client.client_side_validation and ('registration_info' not in params or
                                                       params['registration_info'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `registration_info` when calling `rest_v10_sso_registration_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'registration_info' in params:
            body_params = params['registration_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/sso-registration', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegistrationStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
