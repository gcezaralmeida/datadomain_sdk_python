# dd_sdk_1_0.FilesysStatsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_stats_file_systems_get**](FilesysStatsApi.md#rest_v10_dd_systems_systemid_stats_file_systems_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/file-systems | File System show stats.


# **rest_v10_dd_systems_systemid_stats_file_systems_get**
> FilesysStatsInfos rest_v10_dd_systems_systemid_stats_file_systems_get(system_id, tier, need_delta, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, start_time=start_time, end_time=end_time, exclude_fields=exclude_fields, include_fields=include_fields)

File System show stats.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.FilesysStatsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
tier = 'tier_example' # str | Tier type: all, active, archive or cloud. If not specified or all, all applicable tiers are displayed.
need_delta = true # bool | By default stats absolute values are reported. If set to true then deltas will be reported.  @#$type=xs:boolean
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
start_time = 56 # int | time in epoch, starting from 0  @#$type=xs:unsignedInt (optional)
end_time = 56 # int | time in epoch, starting from 0  @#$type=xs:unsignedInt (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # File System show stats.
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_file_systems_get(system_id, tier, need_delta, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, start_time=start_time, end_time=end_time, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesysStatsApi->rest_v10_dd_systems_systemid_stats_file_systems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **tier** | **str**| Tier type: all, active, archive or cloud. If not specified or all, all applicable tiers are displayed. | 
 **need_delta** | **bool**| By default stats absolute values are reported. If set to true then deltas will be reported.  @#$type&#x3D;xs:boolean | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **start_time** | **int**| time in epoch, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **end_time** | **int**| time in epoch, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**FilesysStatsInfos**](FilesysStatsInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

