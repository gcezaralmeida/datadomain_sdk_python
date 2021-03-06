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


class StatsPerformancesMtreesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get(self, system_id, id, **kwargs):  # noqa: E501
        """Get an MTree Performance details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get(system_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: MTree identifier.  @#$type=xs:string (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str interval: Interval in mins and hours, min Acceptable Values for interval are [ 1mins, 10mins, 1hours, 24hours]  @#$type=xs:string
        :param str last: last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string
        :param str start: last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string
        :param str end: last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string
        :param str exclude_fields: Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :param str include_fields: Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :return: MtreeShowPerformanceDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get_with_http_info(system_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get_with_http_info(system_id, id, **kwargs)  # noqa: E501
            return data

    def rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get_with_http_info(self, system_id, id, **kwargs):  # noqa: E501
        """Get an MTree Performance details.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get_with_http_info(system_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: DD system identifier.  @#$type=xs:string (required)
        :param str id: MTree identifier.  @#$type=xs:string (required)
        :param str authorization: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str x_dd_auth_token: Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string
        :param str interval: Interval in mins and hours, min Acceptable Values for interval are [ 1mins, 10mins, 1hours, 24hours]  @#$type=xs:string
        :param str last: last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string
        :param str start: last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string
        :param str end: last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string
        :param str exclude_fields: Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :param str include_fields: Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings
        :return: MtreeShowPerformanceDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'id', 'authorization', 'x_dd_auth_token', 'interval', 'last', 'start', 'end', 'exclude_fields', 'include_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if self.api_client.client_side_validation and ('system_id' not in params or
                                                       params['system_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `system_id` when calling `rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_dd_auth_token' in params and
                                                       len(params['x_dd_auth_token']) < 1):
            raise ValueError("Invalid value for parameter `x_dd_auth_token` when calling `rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('exclude_fields' in params and not re.search(r'^([^,]+,*)+$', params['exclude_fields'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `exclude_fields` when calling `rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get`, must conform to the pattern `/^([^,]+,*)+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('include_fields' in params and not re.search(r'^([^,]+,*)+$', params['include_fields'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `include_fields` when calling `rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get`, must conform to the pattern `/^([^,]+,*)+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['SYSTEM-ID'] = params['system_id']  # noqa: E501
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'last' in params:
            query_params.append(('last', params['last']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
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
            '/rest/v3.0/dd-systems/{SYSTEM-ID}/stats/performances/mtrees/{ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MtreeShowPerformanceDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
