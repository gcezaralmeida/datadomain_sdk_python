# dd_sdk_1_0.MtreeIdStatsCompressionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v30_dd_systems_systemid_mtrees_id_stats_compressions_get**](MtreeIdStatsCompressionsApi.md#rest_v30_dd_systems_systemid_mtrees_id_stats_compressions_get) | **GET** /rest/v3.0/dd-systems/{SYSTEM-ID}/mtrees/{ID}/stats/compressions | Get Compression info for an MTree.


# **rest_v30_dd_systems_systemid_mtrees_id_stats_compressions_get**
> MtreeCompressionInfoDetails rest_v30_dd_systems_systemid_mtrees_id_stats_compressions_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, tier=tier, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get Compression info for an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreeIdStatsCompressionsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | mtree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
tier = 'tier_example' # str | Tier type: active, archive or cloud, total. If not specified, active tier info will be displayed.If total is specified all applicable tiers are displayed (optional)
filter = 'filter_example' # str | filter=\"collection_epoch=(start_epoch,end_epoch)\". Collection_epoch can not be repeated. Value should be a range, eg (start_epoch, end_epoch). Start epoch for historical data, unit is epoch time. Default value is \"0\", returns all historical data for requested interval or sample of minimal unit in db. End epoch for historical data, unit is epoch time. Default value is current epoch time.  @#$type=statsFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get Compression info for an MTree.
    api_response = api_instance.rest_v30_dd_systems_systemid_mtrees_id_stats_compressions_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, tier=tier, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreeIdStatsCompressionsApi->rest_v30_dd_systems_systemid_mtrees_id_stats_compressions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| mtree identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **tier** | **str**| Tier type: active, archive or cloud, total. If not specified, active tier info will be displayed.If total is specified all applicable tiers are displayed | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;collection_epoch&#x3D;(start_epoch,end_epoch)\&quot;. Collection_epoch can not be repeated. Value should be a range, eg (start_epoch, end_epoch). Start epoch for historical data, unit is epoch time. Default value is \&quot;0\&quot;, returns all historical data for requested interval or sample of minimal unit in db. End epoch for historical data, unit is epoch time. Default value is current epoch time.  @#$type&#x3D;statsFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeCompressionInfoDetails**](MtreeCompressionInfoDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

