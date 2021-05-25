# dd_sdk_1_0.VdiskDevicesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_delete**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Delete a list of VDisk devices.
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_get**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Get VDisk device information.
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_delete**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Delete a VDisk device.
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_get**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Get a VDisk device.
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_put**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Modify multiple VDisk devices.
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_post**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Create a VDisk device.
[**rest_v10_dd_systems_systemid_protocols_vdisk_devices_put**](VdiskDevicesApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_devices_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Modify a VDisk device.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_delete**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_delete) | **DELETE** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Delete a list of VDisk devices.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_get**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Get VDisk device information.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_delete**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_delete) | **DELETE** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Delete a VDisk device.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_get**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Get a VDisk device.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_put**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Modify a VDisk device.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_post**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Create a VDisk device.
[**rest_v20_dd_systems_systemid_protocols_vdisk_devices_put**](VdiskDevicesApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_devices_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices | Modify one or more VDisk devices.
[**rest_v30_dd_systems_systemid_protocols_vdisk_devices_id_get**](VdiskDevicesApi.md#rest_v30_dd_systems_systemid_protocols_vdisk_devices_id_get) | **GET** /rest/v3.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/devices/{ID} | Get a VDisk device.


# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_vdisk_devices_delete(system_id, vdisk_devices_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively, delete_device_group_on_empty=delete_device_group_on_empty)

Delete a list of VDisk devices.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_devices_delete = dd_sdk_1_0.VdiskDevicesDelete() # VdiskDevicesDelete | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
delete_recursively = true # bool | default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type=xs:boolean (optional)
delete_device_group_on_empty = true # bool | default value is false. When delete_device_group_on_empty flag is set, force delete the parent device group if empty on last device delete.  @#$type=xs:boolean (optional)

try:
    # Delete a list of VDisk devices.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_delete(system_id, vdisk_devices_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively, delete_device_group_on_empty=delete_device_group_on_empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devices_delete** | [**VdiskDevicesDelete**](VdiskDevicesDelete.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **delete_recursively** | **bool**| default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type&#x3D;xs:boolean | [optional] 
 **delete_device_group_on_empty** | **bool**| default value is false. When delete_device_group_on_empty flag is set, force delete the parent device group if empty on last device delete.  @#$type&#x3D;xs:boolean | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_get**
> VdiskDeviceInfos rest_v10_dd_systems_systemid_protocols_vdisk_devices_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk device information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskDeviceSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=vdiskDeviceFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk device information.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,user\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskDeviceSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and user&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskDeviceFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDeviceInfos**](VdiskDeviceInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively)

Delete a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
delete_recursively = true # bool | default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type=xs:boolean (optional)

try:
    # Delete a VDisk device.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **delete_recursively** | **bool**| default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type&#x3D;xs:boolean | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_get**
> VdiskDeviceInfoDetail rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk device.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDeviceInfoDetail**](VdiskDeviceInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_put**
> VdiskDeviceInfo rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_put(system_id, id, vdisk_device_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify multiple VDisk devices.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
vdisk_device_modify = dd_sdk_1_0.VdiskDeviceModify() # VdiskDeviceModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify multiple VDisk devices.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_put(system_id, id, vdisk_device_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **vdisk_device_modify** | [**VdiskDeviceModify**](VdiskDeviceModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDeviceInfo**](VdiskDeviceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_post**
> VdiskDeviceInfos2 rest_v10_dd_systems_systemid_protocols_vdisk_devices_post(system_id, vdisk_device_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_device_create = dd_sdk_1_0.VdiskDeviceCreate() # VdiskDeviceCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a VDisk device.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_post(system_id, vdisk_device_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_device_create** | [**VdiskDeviceCreate**](VdiskDeviceCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDeviceInfos2**](VdiskDeviceInfos2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_devices_put**
> VdiskDeviceInfos rest_v10_dd_systems_systemid_protocols_vdisk_devices_put(system_id, vdisk_devices_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_devices_modify = dd_sdk_1_0.VdiskDevicesModify() # VdiskDevicesModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk device.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_devices_put(system_id, vdisk_devices_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v10_dd_systems_systemid_protocols_vdisk_devices_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devices_modify** | [**VdiskDevicesModify**](VdiskDevicesModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDeviceInfos**](VdiskDeviceInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_delete**
> ServiceStatus rest_v20_dd_systems_systemid_protocols_vdisk_devices_delete(system_id, vdisk_devices_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively, delete_device_group_on_empty=delete_device_group_on_empty)

Delete a list of VDisk devices.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_devices_delete = dd_sdk_1_0.VdiskDevicesDelete() # VdiskDevicesDelete | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
delete_recursively = true # bool | default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type=xs:boolean (optional)
delete_device_group_on_empty = true # bool | default value is false. When delete_device_group_on_empty flag is set, force delete the parent device group if empty on last device delete.  @#$type=xs:boolean (optional)

try:
    # Delete a list of VDisk devices.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_delete(system_id, vdisk_devices_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively, delete_device_group_on_empty=delete_device_group_on_empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devices_delete** | [**VdiskDevicesDelete**](VdiskDevicesDelete.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **delete_recursively** | **bool**| default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type&#x3D;xs:boolean | [optional] 
 **delete_device_group_on_empty** | **bool**| default value is false. When delete_device_group_on_empty flag is set, force delete the parent device group if empty on last device delete.  @#$type&#x3D;xs:boolean | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_get**
> VdiskDeviceInfos20 rest_v20_dd_systems_systemid_protocols_vdisk_devices_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk device information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskDeviceSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=vdiskDeviceFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk device information.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,user\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskDeviceSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and user&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskDeviceFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDeviceInfos20**](VdiskDeviceInfos20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_delete**
> ServiceStatus rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively, handle_is_set=handle_is_set, lock_handle=lock_handle)

Delete a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
delete_recursively = true # bool | default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type=xs:boolean (optional)
handle_is_set = true # bool | default value is false. handle_is_set indicates whether lock_handle parameter is provided or not.  @#$type=xs:boolean (optional)
lock_handle = 789 # int | default value is 0. Management lock handle for a locked device. Valid only if handle_is_set is set to true.  @#$type=xs:unsignedLong (optional)

try:
    # Delete a VDisk device.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, delete_recursively=delete_recursively, handle_is_set=handle_is_set, lock_handle=lock_handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **delete_recursively** | **bool**| default value is false. When delete_recursively flag is set, force delete subobjects recursively under the device and destroy the device.  @#$type&#x3D;xs:boolean | [optional] 
 **handle_is_set** | **bool**| default value is false. handle_is_set indicates whether lock_handle parameter is provided or not.  @#$type&#x3D;xs:boolean | [optional] 
 **lock_handle** | **int**| default value is 0. Management lock handle for a locked device. Valid only if handle_is_set is set to true.  @#$type&#x3D;xs:unsignedLong | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_get**
> VdiskDeviceInfoDetail20 rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk device.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDeviceInfoDetail20**](VdiskDeviceInfoDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_put**
> VdiskDeviceInfo20 rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_put(system_id, id, vdisk_device_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
vdisk_device_modify_2_0 = dd_sdk_1_0.VdiskDeviceModify20() # VdiskDeviceModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk device.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_put(system_id, id, vdisk_device_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **vdisk_device_modify_2_0** | [**VdiskDeviceModify20**](VdiskDeviceModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDeviceInfo20**](VdiskDeviceInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_post**
> VdiskDeviceInfos2 rest_v20_dd_systems_systemid_protocols_vdisk_devices_post(system_id, vdisk_device_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_device_create = dd_sdk_1_0.VdiskDeviceCreate() # VdiskDeviceCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a VDisk device.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_post(system_id, vdisk_device_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_device_create** | [**VdiskDeviceCreate**](VdiskDeviceCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDeviceInfos2**](VdiskDeviceInfos2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_devices_put**
> VdiskDeviceInfos rest_v20_dd_systems_systemid_protocols_vdisk_devices_put(system_id, vdisk_devices_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify one or more VDisk devices.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_devices_modify_2_0 = dd_sdk_1_0.VdiskDevicesModify20() # VdiskDevicesModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify one or more VDisk devices.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_devices_put(system_id, vdisk_devices_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v20_dd_systems_systemid_protocols_vdisk_devices_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_devices_modify_2_0** | [**VdiskDevicesModify20**](VdiskDevicesModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskDeviceInfos**](VdiskDeviceInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v30_dd_systems_systemid_protocols_vdisk_devices_id_get**
> VdiskDeviceInfoDetail30 rest_v30_dd_systems_systemid_protocols_vdisk_devices_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk device.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskDevicesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk device identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk device.
    api_response = api_instance.rest_v30_dd_systems_systemid_protocols_vdisk_devices_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskDevicesApi->rest_v30_dd_systems_systemid_protocols_vdisk_devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk device identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskDeviceInfoDetail30**](VdiskDeviceInfoDetail30.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

