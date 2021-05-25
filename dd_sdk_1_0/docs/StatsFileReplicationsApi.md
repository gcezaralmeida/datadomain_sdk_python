# dd_sdk_1_0.StatsFileReplicationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_stats_file_replications_get**](StatsFileReplicationsApi.md#rest_v10_dd_systems_systemid_stats_file_replications_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/file-replications | Get file-replication stats
[**rest_v10_dd_systems_systemid_stats_file_replications_id_get**](StatsFileReplicationsApi.md#rest_v10_dd_systems_systemid_stats_file_replications_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/file-replications/{ID} | Get file-replication details for a storage-unit.


# **rest_v10_dd_systems_systemid_stats_file_replications_get**
> FileReplicationList rest_v10_dd_systems_systemid_stats_file_replications_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get file-replication stats

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.StatsFileReplicationsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"repl_status, direction, local_storage_unit, destination_hostname, destination_storage_unit, active_files\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=fileReplicationSortQuery (optional)
filter = 'filter_example' # str | filter=\"repl_status=completed|error|warning|unknown and direction=inbound|outbound and local_storage_unit and destination_hostname and destination_storage_unit and active_files\". value should be a valid regular expression.  @#$type=fileReplicationFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get file-replication stats
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_file_replications_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsFileReplicationsApi->rest_v10_dd_systems_systemid_stats_file_replications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;repl_status, direction, local_storage_unit, destination_hostname, destination_storage_unit, active_files\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;fileReplicationSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;repl_status&#x3D;completed|error|warning|unknown and direction&#x3D;inbound|outbound and local_storage_unit and destination_hostname and destination_storage_unit and active_files\&quot;. value should be a valid regular expression.  @#$type&#x3D;fileReplicationFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**FileReplicationList**](FileReplicationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_stats_file_replications_id_get**
> FileReplicationList rest_v10_dd_systems_systemid_stats_file_replications_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, interval=interval, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get file-replication details for a storage-unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.StatsFileReplicationsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ID is a combination of local-folder:remote-host:remote-folder  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
interval = 'interval_example' # str | unit for sample data. ex: hour, day, week, month. Default value is minimal unit database keeps for this historical data. (optional)
filter = 'filter_example' # str | Use collection_epoch to retrieve the historical stats for a given range of time. ex: filter=collection_epoch=(start_epoch,end_epoch)  @#$type=statsFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get file-replication details for a storage-unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_file_replications_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, interval=interval, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsFileReplicationsApi->rest_v10_dd_systems_systemid_stats_file_replications_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ID is a combination of local-folder:remote-host:remote-folder  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **interval** | **str**| unit for sample data. ex: hour, day, week, month. Default value is minimal unit database keeps for this historical data. | [optional] 
 **filter** | **str**| Use collection_epoch to retrieve the historical stats for a given range of time. ex: filter&#x3D;collection_epoch&#x3D;(start_epoch,end_epoch)  @#$type&#x3D;statsFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**FileReplicationList**](FileReplicationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

