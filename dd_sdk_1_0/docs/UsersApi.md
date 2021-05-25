# dd_sdk_1_0.UsersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_users_get**](UsersApi.md#rest_v10_dd_systems_systemid_users_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/users | Get users information.
[**rest_v10_dd_systems_systemid_users_id_delete**](UsersApi.md#rest_v10_dd_systems_systemid_users_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/users/{ID} | Delete a User.
[**rest_v10_dd_systems_systemid_users_id_get**](UsersApi.md#rest_v10_dd_systems_systemid_users_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/users/{ID} | Get a User.
[**rest_v10_dd_systems_systemid_users_id_put**](UsersApi.md#rest_v10_dd_systems_systemid_users_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/users/{ID} | Modify a User.
[**rest_v10_dd_systems_systemid_users_post**](UsersApi.md#rest_v10_dd_systems_systemid_users_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/users | Create a User.


# **rest_v10_dd_systems_systemid_users_get**
> UserInfos rest_v10_dd_systems_systemid_users_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get users information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.UsersApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,role\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=userSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and role=value\". value should be a valid regular expression.  @#$type=userFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get users information.
    api_response = api_instance.rest_v10_dd_systems_systemid_users_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->rest_v10_dd_systems_systemid_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,role\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;userSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and role&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;userFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**UserInfos**](UserInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_users_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_users_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, x_dd_sec_officer=x_dd_sec_officer)

Delete a User.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.UsersApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | user identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_sec_officer = 'x_dd_sec_officer_example' # str | Security Officer Information  @#$type=xs:string (optional)

try:
    # Delete a User.
    api_response = api_instance.rest_v10_dd_systems_systemid_users_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, x_dd_sec_officer=x_dd_sec_officer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->rest_v10_dd_systems_systemid_users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| user identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_sec_officer** | **str**| Security Officer Information  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_users_id_get**
> UserInfoDetail rest_v10_dd_systems_systemid_users_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a User.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.UsersApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | user identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a User.
    api_response = api_instance.rest_v10_dd_systems_systemid_users_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->rest_v10_dd_systems_systemid_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| user identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**UserInfoDetail**](UserInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_users_id_put**
> UserInfo rest_v10_dd_systems_systemid_users_id_put(system_id, id, user_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a User.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.UsersApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | user identifier.  @#$type=xs:string
user_modify = dd_sdk_1_0.UserModify() # UserModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a User.
    api_response = api_instance.rest_v10_dd_systems_systemid_users_id_put(system_id, id, user_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->rest_v10_dd_systems_systemid_users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| user identifier.  @#$type&#x3D;xs:string | 
 **user_modify** | [**UserModify**](UserModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_users_post**
> UserInfo rest_v10_dd_systems_systemid_users_post(system_id, user_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token, x_dd_sec_officer=x_dd_sec_officer)

Create a User.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.UsersApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
user_create = dd_sdk_1_0.UserCreate() # UserCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_sec_officer = 'x_dd_sec_officer_example' # str | Security Officer Information  @#$type=xs:string (optional)

try:
    # Create a User.
    api_response = api_instance.rest_v10_dd_systems_systemid_users_post(system_id, user_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token, x_dd_sec_officer=x_dd_sec_officer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->rest_v10_dd_systems_systemid_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **user_create** | [**UserCreate**](UserCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_sec_officer** | **str**| Security Officer Information  @#$type&#x3D;xs:string | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

