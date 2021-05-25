# dd_sdk_1_0.DdboostStorageUnitsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_get**](DdboostStorageUnitsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units | Get DDBoost storage unit information.
[**rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_delete**](DdboostStorageUnitsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units/{ID} | Delete a Storage Unit.
[**rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_get**](DdboostStorageUnitsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units/{ID} | Get a DDBoost storage unit.
[**rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_put**](DdboostStorageUnitsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units/{ID} | Modify a Storage Unit.
[**rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_post**](DdboostStorageUnitsApi.md#rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units | Create a Storage Unit.
[**rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_get**](DdboostStorageUnitsApi.md#rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units/{ID} | Get a DDBoost storage unit.
[**rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_put**](DdboostStorageUnitsApi.md#rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units/{ID} | Modify a Storage Unit.
[**rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_post**](DdboostStorageUnitsApi.md#rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/ddboost/storage-units | Create a Storage Unit.


# **rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_get**
> DdboostStorageUnitInfos rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get DDBoost storage unit information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,role\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=ddboostStorageUnitSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value\". value should be a valid regular expression.  @#$type=ddboostStorageUnitFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get DDBoost storage unit information.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,role\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;ddboostStorageUnitSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;ddboostStorageUnitFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**DdboostStorageUnitInfos**](DdboostStorageUnitInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a Storage Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost storage units identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a Storage Unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost storage units identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_get**
> DdboostStorageUnitInfoDetail rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a DDBoost storage unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost storage units identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a DDBoost storage unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost storage units identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**DdboostStorageUnitInfoDetail**](DdboostStorageUnitInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_put**
> DdboostStorageUnitInfo rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_put(system_id, id, ddboost_storage_unit_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a Storage Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost storage units identifier.  @#$type=xs:string
ddboost_storage_unit_modify = dd_sdk_1_0.DdboostStorageUnitModify() # DdboostStorageUnitModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a Storage Unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_put(system_id, id, ddboost_storage_unit_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost storage units identifier.  @#$type&#x3D;xs:string | 
 **ddboost_storage_unit_modify** | [**DdboostStorageUnitModify**](DdboostStorageUnitModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**DdboostStorageUnitInfo**](DdboostStorageUnitInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_post**
> DdboostStorageUnitInfo rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_post(system_id, ddboost_storage_unit_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a Storage Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
ddboost_storage_unit_create = dd_sdk_1_0.DdboostStorageUnitCreate() # DdboostStorageUnitCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a Storage Unit.
    api_response = api_instance.rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_post(system_id, ddboost_storage_unit_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v10_dd_systems_systemid_protocols_ddboost_storage_units_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **ddboost_storage_unit_create** | [**DdboostStorageUnitCreate**](DdboostStorageUnitCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**DdboostStorageUnitInfo**](DdboostStorageUnitInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_get**
> DdboostStorageUnitInfoDetail20 rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a DDBoost storage unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost storage units identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a DDBoost storage unit.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost storage units identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**DdboostStorageUnitInfoDetail20**](DdboostStorageUnitInfoDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_put**
> DdboostStorageUnitInfoDetail20 rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_put(system_id, id, ddboost_storage_unit_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a Storage Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | ddboost storage units identifier.  @#$type=xs:string
ddboost_storage_unit_modify = dd_sdk_1_0.DdboostStorageUnitModify() # DdboostStorageUnitModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a Storage Unit.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_put(system_id, id, ddboost_storage_unit_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| ddboost storage units identifier.  @#$type&#x3D;xs:string | 
 **ddboost_storage_unit_modify** | [**DdboostStorageUnitModify**](DdboostStorageUnitModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**DdboostStorageUnitInfoDetail20**](DdboostStorageUnitInfoDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_post**
> DdboostStorageUnitInfoDetail20 rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_post(system_id, ddboost_storage_unit_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a Storage Unit.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.DdboostStorageUnitsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
ddboost_storage_unit_create = dd_sdk_1_0.DdboostStorageUnitCreate() # DdboostStorageUnitCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a Storage Unit.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_post(system_id, ddboost_storage_unit_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DdboostStorageUnitsApi->rest_v20_dd_systems_systemid_protocols_ddboost_storage_units_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **ddboost_storage_unit_create** | [**DdboostStorageUnitCreate**](DdboostStorageUnitCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**DdboostStorageUnitInfoDetail20**](DdboostStorageUnitInfoDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

