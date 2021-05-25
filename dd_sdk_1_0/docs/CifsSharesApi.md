# dd_sdk_1_0.CifsSharesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_cifs_shares_get**](CifsSharesApi.md#rest_v10_dd_systems_systemid_protocols_cifs_shares_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/cifs/shares | Get CIFS share information.
[**rest_v10_dd_systems_systemid_protocols_cifs_shares_id_delete**](CifsSharesApi.md#rest_v10_dd_systems_systemid_protocols_cifs_shares_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/cifs/shares/{ID} | Delete a CIFS share.
[**rest_v10_dd_systems_systemid_protocols_cifs_shares_id_get**](CifsSharesApi.md#rest_v10_dd_systems_systemid_protocols_cifs_shares_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/cifs/shares/{ID} | Get a CIFS share.
[**rest_v10_dd_systems_systemid_protocols_cifs_shares_id_put**](CifsSharesApi.md#rest_v10_dd_systems_systemid_protocols_cifs_shares_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/cifs/shares/{ID} | Modify a CIFS share.
[**rest_v10_dd_systems_systemid_protocols_cifs_shares_post**](CifsSharesApi.md#rest_v10_dd_systems_systemid_protocols_cifs_shares_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/cifs/shares | Create a CIFS share.


# **rest_v10_dd_systems_systemid_protocols_cifs_shares_get**
> ShareInfos rest_v10_dd_systems_systemid_protocols_cifs_shares_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get CIFS share information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CifsSharesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,path,mtree\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=shareSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and path=value and mtree=value\". value should be a valid regular expression.  @#$type=shareFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get CIFS share information.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_cifs_shares_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CifsSharesApi->rest_v10_dd_systems_systemid_protocols_cifs_shares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,path,mtree\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;shareSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and path&#x3D;value and mtree&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;shareFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ShareInfos**](ShareInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_cifs_shares_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_cifs_shares_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a CIFS share.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CifsSharesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | CIFS identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a CIFS share.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_cifs_shares_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CifsSharesApi->rest_v10_dd_systems_systemid_protocols_cifs_shares_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| CIFS identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_protocols_cifs_shares_id_get**
> ShareInfoDetail rest_v10_dd_systems_systemid_protocols_cifs_shares_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a CIFS share.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CifsSharesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | CIFS identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a CIFS share.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_cifs_shares_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CifsSharesApi->rest_v10_dd_systems_systemid_protocols_cifs_shares_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| CIFS identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ShareInfoDetail**](ShareInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_cifs_shares_id_put**
> ShareInfo rest_v10_dd_systems_systemid_protocols_cifs_shares_id_put(system_id, id, share_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a CIFS share.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CifsSharesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | CIFS identifier.  @#$type=xs:string
share_modify = dd_sdk_1_0.ShareModify() # ShareModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a CIFS share.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_cifs_shares_id_put(system_id, id, share_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CifsSharesApi->rest_v10_dd_systems_systemid_protocols_cifs_shares_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| CIFS identifier.  @#$type&#x3D;xs:string | 
 **share_modify** | [**ShareModify**](ShareModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ShareInfo**](ShareInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_cifs_shares_post**
> ShareInfo rest_v10_dd_systems_systemid_protocols_cifs_shares_post(system_id, share_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a CIFS share.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CifsSharesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
share_create = dd_sdk_1_0.ShareCreate() # ShareCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a CIFS share.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_cifs_shares_post(system_id, share_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CifsSharesApi->rest_v10_dd_systems_systemid_protocols_cifs_shares_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **share_create** | [**ShareCreate**](ShareCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ShareInfo**](ShareInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

