# dd_sdk_1_0.SupportBundlesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_supports_support_bundles_delete**](SupportBundlesApi.md#rest_v10_dd_systems_systemid_supports_support_bundles_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/supports/support-bundles | Delete all support bundles
[**rest_v10_dd_systems_systemid_supports_support_bundles_get**](SupportBundlesApi.md#rest_v10_dd_systems_systemid_supports_support_bundles_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/supports/support-bundles | List support bundles
[**rest_v10_dd_systems_systemid_supports_support_bundles_id_delete**](SupportBundlesApi.md#rest_v10_dd_systems_systemid_supports_support_bundles_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/supports/support-bundles/{ID} | Delete a support bundle
[**rest_v10_dd_systems_systemid_supports_support_bundles_post**](SupportBundlesApi.md#rest_v10_dd_systems_systemid_supports_support_bundles_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/supports/support-bundles | Create support bundle
[**rest_v20_dd_systems_systemid_supports_support_bundles_post**](SupportBundlesApi.md#rest_v20_dd_systems_systemid_supports_support_bundles_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/supports/support-bundles | Create support bundle asynchronously


# **rest_v10_dd_systems_systemid_supports_support_bundles_delete**
> ServiceStatus rest_v10_dd_systems_systemid_supports_support_bundles_delete(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete all support bundles

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SupportBundlesApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete all support bundles
    api_response = api_instance.rest_v10_dd_systems_systemid_supports_support_bundles_delete(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportBundlesApi->rest_v10_dd_systems_systemid_supports_support_bundles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_supports_support_bundles_get**
> SupportBundleInfos rest_v10_dd_systems_systemid_supports_support_bundles_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

List support bundles

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SupportBundlesApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,hostname,size_in_bytes,time_created_epoch\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=supportBundleSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=regex and hostname=regex and size_in_bytes=range and time_created_epoch=range\". The range should be (min, max) or (,max) or (min,). regex means regular expression.  @#$type=supportBundleFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # List support bundles
    api_response = api_instance.rest_v10_dd_systems_systemid_supports_support_bundles_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportBundlesApi->rest_v10_dd_systems_systemid_supports_support_bundles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,hostname,size_in_bytes,time_created_epoch\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;supportBundleSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;regex and hostname&#x3D;regex and size_in_bytes&#x3D;range and time_created_epoch&#x3D;range\&quot;. The range should be (min, max) or (,max) or (min,). regex means regular expression.  @#$type&#x3D;supportBundleFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**SupportBundleInfos**](SupportBundleInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_supports_support_bundles_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_supports_support_bundles_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a support bundle

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SupportBundlesApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
id = 'id_example' # str | Urlencoded support bundle name.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a support bundle
    api_response = api_instance.rest_v10_dd_systems_systemid_supports_support_bundles_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportBundlesApi->rest_v10_dd_systems_systemid_supports_support_bundles_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **id** | **str**| Urlencoded support bundle name.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_supports_support_bundles_post**
> SupportBundleInfos rest_v10_dd_systems_systemid_supports_support_bundles_post(system_id, support_bundle_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create support bundle

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SupportBundlesApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
support_bundle_create = dd_sdk_1_0.SupportBundleCreate() # SupportBundleCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create support bundle
    api_response = api_instance.rest_v10_dd_systems_systemid_supports_support_bundles_post(system_id, support_bundle_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportBundlesApi->rest_v10_dd_systems_systemid_supports_support_bundles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **support_bundle_create** | [**SupportBundleCreate**](SupportBundleCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**SupportBundleInfos**](SupportBundleInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_supports_support_bundles_post**
> ServiceStatus rest_v20_dd_systems_systemid_supports_support_bundles_post(system_id, support_bundle_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create support bundle asynchronously

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SupportBundlesApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
support_bundle_create = dd_sdk_1_0.SupportBundleCreate() # SupportBundleCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create support bundle asynchronously
    api_response = api_instance.rest_v20_dd_systems_systemid_supports_support_bundles_post(system_id, support_bundle_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportBundlesApi->rest_v20_dd_systems_systemid_supports_support_bundles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **support_bundle_create** | [**SupportBundleCreate**](SupportBundleCreate.md)|  | 
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

