# dd_sdk_1_0.AlertsNotifylistsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_alerts_notify_lists_delete**](AlertsNotifylistsApi.md#rest_v10_dd_systems_systemid_alerts_notify_lists_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/notify-lists | Delete all user-configured alert notification lists
[**rest_v10_dd_systems_systemid_alerts_notify_lists_get**](AlertsNotifylistsApi.md#rest_v10_dd_systems_systemid_alerts_notify_lists_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/notify-lists | Show list of alerts notification lists
[**rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete**](AlertsNotifylistsApi.md#rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/notify-lists/{ID} | Delete an alert notification list
[**rest_v10_dd_systems_systemid_alerts_notify_lists_id_get**](AlertsNotifylistsApi.md#rest_v10_dd_systems_systemid_alerts_notify_lists_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/notify-lists/{ID} | Show details of an alert notification list
[**rest_v10_dd_systems_systemid_alerts_notify_lists_id_put**](AlertsNotifylistsApi.md#rest_v10_dd_systems_systemid_alerts_notify_lists_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/notify-lists/{ID} | Modify an alert notification list. Existing information will be replaced by new input
[**rest_v10_dd_systems_systemid_alerts_notify_lists_post**](AlertsNotifylistsApi.md#rest_v10_dd_systems_systemid_alerts_notify_lists_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/notify-lists | Create an alert notification list


# **rest_v10_dd_systems_systemid_alerts_notify_lists_delete**
> ServiceStatus rest_v10_dd_systems_systemid_alerts_notify_lists_delete(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete all user-configured alert notification lists

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsNotifylistsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete all user-configured alert notification lists
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_notify_lists_delete(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsNotifylistsApi->rest_v10_dd_systems_systemid_alerts_notify_lists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_alerts_notify_lists_get**
> NotifyLists rest_v10_dd_systems_systemid_alerts_notify_lists_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Show list of alerts notification lists

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsNotifylistsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=notifyListsSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value\". value should be a valid regular expression.  @#$type=notifyListsFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Show list of alerts notification lists
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_notify_lists_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsNotifylistsApi->rest_v10_dd_systems_systemid_alerts_notify_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;notifyListsSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;notifyListsFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**NotifyLists**](NotifyLists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete an alert notification list

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsNotifylistsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
id = 'id_example' # str | Alert notification list identifier  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete an alert notification list
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsNotifylistsApi->rest_v10_dd_systems_systemid_alerts_notify_lists_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **id** | **str**| Alert notification list identifier  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_alerts_notify_lists_id_get**
> NotifyListDetail rest_v10_dd_systems_systemid_alerts_notify_lists_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Show details of an alert notification list

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsNotifylistsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
id = 'id_example' # str | Alert notification list identifier  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Show details of an alert notification list
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_notify_lists_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsNotifylistsApi->rest_v10_dd_systems_systemid_alerts_notify_lists_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **id** | **str**| Alert notification list identifier  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**NotifyListDetail**](NotifyListDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_alerts_notify_lists_id_put**
> NotifyList rest_v10_dd_systems_systemid_alerts_notify_lists_id_put(system_id, id, notify_list_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an alert notification list. Existing information will be replaced by new input

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsNotifylistsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
id = 'id_example' # str | Alert notification list identifier  @#$type=xs:string
notify_list_modify = dd_sdk_1_0.NotifyListProperty() # NotifyListProperty | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an alert notification list. Existing information will be replaced by new input
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_notify_lists_id_put(system_id, id, notify_list_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsNotifylistsApi->rest_v10_dd_systems_systemid_alerts_notify_lists_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **id** | **str**| Alert notification list identifier  @#$type&#x3D;xs:string | 
 **notify_list_modify** | [**NotifyListProperty**](NotifyListProperty.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**NotifyList**](NotifyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_alerts_notify_lists_post**
> NotifyList rest_v10_dd_systems_systemid_alerts_notify_lists_post(system_id, notify_list_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create an alert notification list

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsNotifylistsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
notify_list_create = dd_sdk_1_0.NotifyListCreate() # NotifyListCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create an alert notification list
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_notify_lists_post(system_id, notify_list_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsNotifylistsApi->rest_v10_dd_systems_systemid_alerts_notify_lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **notify_list_create** | [**NotifyListCreate**](NotifyListCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**NotifyList**](NotifyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

