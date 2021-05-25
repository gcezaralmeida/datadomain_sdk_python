# dd_sdk_1_0.VdiskDevgrpsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_get**](VdiskDevgrpsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups | Get VDisk device group information.
[**rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_delete**](VdiskDevgrpsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups/{ID} | Delete a VDisk device group.
[**rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_get**](VdiskDevgrpsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups/{ID} | Get a VDisk device group.
[**rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_put**](VdiskDevgrpsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups/{ID} | Modify a VDisk device group.
[**rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_post**](VdiskDevgrpsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups | Create a VDisk device group.
[**rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_get**](VdiskDevgrpsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups | Get VDisk device group information.
[**rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_id_put**](VdiskDevgrpsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups/{ID} | Modify a VDisk device group.
[**rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_post**](VdiskDevgrpsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/device-groups | Create a VDisk device group.


# **rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_get**
> VdiskDevgrpInfos rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk device group information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,pool_name\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskDevgrpSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and pool_name=value\". value should be a valid regular expression.  @#$type=vdiskDevgrpFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk device group information.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,pool_name\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskDevgrpSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and pool_name&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskDevgrpFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDevgrpInfos**](VdiskDevgrpInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively)

Delete a VDisk device group.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device group identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
delete_recursively = true # bool | default value is false. When delete_recursively flag is set, force delete subobjects recursively under the devcie group and destroy the device group.  @#$type=xs:boolean (optional)

try:
    # Delete a VDisk device group.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device group identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **delete_recursively** | **bool**| default value is false. When delete_recursively flag is set, force delete subobjects recursively under the devcie group and destroy the device group.  @#$type&#x3D;xs:boolean | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_get**
> VdiskDevgrpInfoDetail rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk device group.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device group identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk device group.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device group identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDevgrpInfoDetail**](VdiskDevgrpInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_put**
> VdiskDevgrpInfo rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_put(system_id, id, vdisk_devgrp_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk device group.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device group identifier.  @#$type=xs:string
vdisk_devgrp_modify = dd_sdk_1_0.VdiskDevgrpModify() # VdiskDevgrpModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk device group.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_put(system_id, id, vdisk_devgrp_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device group identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devgrp_modify** | [**VdiskDevgrpModify**](VdiskDevgrpModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDevgrpInfo**](VdiskDevgrpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_post**
> VdiskDevgrpInfo rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_post(system_id, vdisk_devgrp_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a VDisk device group.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_devgrp_create = dd_sdk_1_0.VdiskDevgrpCreate() # VdiskDevgrpCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a VDisk device group.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_post(system_id, vdisk_devgrp_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v10_dd_systems_systemid_protocols_vdisk_device_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devgrp_create** | [**VdiskDevgrpCreate**](VdiskDevgrpCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDevgrpInfo**](VdiskDevgrpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_get**
> VdiskDevgrpInfos rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk device group information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,pool_name\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskDevgrpSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and pool_name=value\". value should be a valid regular expression.  @#$type=vdiskDevgrpFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk device group information.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,pool_name\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskDevgrpSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and pool_name&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskDevgrpFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDevgrpInfos**](VdiskDevgrpInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_id_put**
> VdiskDevgrpInfo rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_id_put(system_id, id, vdisk_devgrp_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk device group.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device group identifier.  @#$type=xs:string
vdisk_devgrp_modify_2_0 = dd_sdk_1_0.VdiskDevgrpModify20() # VdiskDevgrpModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk device group.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_id_put(system_id, id, vdisk_devgrp_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device group identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devgrp_modify_2_0** | [**VdiskDevgrpModify20**](VdiskDevgrpModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDevgrpInfo**](VdiskDevgrpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_post**
> VdiskDevgrpInfo rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_post(system_id, vdisk_devgrp_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a VDisk device group.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevgrpsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_devgrp_create = dd_sdk_1_0.VdiskDevgrpCreate() # VdiskDevgrpCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a VDisk device group.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_post(system_id, vdisk_devgrp_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevgrpsApi->rest_v20_dd_systems_systemid_protocols_vdisk_device_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devgrp_create** | [**VdiskDevgrpCreate**](VdiskDevgrpCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDevgrpInfo**](VdiskDevgrpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

