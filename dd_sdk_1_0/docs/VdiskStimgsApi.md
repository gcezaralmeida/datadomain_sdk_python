# dd_sdk_1_0.VdiskStimgsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_vdisk_static_images_get**](VdiskStimgsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_static_images_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images | Get VDisk static images information.
[**rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_delete**](VdiskStimgsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images/{ID} | Delete a VDisk static image.
[**rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_get**](VdiskStimgsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images/{ID} | Get a VDisk static image.
[**rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_put**](VdiskStimgsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images/{ID} | Modify a VDisk static image.
[**rest_v10_dd_systems_systemid_protocols_vdisk_static_images_post**](VdiskStimgsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_static_images_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images | Create a VDisk static image.
[**rest_v10_dd_systems_systemid_protocols_vdisk_static_images_put**](VdiskStimgsApi.md#rest_v10_dd_systems_systemid_protocols_vdisk_static_images_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images | Modify multiple VDisk static images.
[**rest_v20_dd_systems_systemid_protocols_vdisk_static_images_get**](VdiskStimgsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_static_images_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images | Get VDisk static images information.
[**rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_get**](VdiskStimgsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images/{ID} | Get a VDisk static image.
[**rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_put**](VdiskStimgsApi.md#rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images/{ID} | Modify a VDisk static image.
[**rest_v30_dd_systems_systemid_protocols_vdisk_static_images_id_get**](VdiskStimgsApi.md#rest_v30_dd_systems_systemid_protocols_vdisk_static_images_id_get) | **GET** /rest/v3.0/dd-systems/{SYSTEM-ID}/protocols/vdisk/static-images/{ID} | Get a VDisk static image.


# **rest_v10_dd_systems_systemid_protocols_vdisk_static_images_get**
> VdiskStimgInfos rest_v10_dd_systems_systemid_protocols_vdisk_static_images_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk static images information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskStimgSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=vdiskStimgFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk static images information.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_static_images_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v10_dd_systems_systemid_protocols_vdisk_static_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,user\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskStimgSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and user&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskStimgFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskStimgInfos**](VdiskStimgInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk static image identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a VDisk static image.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk static image identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_get**
> VdiskStimgInfoDetail rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk static image identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk static image.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk static image identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskStimgInfoDetail**](VdiskStimgInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_put**
> VdiskStimgInfo rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_put(system_id, id, vdisk_stimg_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk static image identifier.  @#$type=xs:string
vdisk_stimg_modify = dd_sdk_1_0.VdiskStimgModify() # VdiskStimgModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk static image.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_put(system_id, id, vdisk_stimg_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v10_dd_systems_systemid_protocols_vdisk_static_images_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk static image identifier.  @#$type&#x3D;xs:string | 
 **vdisk_stimg_modify** | [**VdiskStimgModify**](VdiskStimgModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskStimgInfo**](VdiskStimgInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_static_images_post**
> VdiskStimgInfos rest_v10_dd_systems_systemid_protocols_vdisk_static_images_post(system_id, vdisk_stimgs_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_stimgs_create = dd_sdk_1_0.VdiskStimgsCreate() # VdiskStimgsCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a VDisk static image.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_static_images_post(system_id, vdisk_stimgs_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v10_dd_systems_systemid_protocols_vdisk_static_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_stimgs_create** | [**VdiskStimgsCreate**](VdiskStimgsCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskStimgInfos**](VdiskStimgInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_vdisk_static_images_put**
> VdiskStimgInfos rest_v10_dd_systems_systemid_protocols_vdisk_static_images_put(system_id, vdisk_stimgs_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify multiple VDisk static images.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
vdisk_stimgs_modify = dd_sdk_1_0.VdiskStimgsModify() # VdiskStimgsModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify multiple VDisk static images.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_vdisk_static_images_put(system_id, vdisk_stimgs_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v10_dd_systems_systemid_protocols_vdisk_static_images_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **vdisk_stimgs_modify** | [**VdiskStimgsModify**](VdiskStimgsModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskStimgInfos**](VdiskStimgInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_static_images_get**
> VdiskStimgInfos20 rest_v20_dd_systems_systemid_protocols_vdisk_static_images_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get VDisk static images information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=vdiskStimgSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=vdiskStimgFilterQuery_2_0 (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get VDisk static images information.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_static_images_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v20_dd_systems_systemid_protocols_vdisk_static_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,user\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;vdiskStimgSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and user&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;vdiskStimgFilterQuery_2_0 | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskStimgInfos20**](VdiskStimgInfos20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_get**
> VdiskStimgInfoDetail20 rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk static image guid identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
filter = 'filter_example' # str | filter=\"fields=recall_status\".  @#$type=vdiskStimgFilterRecallStatusQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk static image.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk static image guid identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;fields&#x3D;recall_status\&quot;.  @#$type&#x3D;vdiskStimgFilterRecallStatusQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskStimgInfoDetail20**](VdiskStimgInfoDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_put**
> VdiskStimgInfo rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_put(system_id, id, vdisk_stimg_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk static image guid identifier.  @#$type=xs:string
vdisk_stimg_modify_2_0 = dd_sdk_1_0.VdiskStimgModify20() # VdiskStimgModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a VDisk static image.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_put(system_id, id, vdisk_stimg_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v20_dd_systems_systemid_protocols_vdisk_static_images_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk static image guid identifier.  @#$type&#x3D;xs:string | 
 **vdisk_stimg_modify_2_0** | [**VdiskStimgModify20**](VdiskStimgModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**VdiskStimgInfo**](VdiskStimgInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v30_dd_systems_systemid_protocols_vdisk_static_images_id_get**
> VdiskStimgInfoDetail30 rest_v30_dd_systems_systemid_protocols_vdisk_static_images_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get a VDisk static image.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.VdiskStimgsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | VDisk static image guid identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
filter = 'filter_example' # str | filter=\"fields=recall_status\".  @#$type=vdiskStimgFilterRecallStatusQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a VDisk static image.
    api_response = api_instance.rest_v30_dd_systems_systemid_protocols_vdisk_static_images_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdiskStimgsApi->rest_v30_dd_systems_systemid_protocols_vdisk_static_images_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| VDisk static image guid identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;fields&#x3D;recall_status\&quot;.  @#$type&#x3D;vdiskStimgFilterRecallStatusQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**VdiskStimgInfoDetail30**](VdiskStimgInfoDetail30.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

