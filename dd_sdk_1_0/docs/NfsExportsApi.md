# dd_sdk_1_0.NfsExportsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_nfs_exports_get**](NfsExportsApi.md#rest_v10_dd_systems_systemid_protocols_nfs_exports_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports | Get NFS export list.
[**rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete**](NfsExportsApi.md#rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID} | Delete an NFS export.
[**rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get**](NfsExportsApi.md#rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID} | Get an NFS export.
[**rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put**](NfsExportsApi.md#rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID} | Modify an NFS export.
[**rest_v10_dd_systems_systemid_protocols_nfs_exports_post**](NfsExportsApi.md#rest_v10_dd_systems_systemid_protocols_nfs_exports_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports | Create NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_delete**](NfsExportsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_delete) | **DELETE** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports | Destroy NFS export[s].
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_get**](NfsExportsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports | Get NFS export list.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete**](NfsExportsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete) | **DELETE** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID} | Destroy an NFS export
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get**](NfsExportsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID} | Get details of an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put**](NfsExportsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID} | Modify an NFS export
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_post**](NfsExportsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports | Create an NFS export.


# **rest_v10_dd_systems_systemid_protocols_nfs_exports_get**
> ExportInfos rest_v10_dd_systems_systemid_protocols_nfs_exports_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get NFS export list.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"path,mtree\". For descending order, prefix the key with a dash (-). Ex: -path  @#$type=exportSortQuery (optional)
filter = 'filter_example' # str | filter=\"path=value and mtree=value\". Value should be a valid regular expression.  @#$type=exportFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get NFS export list.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_nfs_exports_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v10_dd_systems_systemid_protocols_nfs_exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;path,mtree\&quot;. For descending order, prefix the key with a dash (-). Ex: -path  @#$type&#x3D;exportSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;path&#x3D;value and mtree&#x3D;value\&quot;. Value should be a valid regular expression.  @#$type&#x3D;exportFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ExportInfos**](ExportInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete an NFS export.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v10_dd_systems_systemid_protocols_nfs_exports_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get**
> ExportInfoDetail rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get an NFS export.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v10_dd_systems_systemid_protocols_nfs_exports_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ExportInfoDetail**](ExportInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put**
> ExportInfo rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put(system_id, id, export_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
export_modify = dd_sdk_1_0.ExportModify() # ExportModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an NFS export.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put(system_id, id, export_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v10_dd_systems_systemid_protocols_nfs_exports_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **export_modify** | [**ExportModify**](ExportModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportInfo**](ExportInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_nfs_exports_post**
> ExportInfo rest_v10_dd_systems_systemid_protocols_nfs_exports_post(system_id, export_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
export_create = dd_sdk_1_0.ExportCreate() # ExportCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create NFS export.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_nfs_exports_post(system_id, export_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v10_dd_systems_systemid_protocols_nfs_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **export_create** | [**ExportCreate**](ExportCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportInfo**](ExportInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_delete**
> ServiceStatus rest_v20_dd_systems_systemid_protocols_nfs_exports_delete(system_id, export_spec, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Destroy NFS export[s].

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
export_spec = 'export_spec_example' # str | export spec or all  @#$type=exportFilterQuery_2_0
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Destroy NFS export[s].
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_delete(system_id, export_spec, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **export_spec** | **str**| export spec or all  @#$type&#x3D;exportFilterQuery_2_0 | 
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

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_get**
> ExportsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get NFS export list.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"path,mtree\". For descending order, prefix the key with a dash (-). Ex: -path  @#$type=exportSortQuery_2_0 (optional)
filter = 'filter_example' # str | filter=\"path=value and mtree=value\". Value should be a valid regular expression.  @#$type=exportFilterQuery_2_0 (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get NFS export list.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;path,mtree\&quot;. For descending order, prefix the key with a dash (-). Ex: -path  @#$type&#x3D;exportSortQuery_2_0 | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;path&#x3D;value and mtree&#x3D;value\&quot;. Value should be a valid regular expression.  @#$type&#x3D;exportFilterQuery_2_0 | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ExportsInfo20**](ExportsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete**
> ServiceStatus rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Destroy an NFS export

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Destroy an NFS export
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get**
> ExportInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get details of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get details of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ExportInfo20**](ExportInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put**
> ExportInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put(system_id, id, nfs_export_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an NFS export

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
nfs_export_modify_2_0 = dd_sdk_1_0.ExportModify20() # ExportModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an NFS export
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put(system_id, id, nfs_export_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_modify_2_0** | [**ExportModify20**](ExportModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportInfo20**](ExportInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_post**
> ExportInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_post(system_id, nfs_export_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
nfs_export_create_2_0 = dd_sdk_1_0.ExportCreate20() # ExportCreate20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_post(system_id, nfs_export_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_create_2_0** | [**ExportCreate20**](ExportCreate20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportInfo20**](ExportInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

