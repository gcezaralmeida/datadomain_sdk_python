# dd_sdk_1_0.SnmpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_services_snmp_get**](SnmpApi.md#rest_v10_dd_systems_systemid_services_snmp_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/snmp | Show SNMP configuration
[**rest_v10_dd_systems_systemid_services_snmp_put**](SnmpApi.md#rest_v10_dd_systems_systemid_services_snmp_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/services/snmp | Modify SNMP configuration. Existing information will be replaced by new input
[**rest_v20_dd_systems_systemid_services_snmp_get**](SnmpApi.md#rest_v20_dd_systems_systemid_services_snmp_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/services/snmp | Show SNMP configuration


# **rest_v10_dd_systems_systemid_services_snmp_get**
> SnmpInfo rest_v10_dd_systems_systemid_services_snmp_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Show SNMP configuration

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SnmpApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Show SNMP configuration
    api_response = api_instance.rest_v10_dd_systems_systemid_services_snmp_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpApi->rest_v10_dd_systems_systemid_services_snmp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**SnmpInfo**](SnmpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_services_snmp_put**
> ServiceStatus rest_v10_dd_systems_systemid_services_snmp_put(system_id, snmp_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify SNMP configuration. Existing information will be replaced by new input

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SnmpApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
snmp_modify = dd_sdk_1_0.SnmpModify() # SnmpModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify SNMP configuration. Existing information will be replaced by new input
    api_response = api_instance.rest_v10_dd_systems_systemid_services_snmp_put(system_id, snmp_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpApi->rest_v10_dd_systems_systemid_services_snmp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **snmp_modify** | [**SnmpModify**](SnmpModify.md)|  | 
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

# **rest_v20_dd_systems_systemid_services_snmp_get**
> SnmpInfo20 rest_v20_dd_systems_systemid_services_snmp_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Show SNMP configuration

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SnmpApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Show SNMP configuration
    api_response = api_instance.rest_v20_dd_systems_systemid_services_snmp_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpApi->rest_v20_dd_systems_systemid_services_snmp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**SnmpInfo20**](SnmpInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

