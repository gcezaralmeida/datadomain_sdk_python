# dd_sdk_1_0.ServicesAsupApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_services_asups_delete**](ServicesAsupApi.md#rest_v10_dd_systems_systemid_services_asups_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/asups | asup reset and delete.
[**rest_v10_dd_systems_systemid_services_asups_get**](ServicesAsupApi.md#rest_v10_dd_systems_systemid_services_asups_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/asups | GET request REST asup.
[**rest_v10_dd_systems_systemid_services_asups_put**](ServicesAsupApi.md#rest_v10_dd_systems_systemid_services_asups_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/asups | asup settings.


# **rest_v10_dd_systems_systemid_services_asups_delete**
> ServiceStatus rest_v10_dd_systems_systemid_services_asups_delete(system_id, asup_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

asup reset and delete.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.ServicesAsupApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
asup_delete = dd_sdk_1_0.AsupDelete() # AsupDelete | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # asup reset and delete.
    api_response = api_instance.rest_v10_dd_systems_systemid_services_asups_delete(system_id, asup_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesAsupApi->rest_v10_dd_systems_systemid_services_asups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **asup_delete** | [**AsupDelete**](AsupDelete.md)|  | 
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

# **rest_v10_dd_systems_systemid_services_asups_get**
> AsupDetailsInfos rest_v10_dd_systems_systemid_services_asups_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

GET request REST asup.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.ServicesAsupApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # GET request REST asup.
    api_response = api_instance.rest_v10_dd_systems_systemid_services_asups_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesAsupApi->rest_v10_dd_systems_systemid_services_asups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**AsupDetailsInfos**](AsupDetailsInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_services_asups_put**
> ServiceStatus rest_v10_dd_systems_systemid_services_asups_put(system_id, asup_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

asup settings.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.ServicesAsupApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
asup_modify = dd_sdk_1_0.AsupModify() # AsupModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # asup settings.
    api_response = api_instance.rest_v10_dd_systems_systemid_services_asups_put(system_id, asup_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesAsupApi->rest_v10_dd_systems_systemid_services_asups_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **asup_modify** | [**AsupModify**](AsupModify.md)|  | 
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

