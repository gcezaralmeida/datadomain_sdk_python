# dd_sdk_1_0.NfsExportsIdClientsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_delete**](NfsExportsIdClientsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_delete) | **DELETE** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/clients | Delete clients of an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_get**](NfsExportsIdClientsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/clients | List all clients of an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_post**](NfsExportsIdClientsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/clients | Create clients on an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_put**](NfsExportsIdClientsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/clients | Modify clients of an NFS export.


# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_delete**
> ServiceStatus rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_delete(system_id, id, nfs_export_client_delete_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete clients of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
nfs_export_client_delete_2_0 = dd_sdk_1_0.ExportClientDelete20() # ExportClientDelete20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete clients of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_delete(system_id, id, nfs_export_client_delete_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdClientsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_client_delete_2_0** | [**ExportClientDelete20**](ExportClientDelete20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_get**
> ExportClientsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, sort=sort, exclude_fields=exclude_fields, include_fields=include_fields)

List all clients of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
sort = 'sort_example' # str | sort=\"hostname or ip-address. For descending order, prefix the key with a dash (-). key=\"hostname/ip-address\"  @#$type=clientsSortQuery_2_0 (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # List all clients of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, sort=sort, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdClientsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;hostname or ip-address. For descending order, prefix the key with a dash (-). key&#x3D;\&quot;hostname/ip-address\&quot;  @#$type&#x3D;clientsSortQuery_2_0 | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ExportClientsInfo20**](ExportClientsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_post**
> ExportClientsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_post(system_id, id, nfs_export_client_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create clients on an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
nfs_export_client_create_2_0 = dd_sdk_1_0.ExportClientCreate20() # ExportClientCreate20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create clients on an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_post(system_id, id, nfs_export_client_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdClientsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_client_create_2_0** | [**ExportClientCreate20**](ExportClientCreate20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportClientsInfo20**](ExportClientsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_put**
> ExportClientsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_put(system_id, id, nfs_export_client_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify clients of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
nfs_export_client_modify_2_0 = dd_sdk_1_0.ExportClientModify20() # ExportClientModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify clients of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_put(system_id, id, nfs_export_client_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdClientsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_clients_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_client_modify_2_0** | [**ExportClientModify20**](ExportClientModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportClientsInfo20**](ExportClientsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

