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


class MdtagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rest_v10_dd_systems_systemid_mdtags_get(self, system_id, **kwargs):  # noqa: E501
        """Retrieve list of objects matching supplied tag name, value, or time criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_get(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param int page: page number, starting from 0  @#$type=xs:unsignedInt
        :param int size: Paging size  @#$type=xs:unsignedInt
        :param str sort: sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=mdtagSortQuery
        :param str filter: filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=mdtagFilterQuery
        :param str tag_scope: Scope of tagdata to retrieve.  @#$type=mdtagGetFlags
        :param str exclude_fields: Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :param str include_fields: Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :return: MdtagObjectDetailList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_dd_systems_systemid_mdtags_get_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_dd_systems_systemid_mdtags_get_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def rest_v10_dd_systems_systemid_mdtags_get_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """Retrieve list of objects matching supplied tag name, value, or time criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_get_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param int page: page number, starting from 0  @#$type=xs:unsignedInt
        :param int size: Paging size  @#$type=xs:unsignedInt
        :param str sort: sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=mdtagSortQuery
        :param str filter: filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=mdtagFilterQuery
        :param str tag_scope: Scope of tagdata to retrieve.  @#$type=mdtagGetFlags
        :param str exclude_fields: Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :param str include_fields: Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :return: MdtagObjectDetailList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'authorization', 'x_dd_auth_token', 'page', 'size', 'sort', 'filter', 'tag_scope', 'exclude_fields', 'include_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_dd_systems_systemid_mdtags_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if self.api_client.client_side_validation and ('system_id' not in params or
                                                       params['system_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `system_id` when calling `rest_v10_dd_systems_systemid_mdtags_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_dd_auth_token' in params and
                                                       len(params['x_dd_auth_token']) < 1):
            raise ValueError("Invalid value for parameter `x_dd_auth_token` when calling `rest_v10_dd_systems_systemid_mdtags_get`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `rest_v10_dd_systems_systemid_mdtags_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('size' in params and params['size'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `size` when calling `rest_v10_dd_systems_systemid_mdtags_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('sort' in params and not re.search(r'^(\\s*-?(name|namespace)\\s*,)*\\s*-?(name|namespace)\\s*$', params['sort'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `sort` when calling `rest_v10_dd_systems_systemid_mdtags_get`, must conform to the pattern `/^(\\s*-?(name|namespace)\\s*,)*\\s*-?(name|namespace)\\s*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in params and not re.search(r'^\\s*(tag){1}\\s*([:,!])+', params['filter'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `filter` when calling `rest_v10_dd_systems_systemid_mdtags_get`, must conform to the pattern `/^\\s*(tag){1}\\s*([:,!])+/`")  # noqa: E501
        if self.api_client.client_side_validation and ('exclude_fields' in params and not re.search(r'^([^,]+,*)+$', params['exclude_fields'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `exclude_fields` when calling `rest_v10_dd_systems_systemid_mdtags_get`, must conform to the pattern `/^([^,]+,*)+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('include_fields' in params and not re.search(r'^([^,]+,*)+$', params['include_fields'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `include_fields` when calling `rest_v10_dd_systems_systemid_mdtags_get`, must conform to the pattern `/^([^,]+,*)+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['SYSTEM-ID'] = params['system_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'tag_scope' in params:
            query_params.append(('tag_scope', params['tag_scope']))  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
        if 'include_fields' in params:
            query_params.append(('include_fields', params['include_fields']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_dd_auth_token' in params:
            header_params['X-DD-AUTH-TOKEN'] = params['x_dd_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MdtagObjectDetailList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v10_dd_systems_systemid_mdtags_id_delete(self, system_id, id, filter, **kwargs):  # noqa: E501
        """Remove object from metadata tag store  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_id_delete(system_id, id, filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: Object identifier.  @#$type=xs:string (required)
        :param str filter: Namespace must be specified for the object target.  @#$type=mdtagIdFilterQuery (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :return: ServiceStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_dd_systems_systemid_mdtags_id_delete_with_http_info(system_id, id, filter, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_dd_systems_systemid_mdtags_id_delete_with_http_info(system_id, id, filter, **kwargs)  # noqa: E501
            return data

    def rest_v10_dd_systems_systemid_mdtags_id_delete_with_http_info(self, system_id, id, filter, **kwargs):  # noqa: E501
        """Remove object from metadata tag store  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_id_delete_with_http_info(system_id, id, filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: Object identifier.  @#$type=xs:string (required)
        :param str filter: Namespace must be specified for the object target.  @#$type=mdtagIdFilterQuery (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :return: ServiceStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'id', 'filter', 'authorization', 'x_dd_auth_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_dd_systems_systemid_mdtags_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if self.api_client.client_side_validation and ('system_id' not in params or
                                                       params['system_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `system_id` when calling `rest_v10_dd_systems_systemid_mdtags_id_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `rest_v10_dd_systems_systemid_mdtags_id_delete`")  # noqa: E501
        # verify the required parameter 'filter' is set
        if self.api_client.client_side_validation and ('filter' not in params or
                                                       params['filter'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `filter` when calling `rest_v10_dd_systems_systemid_mdtags_id_delete`")  # noqa: E501

        if self.api_client.client_side_validation and ('filter' in params and not re.search(r'^\\s*(namespace)\\s*=\\s*\\S*\\s*$', params['filter'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `filter` when calling `rest_v10_dd_systems_systemid_mdtags_id_delete`, must conform to the pattern `/^\\s*(namespace)\\s*=\\s*\\S*\\s*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('x_dd_auth_token' in params and
                                                       len(params['x_dd_auth_token']) < 1):
            raise ValueError("Invalid value for parameter `x_dd_auth_token` when calling `rest_v10_dd_systems_systemid_mdtags_id_delete`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['SYSTEM-ID'] = params['system_id']  # noqa: E501
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_dd_auth_token' in params:
            header_params['X-DD-AUTH-TOKEN'] = params['x_dd_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags/{ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v10_dd_systems_systemid_mdtags_id_get(self, system_id, id, filter, **kwargs):  # noqa: E501
        """Get the set of tags for an object.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_id_get(system_id, id, filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: Object identifier.  @#$type=xs:string (required)
        :param str filter: filter=\"namespace=value\". value should be a valid namespace string.  @#$type=mdtagIdFilterQuery (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str tag_scope: Scope of tagdata to retrieve.  @#$type=mdtagGetFlags
        :param str exclude_fields: Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :param str include_fields: Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :return: MdtagObjectDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_dd_systems_systemid_mdtags_id_get_with_http_info(system_id, id, filter, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_dd_systems_systemid_mdtags_id_get_with_http_info(system_id, id, filter, **kwargs)  # noqa: E501
            return data

    def rest_v10_dd_systems_systemid_mdtags_id_get_with_http_info(self, system_id, id, filter, **kwargs):  # noqa: E501
        """Get the set of tags for an object.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_id_get_with_http_info(system_id, id, filter, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: Object identifier.  @#$type=xs:string (required)
        :param str filter: filter=\"namespace=value\". value should be a valid namespace string.  @#$type=mdtagIdFilterQuery (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str tag_scope: Scope of tagdata to retrieve.  @#$type=mdtagGetFlags
        :param str exclude_fields: Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :param str include_fields: Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :return: MdtagObjectDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'id', 'filter', 'authorization', 'x_dd_auth_token', 'tag_scope', 'exclude_fields', 'include_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_dd_systems_systemid_mdtags_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if self.api_client.client_side_validation and ('system_id' not in params or
                                                       params['system_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `system_id` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`")  # noqa: E501
        # verify the required parameter 'filter' is set
        if self.api_client.client_side_validation and ('filter' not in params or
                                                       params['filter'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `filter` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('filter' in params and not re.search(r'^\\s*(namespace)\\s*=\\s*\\S*\\s*$', params['filter'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `filter` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`, must conform to the pattern `/^\\s*(namespace)\\s*=\\s*\\S*\\s*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('x_dd_auth_token' in params and
                                                       len(params['x_dd_auth_token']) < 1):
            raise ValueError("Invalid value for parameter `x_dd_auth_token` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('exclude_fields' in params and not re.search(r'^([^,]+,*)+$', params['exclude_fields'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `exclude_fields` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`, must conform to the pattern `/^([^,]+,*)+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('include_fields' in params and not re.search(r'^([^,]+,*)+$', params['include_fields'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `include_fields` when calling `rest_v10_dd_systems_systemid_mdtags_id_get`, must conform to the pattern `/^([^,]+,*)+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['SYSTEM-ID'] = params['system_id']  # noqa: E501
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'tag_scope' in params:
            query_params.append(('tag_scope', params['tag_scope']))  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
        if 'include_fields' in params:
            query_params.append(('include_fields', params['include_fields']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_dd_auth_token' in params:
            header_params['X-DD-AUTH-TOKEN'] = params['x_dd_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags/{ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MdtagObjectDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v10_dd_systems_systemid_mdtags_id_put(self, system_id, id, mdtag_object_modify, **kwargs):  # noqa: E501
        """Set or clear a set of metadata tags for an object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_id_put(system_id, id, mdtag_object_modify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: Object identifier.  @#$type=xs:string (required)
        :param MdtagObjectModify mdtag_object_modify: (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :return: MdtagObjectIdentity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v10_dd_systems_systemid_mdtags_id_put_with_http_info(system_id, id, mdtag_object_modify, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v10_dd_systems_systemid_mdtags_id_put_with_http_info(system_id, id, mdtag_object_modify, **kwargs)  # noqa: E501
            return data

    def rest_v10_dd_systems_systemid_mdtags_id_put_with_http_info(self, system_id, id, mdtag_object_modify, **kwargs):  # noqa: E501
        """Set or clear a set of metadata tags for an object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v10_dd_systems_systemid_mdtags_id_put_with_http_info(system_id, id, mdtag_object_modify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: Object identifier.  @#$type=xs:string (required)
        :param MdtagObjectModify mdtag_object_modify: (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :return: MdtagObjectIdentity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'id', 'mdtag_object_modify', 'authorization', 'x_dd_auth_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v10_dd_systems_systemid_mdtags_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if self.api_client.client_side_validation and ('system_id' not in params or
                                                       params['system_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `system_id` when calling `rest_v10_dd_systems_systemid_mdtags_id_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `rest_v10_dd_systems_systemid_mdtags_id_put`")  # noqa: E501
        # verify the required parameter 'mdtag_object_modify' is set
        if self.api_client.client_side_validation and ('mdtag_object_modify' not in params or
                                                       params['mdtag_object_modify'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mdtag_object_modify` when calling `rest_v10_dd_systems_systemid_mdtags_id_put`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_dd_auth_token' in params and
                                                       len(params['x_dd_auth_token']) < 1):
            raise ValueError("Invalid value for parameter `x_dd_auth_token` when calling `rest_v10_dd_systems_systemid_mdtags_id_put`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['SYSTEM-ID'] = params['system_id']  # noqa: E501
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_dd_auth_token' in params:
            header_params['X-DD-AUTH-TOKEN'] = params['x_dd_auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'mdtag_object_modify' in params:
            body_params = params['mdtag_object_modify']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags/{ID}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MdtagObjectIdentity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)