# dd_sdk_1_0.CloudUnitApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_cloud_units_get**](CloudUnitApi.md#rest_v10_dd_systems_systemid_cloud_units_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-units | Get List of Cloud Units.
[**rest_v10_dd_systems_systemid_cloud_units_id_delete**](CloudUnitApi.md#rest_v10_dd_systems_systemid_cloud_units_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-units/{ID} | Delete a Cloud Unit.
[**rest_v10_dd_systems_systemid_cloud_units_id_get**](CloudUnitApi.md#rest_v10_dd_systems_systemid_cloud_units_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-units/{ID} | Get Cloud Unit Details.
[**rest_v10_dd_systems_systemid_cloud_units_post**](CloudUnitApi.md#rest_v10_dd_systems_systemid_cloud_units_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-units | Create a Cloud Unit.


# **rest_v10_dd_systems_systemid_cloud_units_get**
> CloudUnits rest_v10_dd_systems_systemid_cloud_units_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get List of Cloud Units.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudUnitApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"cloud_unit_name\". For descending order, prefix the key with a dash (-). Ex: -cloud_unit_name  @#$type=cloudUnitSortQuery (optional)
filter = 'filter_example' # str | filter=\"cloud_unit_name=value\". value should be a valid regular expression.  @#$type=cloudUnitFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get List of Cloud Units.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_units_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudUnitApi->rest_v10_dd_systems_systemid_cloud_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;cloud_unit_name\&quot;. For descending order, prefix the key with a dash (-). Ex: -cloud_unit_name  @#$type&#x3D;cloudUnitSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;cloud_unit_name&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;cloudUnitFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**CloudUnits**](CloudUnits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_cloud_units_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_cloud_units_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a Cloud Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudUnitApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Unit identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a Cloud Unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_units_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudUnitApi->rest_v10_dd_systems_systemid_cloud_units_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Unit identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_cloud_units_id_get**
> CloudUnitDetail rest_v10_dd_systems_systemid_cloud_units_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get Cloud Unit Details.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudUnitApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Unit identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get Cloud Unit Details.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_units_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudUnitApi->rest_v10_dd_systems_systemid_cloud_units_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Unit identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**CloudUnitDetail**](CloudUnitDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_cloud_units_post**
> CloudUnit rest_v10_dd_systems_systemid_cloud_units_post(system_id, cloud_unit_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a Cloud Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudUnitApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
cloud_unit_create = dd_sdk_1_0.CloudUnitCreate() # CloudUnitCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a Cloud Unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_units_post(system_id, cloud_unit_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudUnitApi->rest_v10_dd_systems_systemid_cloud_units_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **cloud_unit_create** | [**CloudUnitCreate**](CloudUnitCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**CloudUnit**](CloudUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

