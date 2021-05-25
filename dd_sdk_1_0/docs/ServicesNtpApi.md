# dd_sdk_1_0.ServicesNtpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_services_ntp_get**](ServicesNtpApi.md#rest_v10_dd_systems_systemid_services_ntp_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/ntp | Get NTP Settings information.
[**rest_v10_dd_systems_systemid_services_ntp_put**](ServicesNtpApi.md#rest_v10_dd_systems_systemid_services_ntp_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/ntp | Modify an NTP Settings.
[**rest_v20_dd_systems_systemid_services_ntp_put**](ServicesNtpApi.md#rest_v20_dd_systems_systemid_services_ntp_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/services/ntp | Modify an NTP Settings.


# **rest_v10_dd_systems_systemid_services_ntp_get**
> ServiceNtpInfo rest_v10_dd_systems_systemid_services_ntp_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, exclude_fields=exclude_fields, include_fields=include_fields)

Get NTP Settings information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.ServicesNtpApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get NTP Settings information.
    api_response = api_instance.rest_v10_dd_systems_systemid_services_ntp_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesNtpApi->rest_v10_dd_systems_systemid_services_ntp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ServiceNtpInfo**](ServiceNtpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_services_ntp_put**
> ServiceStatus rest_v10_dd_systems_systemid_services_ntp_put(system_id, services_ntp_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an NTP Settings.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.ServicesNtpApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
services_ntp_modify = dd_sdk_1_0.ServicesNtpModify() # ServicesNtpModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an NTP Settings.
    api_response = api_instance.rest_v10_dd_systems_systemid_services_ntp_put(system_id, services_ntp_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesNtpApi->rest_v10_dd_systems_systemid_services_ntp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **services_ntp_modify** | [**ServicesNtpModify**](ServicesNtpModify.md)|  | 
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

# **rest_v20_dd_systems_systemid_services_ntp_put**
> ServiceNtpInfo rest_v20_dd_systems_systemid_services_ntp_put(system_id, services_ntp_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an NTP Settings.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.ServicesNtpApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
services_ntp_modify_2_0 = dd_sdk_1_0.ServicesNtpModify20() # ServicesNtpModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an NTP Settings.
    api_response = api_instance.rest_v20_dd_systems_systemid_services_ntp_put(system_id, services_ntp_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesNtpApi->rest_v20_dd_systems_systemid_services_ntp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **services_ntp_modify_2_0** | [**ServicesNtpModify20**](ServicesNtpModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ServiceNtpInfo**](ServiceNtpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

