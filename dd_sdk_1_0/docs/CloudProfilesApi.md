# dd_sdk_1_0.CloudProfilesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_cloud_profiles_get**](CloudProfilesApi.md#rest_v10_dd_systems_systemid_cloud_profiles_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-profiles | Get List of cloud profiles.
[**rest_v10_dd_systems_systemid_cloud_profiles_id_delete**](CloudProfilesApi.md#rest_v10_dd_systems_systemid_cloud_profiles_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-profiles/{ID} | Delete a cloud profile.
[**rest_v10_dd_systems_systemid_cloud_profiles_id_get**](CloudProfilesApi.md#rest_v10_dd_systems_systemid_cloud_profiles_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-profiles/{ID} | Get a cloud profile.
[**rest_v10_dd_systems_systemid_cloud_profiles_id_put**](CloudProfilesApi.md#rest_v10_dd_systems_systemid_cloud_profiles_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-profiles/{ID} | Modify a cloud profile.
[**rest_v10_dd_systems_systemid_cloud_profiles_post**](CloudProfilesApi.md#rest_v10_dd_systems_systemid_cloud_profiles_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/cloud-profiles | Create cloud profile.
[**rest_v20_dd_systems_systemid_cloud_profiles_id_get**](CloudProfilesApi.md#rest_v20_dd_systems_systemid_cloud_profiles_id_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/cloud-profiles/{ID} | Get a cloud profile.
[**rest_v20_dd_systems_systemid_cloud_profiles_id_put**](CloudProfilesApi.md#rest_v20_dd_systems_systemid_cloud_profiles_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/cloud-profiles/{ID} | Modify a cloud profile.
[**rest_v20_dd_systems_systemid_cloud_profiles_post**](CloudProfilesApi.md#rest_v20_dd_systems_systemid_cloud_profiles_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/cloud-profiles | Create cloud profile.


# **rest_v10_dd_systems_systemid_cloud_profiles_get**
> CloudProfiles rest_v10_dd_systems_systemid_cloud_profiles_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get List of cloud profiles.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,provider_name\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=cloudProfileSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=value and cloud_provider=value\". value should be a valid regular expression.  @#$type=cloudProfileFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get List of cloud profiles.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_profiles_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v10_dd_systems_systemid_cloud_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,provider_name\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;cloudProfileSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;value and cloud_provider&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;cloudProfileFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**CloudProfiles**](CloudProfiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_cloud_profiles_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_cloud_profiles_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Profile identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a cloud profile.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_profiles_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v10_dd_systems_systemid_cloud_profiles_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Profile identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_cloud_profiles_id_get**
> CloudProfileDetail rest_v10_dd_systems_systemid_cloud_profiles_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Profile identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a cloud profile.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_profiles_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v10_dd_systems_systemid_cloud_profiles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Profile identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**CloudProfileDetail**](CloudProfileDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_cloud_profiles_id_put**
> CloudProfile rest_v10_dd_systems_systemid_cloud_profiles_id_put(system_id, id, cloud_profile_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Profile identifier.  @#$type=xs:string
cloud_profile_modify = dd_sdk_1_0.CloudProfileConfig() # CloudProfileConfig | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a cloud profile.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_profiles_id_put(system_id, id, cloud_profile_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v10_dd_systems_systemid_cloud_profiles_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Profile identifier.  @#$type&#x3D;xs:string | 
 **cloud_profile_modify** | [**CloudProfileConfig**](CloudProfileConfig.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**CloudProfile**](CloudProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_cloud_profiles_post**
> CloudProfile rest_v10_dd_systems_systemid_cloud_profiles_post(system_id, cloud_profile_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
cloud_profile_create = dd_sdk_1_0.CloudProfileConfig() # CloudProfileConfig | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create cloud profile.
    api_response = api_instance.rest_v10_dd_systems_systemid_cloud_profiles_post(system_id, cloud_profile_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v10_dd_systems_systemid_cloud_profiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **cloud_profile_create** | [**CloudProfileConfig**](CloudProfileConfig.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**CloudProfile**](CloudProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_cloud_profiles_id_get**
> CloudProfileDetail20 rest_v20_dd_systems_systemid_cloud_profiles_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get a cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Profile identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get a cloud profile.
    api_response = api_instance.rest_v20_dd_systems_systemid_cloud_profiles_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v20_dd_systems_systemid_cloud_profiles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Profile identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**CloudProfileDetail20**](CloudProfileDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_cloud_profiles_id_put**
> CloudProfileDetail20 rest_v20_dd_systems_systemid_cloud_profiles_id_put(system_id, id, cloud_profile_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | Cloud Profile identifier.  @#$type=xs:string
cloud_profile_modify_2_0 = dd_sdk_1_0.CloudProfileModify20() # CloudProfileModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a cloud profile.
    api_response = api_instance.rest_v20_dd_systems_systemid_cloud_profiles_id_put(system_id, id, cloud_profile_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v20_dd_systems_systemid_cloud_profiles_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| Cloud Profile identifier.  @#$type&#x3D;xs:string | 
 **cloud_profile_modify_2_0** | [**CloudProfileModify20**](CloudProfileModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**CloudProfileDetail20**](CloudProfileDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_cloud_profiles_post**
> CloudProfileDetail20 rest_v20_dd_systems_systemid_cloud_profiles_post(system_id, cloud_profile_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create cloud profile.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CloudProfilesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
cloud_profile_create_2_0 = dd_sdk_1_0.CloudProfileCreate20() # CloudProfileCreate20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create cloud profile.
    api_response = api_instance.rest_v20_dd_systems_systemid_cloud_profiles_post(system_id, cloud_profile_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudProfilesApi->rest_v20_dd_systems_systemid_cloud_profiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **cloud_profile_create_2_0** | [**CloudProfileCreate20**](CloudProfileCreate20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**CloudProfileDetail20**](CloudProfileDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

