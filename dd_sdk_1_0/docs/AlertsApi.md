# dd_sdk_1_0.AlertsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_alerts_delete**](AlertsApi.md#rest_v10_dd_systems_systemid_alerts_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts | Delete all alerts
[**rest_v10_dd_systems_systemid_alerts_get**](AlertsApi.md#rest_v10_dd_systems_systemid_alerts_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts | Show list of alerts
[**rest_v10_dd_systems_systemid_alerts_id_delete**](AlertsApi.md#rest_v10_dd_systems_systemid_alerts_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/{ID} | Delete an alert
[**rest_v10_dd_systems_systemid_alerts_id_get**](AlertsApi.md#rest_v10_dd_systems_systemid_alerts_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/alerts/{ID} | Show details of an alert


# **rest_v10_dd_systems_systemid_alerts_delete**
> ServiceStatus rest_v10_dd_systems_systemid_alerts_delete(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete all alerts

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete all alerts
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_delete(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->rest_v10_dd_systems_systemid_alerts_delete: %s\n" % e)
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

# **rest_v10_dd_systems_systemid_alerts_get**
> Alerts rest_v10_dd_systems_systemid_alerts_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, is_active=is_active, exclude_fields=exclude_fields, include_fields=include_fields)

Show list of alerts

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"severity,class,msg,object_id,status,alert_gen_epoch\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=alertsSortQuery (optional)
filter = 'filter_example' # str | filter=\"severity=value and class=value where value is one of Cifs, Storage, Cluster, Network, Security, Filesystem, Environment, Replication, HardwareFailure, SystemMaintenance, Syslog, Firmware, ha, Cloud, capacity, dataAvailability, infrastructure and msg=value and object_id=value and status=value and alert_gen_epoch=range and node_id=value\". value should be a valid regular expression.  @#$type=alertsFilterQuery (optional)
is_active = true # bool | By default, it will show all of the alerts. If type is set to \"true\", show active alerts; otherwise, show all alerts.  @#$type=xs:boolean (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Show list of alerts
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, is_active=is_active, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->rest_v10_dd_systems_systemid_alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;severity,class,msg,object_id,status,alert_gen_epoch\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;alertsSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;severity&#x3D;value and class&#x3D;value where value is one of Cifs, Storage, Cluster, Network, Security, Filesystem, Environment, Replication, HardwareFailure, SystemMaintenance, Syslog, Firmware, ha, Cloud, capacity, dataAvailability, infrastructure and msg&#x3D;value and object_id&#x3D;value and status&#x3D;value and alert_gen_epoch&#x3D;range and node_id&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;alertsFilterQuery | [optional] 
 **is_active** | **bool**| By default, it will show all of the alerts. If type is set to \&quot;true\&quot;, show active alerts; otherwise, show all alerts.  @#$type&#x3D;xs:boolean | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**Alerts**](Alerts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_alerts_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_alerts_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete an alert

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
id = 'id_example' # str | Alert identifier  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete an alert
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->rest_v10_dd_systems_systemid_alerts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **id** | **str**| Alert identifier  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_alerts_id_get**
> AlertDetail rest_v10_dd_systems_systemid_alerts_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Show details of an alert

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AlertsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type=xs:string
id = 'id_example' # str | Alert identifier  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Show details of an alert
    api_response = api_instance.rest_v10_dd_systems_systemid_alerts_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->rest_v10_dd_systems_systemid_alerts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR  @#$type&#x3D;xs:string | 
 **id** | **str**| Alert identifier  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**AlertDetail**](AlertDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

