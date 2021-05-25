# dd_sdk_1_0.VdiskPoolsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_vdisk_pools_get**](VdiskPoolsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_pools_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/pools | Get VDisk pool information.
[**rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_delete**](VdiskPoolsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/pools/{ID} | Delete a VDisk pool.
[**rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_get**](VdiskPoolsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/pools/{ID} | Get a VDisk pool.
[**rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_put**](VdiskPoolsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/pools/{ID} | Modify a VDisk pool.
[**rest_v10_dd_systems_systemid_protocols_vdisk_pools_post**](VdiskPoolsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_pools_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/pools | Create a VDisk pool.
[**rest_v20_dd_systems_systemid_protocols_vdisk_pools_id_put**](VdiskPoolsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_pools_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/pools/{ID} | Modify a VDisk pool.


# **rest_v10_dd_systems_systemid_protocols_vdisk_pools_get**
> VdiskPoolInfos rest_v10_dd_systems_systemid_protocols_vdisk_pools_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk pool information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskPoolsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskPoolSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=vdiskPoolFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk pool information.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_pools_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskPoolsApi->rest_v10_dd_systems_systemid_protocols_vdisk_pools_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,user\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskPoolSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and user&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskPoolFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskPoolInfos**](VdiskPoolInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively)

Delete a VDisk pool.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskPoolsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk pool identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
delete_recursively = true # bool | default value is false. When delete_recursively flag is set, force delete subobjects recursively under the pool and destroy the pool.  @#$type=xs:boolean (optional)

try:
    # Delete a VDisk pool.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskPoolsApi->rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk pool identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **delete_recursively** | **bool**| default value is false. When delete_recursively flag is set, force delete subobjects recursively under the pool and destroy the pool.  @#$type&#x3D;xs:boolean | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_get**
> VdiskPoolInfoDetail rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk pool.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskPoolsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk pool identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk pool.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskPoolsApi->rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk pool identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskPoolInfoDetail**](VdiskPoolInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_put**
> VdiskPoolInfo rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_put(system_id, id, vdisk_pool_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk pool.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskPoolsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk pool identifier.  @#$type=xs:string
vdisk_pool_modify = dd_sdk_1_0.VdiskPoolModify() # VdiskPoolModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk pool.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_put(system_id, id, vdisk_pool_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskPoolsApi->rest_v10_dd_systems_systemid_protocols_vdisk_pools_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk pool identifier.  @#$type&#x3D;xs:string | 
 **vdisk_pool_modify** | [**VdiskPoolModify**](VdiskPoolModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskPoolInfo**](VdiskPoolInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_pools_post**
> VdiskPoolInfo rest_v10_dd_systems_systemid_protocols_vdisk_pools_post(system_id, vdisk_pool_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a VDisk pool.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskPoolsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_pool_create = dd_sdk_1_0.VdiskPoolCreate() # VdiskPoolCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a VDisk pool.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_pools_post(system_id, vdisk_pool_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskPoolsApi->rest_v10_dd_systems_systemid_protocols_vdisk_pools_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_pool_create** | [**VdiskPoolCreate**](VdiskPoolCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskPoolInfo**](VdiskPoolInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_pools_id_put**
> VdiskPoolInfo rest_v20_dd_systems_systemid_protocols_vdisk_pools_id_put(system_id, id, vdisk_pool_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk pool.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskPoolsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk pool identifier.  @#$type=xs:string
vdisk_pool_modify_2_0 = dd_sdk_1_0.VdiskPoolModify20() # VdiskPoolModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk pool.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_pools_id_put(system_id, id, vdisk_pool_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskPoolsApi->rest_v20_dd_systems_systemid_protocols_vdisk_pools_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk pool identifier.  @#$type&#x3D;xs:string | 
 **vdisk_pool_modify_2_0** | [**VdiskPoolModify20**](VdiskPoolModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskPoolInfo**](VdiskPoolInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

