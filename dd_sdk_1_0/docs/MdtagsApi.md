# dd_sdk_1_0.MdtagsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_mdtags_get**](MdtagsApi.md#rest_v10_dd_systems_systemid_mdtags_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags | Retrieve list of objects matching supplied tag name, value, or time criteria.
[**rest_v10_dd_systems_systemid_mdtags_id_delete**](MdtagsApi.md#rest_v10_dd_systems_systemid_mdtags_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags/{ID} | Remove object from metadata tag store
[**rest_v10_dd_systems_systemid_mdtags_id_get**](MdtagsApi.md#rest_v10_dd_systems_systemid_mdtags_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags/{ID} | Get the set of tags for an object.
[**rest_v10_dd_systems_systemid_mdtags_id_put**](MdtagsApi.md#rest_v10_dd_systems_systemid_mdtags_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/mdtags/{ID} | Set or clear a set of metadata tags for an object


# **rest_v10_dd_systems_systemid_mdtags_get**
> MdtagObjectDetailList rest_v10_dd_systems_systemid_mdtags_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, tag_scope=tag_scope, exclude_fields=exclude_fields, include_fields=include_fields)

Retrieve list of objects matching supplied tag name, value, or time criteria.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MdtagsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,user\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=mdtagSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and user=value\". value should be a valid regular expression.  @#$type=mdtagFilterQuery (optional)
tag_scope = 'tag_scope_example' # str | Scope of tagdata to retrieve.  @#$type=mdtagGetFlags (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Retrieve list of objects matching supplied tag name, value, or time criteria.
    api_response = api_instance.rest_v10_dd_systems_systemid_mdtags_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, tag_scope=tag_scope, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdtagsApi->rest_v10_dd_systems_systemid_mdtags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,user\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;mdtagSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and user&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;mdtagFilterQuery | [optional] 
 **tag_scope** | **str**| Scope of tagdata to retrieve.  @#$type&#x3D;mdtagGetFlags | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MdtagObjectDetailList**](MdtagObjectDetailList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_mdtags_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_mdtags_id_delete(system_id, id, filter, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Remove object from metadata tag store

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MdtagsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Object identifier.  @#$type=xs:string
filter = 'filter_example' # str | Namespace must be specified for the object target.  @#$type=mdtagIdFilterQuery
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Remove object from metadata tag store
    api_response = api_instance.rest_v10_dd_systems_systemid_mdtags_id_delete(system_id, id, filter, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdtagsApi->rest_v10_dd_systems_systemid_mdtags_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Object identifier.  @#$type&#x3D;xs:string | 
 **filter** | **str**| Namespace must be specified for the object target.  @#$type&#x3D;mdtagIdFilterQuery | 
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

# **rest_v10_dd_systems_systemid_mdtags_id_get**
> MdtagObjectDetail rest_v10_dd_systems_systemid_mdtags_id_get(system_id, id, filter, authorization=authorization, x_dd_auth_token=x_dd_auth_token, tag_scope=tag_scope, exclude_fields=exclude_fields, include_fields=include_fields)

Get the set of tags for an object.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MdtagsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Object identifier.  @#$type=xs:string
filter = 'filter_example' # str | filter=\"namespace=value\". value should be a valid namespace string.  @#$type=mdtagIdFilterQuery
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
tag_scope = 'tag_scope_example' # str | Scope of tagdata to retrieve.  @#$type=mdtagGetFlags (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get the set of tags for an object.
    api_response = api_instance.rest_v10_dd_systems_systemid_mdtags_id_get(system_id, id, filter, authorization=authorization, x_dd_auth_token=x_dd_auth_token, tag_scope=tag_scope, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdtagsApi->rest_v10_dd_systems_systemid_mdtags_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Object identifier.  @#$type&#x3D;xs:string | 
 **filter** | **str**| filter&#x3D;\&quot;namespace&#x3D;value\&quot;. value should be a valid namespace string.  @#$type&#x3D;mdtagIdFilterQuery | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **tag_scope** | **str**| Scope of tagdata to retrieve.  @#$type&#x3D;mdtagGetFlags | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MdtagObjectDetail**](MdtagObjectDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_mdtags_id_put**
> MdtagObjectIdentity rest_v10_dd_systems_systemid_mdtags_id_put(system_id, id, mdtag_object_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Set or clear a set of metadata tags for an object

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MdtagsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Object identifier.  @#$type=xs:string
mdtag_object_modify = dd_sdk_1_0.MdtagObjectModify() # MdtagObjectModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Set or clear a set of metadata tags for an object
    api_response = api_instance.rest_v10_dd_systems_systemid_mdtags_id_put(system_id, id, mdtag_object_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdtagsApi->rest_v10_dd_systems_systemid_mdtags_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Object identifier.  @#$type&#x3D;xs:string | 
 **mdtag_object_modify** | [**MdtagObjectModify**](MdtagObjectModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**MdtagObjectIdentity**](MdtagObjectIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

