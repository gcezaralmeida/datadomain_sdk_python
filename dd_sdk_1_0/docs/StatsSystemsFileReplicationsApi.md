# dd_sdk_1_0.StatsSystemsFileReplicationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_stats_systems_file_replications_get**](StatsSystemsFileReplicationsApi.md#rest_v10_dd_systems_systemid_stats_systems_file_replications_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/systems/file-replications | Get the managed file replication traffic statistics


# **rest_v10_dd_systems_systemid_stats_systems_file_replications_get**
> FileReplicationStats rest_v10_dd_systems_systemid_stats_systems_file_replications_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, interval=interval, filter=filter, remote_hostname=remote_hostname, exclude_fields=exclude_fields, include_fields=include_fields)

Get the managed file replication traffic statistics

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.StatsSystemsFileReplicationsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
interval = 'interval_example' # str | unit for sample data. ex: hour, day, week. Default value is minimal unit database keeps for this historical data. (optional)
filter = 'filter_example' # str | Use collection_epoch to retrieve the historical stats for a given range of time. ex: filter=collection_epoch=(start_epoch,end_epoch)  @#$type=statsFilterQuery (optional)
remote_hostname = 'remote_hostname_example' # str | Optional parameter pattern for filtering stats by the remote hostname  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get the managed file replication traffic statistics
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_systems_file_replications_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, interval=interval, filter=filter, remote_hostname=remote_hostname, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsSystemsFileReplicationsApi->rest_v10_dd_systems_systemid_stats_systems_file_replications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **interval** | **str**| unit for sample data. ex: hour, day, week. Default value is minimal unit database keeps for this historical data. | [optional] 
 **filter** | **str**| Use collection_epoch to retrieve the historical stats for a given range of time. ex: filter&#x3D;collection_epoch&#x3D;(start_epoch,end_epoch)  @#$type&#x3D;statsFilterQuery | [optional] 
 **remote_hostname** | **str**| Optional parameter pattern for filtering stats by the remote hostname  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**FileReplicationStats**](FileReplicationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

