# dd_sdk_1_0.StatsPerformancesMtreesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get**](StatsPerformancesMtreesApi.md#rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get) | **GET** /rest/v3.0/dd-systems/{SYSTEM-ID}/stats/performances/mtrees/{ID} | Get an MTree Performance details.


# **rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get**
> MtreeShowPerformanceDetails rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, interval=interval, last=last, start=start, end=end, exclude_fields=exclude_fields, include_fields=include_fields)

Get an MTree Performance details.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.StatsPerformancesMtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
interval = 'interval_example' # str | Interval in mins and hours, min Acceptable Values for interval are [ 1mins, 10mins, 1hours, 24hours]  @#$type=xs:string (optional)
last = 'last_example' # str | last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string (optional)
start = 'start_example' # str | last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string (optional)
end = 'end_example' # str | last <n>{hours | days | weeks | months} | start <MMDDhhmm[[CC]YY] [end <MMDDhhmm[[CC]YY]>]  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get an MTree Performance details.
    api_response = api_instance.rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, interval=interval, last=last, start=start, end=end, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsPerformancesMtreesApi->rest_v30_dd_systems_systemid_stats_performances_mtrees_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **interval** | **str**| Interval in mins and hours, min Acceptable Values for interval are [ 1mins, 10mins, 1hours, 24hours]  @#$type&#x3D;xs:string | [optional] 
 **last** | **str**| last &lt;n&gt;{hours | days | weeks | months} | start &lt;MMDDhhmm[[CC]YY] [end &lt;MMDDhhmm[[CC]YY]&gt;]  @#$type&#x3D;xs:string | [optional] 
 **start** | **str**| last &lt;n&gt;{hours | days | weeks | months} | start &lt;MMDDhhmm[[CC]YY] [end &lt;MMDDhhmm[[CC]YY]&gt;]  @#$type&#x3D;xs:string | [optional] 
 **end** | **str**| last &lt;n&gt;{hours | days | weeks | months} | start &lt;MMDDhhmm[[CC]YY] [end &lt;MMDDhhmm[[CC]YY]&gt;]  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeShowPerformanceDetails**](MtreeShowPerformanceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

