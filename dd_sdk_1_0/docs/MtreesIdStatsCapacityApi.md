# dd_sdk_1_0.MtreesIdStatsCapacityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_dd_systems_systemid_mtrees_id_stats_capacity_get**](MtreesIdStatsCapacityApi.md#rest_v20_dd_systems_systemid_mtrees_id_stats_capacity_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/mtrees/{ID}/stats/capacity | Get mtree level capacity stats detail.


# **rest_v20_dd_systems_systemid_mtrees_id_stats_capacity_get**
> MtreeStatsCapacityInfos rest_v20_dd_systems_systemid_mtrees_id_stats_capacity_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, tier=tier, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get mtree level capacity stats detail.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesIdStatsCapacityApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
tier = 'tier_example' # str | Tier type: all, active, archive or cloud. If not specified or all, all applicable tiers are displayed. (optional)
sort = 'sort_example' # str | sort=\"collection_epoch\". Default is descending order. For descending order, prefix the key with a dash (-). Ex: -collection_epoch  @#$type=statsSortQuery (optional)
filter = 'filter_example' # str | filter=\"collection_epoch=value\". Collection_epoch can not be repeated. Value should be a range, eg (start_time, end_time). Start time for historical data, unit is epoch time. Default value is \"0\", which means last 7 days from the end time. End time for historical data, unit is epoch time. Default value is current epoch time.  @#$type=statsFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get mtree level capacity stats detail.
    api_response = api_instance.rest_v20_dd_systems_systemid_mtrees_id_stats_capacity_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, tier=tier, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesIdStatsCapacityApi->rest_v20_dd_systems_systemid_mtrees_id_stats_capacity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **tier** | **str**| Tier type: all, active, archive or cloud. If not specified or all, all applicable tiers are displayed. | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;collection_epoch\&quot;. Default is descending order. For descending order, prefix the key with a dash (-). Ex: -collection_epoch  @#$type&#x3D;statsSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;collection_epoch&#x3D;value\&quot;. Collection_epoch can not be repeated. Value should be a range, eg (start_time, end_time). Start time for historical data, unit is epoch time. Default value is \&quot;0\&quot;, which means last 7 days from the end time. End time for historical data, unit is epoch time. Default value is current epoch time.  @#$type&#x3D;statsFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeStatsCapacityInfos**](MtreeStatsCapacityInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

