# dd_sdk_1_0.DdboostClientsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_ddboost_clients_get**](DdboostClientsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_clients_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/clients | Get the list of DDBoost clients.
[**rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_delete**](DdboostClientsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/clients/{ID} | Remove a DDBoost client.
[**rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_put**](DdboostClientsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/clients/{ID} | Modify a DDBoost client.
[**rest_v10_dd_systems_systemid_protocols_ddboost_clients_post**](DdboostClientsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_clients_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/clients | Add a DDBoost client.


# **rest_v10_dd_systems_systemid_protocols_ddboost_clients_get**
> DdboostClientList rest_v10_dd_systems_systemid_protocols_ddboost_clients_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get the list of DDBoost clients.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=ddboostClientSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value\". value should be a valid regular expression.  @#$type=ddboostClientFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get the list of DDBoost clients.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_clients_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostClientsApi->rest_v10_dd_systems_systemid_protocols_ddboost_clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;ddboostClientSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;ddboostClientFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**DdboostClientList**](DdboostClientList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Remove a DDBoost client.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost user identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Remove a DDBoost client.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostClientsApi->rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost user identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_put**
> DdboostClientInfo rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_put(system_id, id, ddboost_client_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a DDBoost client.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost user identifier.  @#$type=xs:string
ddboost_client_modify = dd_sdk_1_0.DdboostClientModify() # DdboostClientModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a DDBoost client.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_put(system_id, id, ddboost_client_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostClientsApi->rest_v10_dd_systems_systemid_protocols_ddboost_clients_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost user identifier.  @#$type&#x3D;xs:string | 
 **ddboost_client_modify** | [**DdboostClientModify**](DdboostClientModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**DdboostClientInfo**](DdboostClientInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_ddboost_clients_post**
> DdboostClientInfo rest_v10_dd_systems_systemid_protocols_ddboost_clients_post(system_id, ddboost_client_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Add a DDBoost client.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostClientsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
ddboost_client_create = dd_sdk_1_0.DdboostClientCreate() # DdboostClientCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Add a DDBoost client.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_clients_post(system_id, ddboost_client_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostClientsApi->rest_v10_dd_systems_systemid_protocols_ddboost_clients_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **ddboost_client_create** | [**DdboostClientCreate**](DdboostClientCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**DdboostClientInfo**](DdboostClientInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

