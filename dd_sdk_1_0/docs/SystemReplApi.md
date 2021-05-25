# dd_sdk_1_0.SystemReplApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_dd_systems_systemid_systems_stats_repl_get**](SystemReplApi.md#rest_v20_dd_systems_systemid_systems_stats_repl_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/systems/stats/repl | Get system repl stats.


# **rest_v20_dd_systems_systemid_systems_stats_repl_get**
> SystemReplStatsInfos rest_v20_dd_systems_systemid_systems_stats_repl_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, start_time=start_time, end_time=end_time, page=page, size=size, exclude_fields=exclude_fields, include_fields=include_fields)

Get system repl stats.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SystemReplApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
start_time = 56 # int | time in epoch, starting from 0  @#$type=xs:unsignedInt (optional)
end_time = 56 # int | time in epoch, starting from 0  @#$type=xs:unsignedInt (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get system repl stats.
    api_response = api_instance.rest_v20_dd_systems_systemid_systems_stats_repl_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, start_time=start_time, end_time=end_time, page=page, size=size, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemReplApi->rest_v20_dd_systems_systemid_systems_stats_repl_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **start_time** | **int**| time in epoch, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **end_time** | **int**| time in epoch, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**SystemReplStatsInfos**](SystemReplStatsInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

