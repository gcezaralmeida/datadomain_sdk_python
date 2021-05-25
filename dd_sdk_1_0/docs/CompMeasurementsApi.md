# dd_sdk_1_0.CompMeasurementsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_stats_compression_measurements_delete**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements | Delete multiple compression measurements
[**rest_v10_dd_systems_systemid_stats_compression_measurements_get**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements | Get the list of compression measurement information
[**rest_v10_dd_systems_systemid_stats_compression_measurements_id_delete**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements/{ID} | Delete a compression measurement, which is not completed.
[**rest_v10_dd_systems_systemid_stats_compression_measurements_id_get**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements/{ID} | Get the detailed information of a specified compression measurement
[**rest_v10_dd_systems_systemid_stats_compression_measurements_id_put**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements/{ID} | Start this job or add more include and exclude paths to a compression measurement
[**rest_v10_dd_systems_systemid_stats_compression_measurements_post**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements | Create a compression measurement. Note that maximum request size is 64k. Client needs to use PUT /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements/{ID} to add more inclue/exclude paths if the total include/exclude paths causes the whole request exceed 64k
[**rest_v10_dd_systems_systemid_stats_compression_measurements_put**](CompMeasurementsApi.md#rest_v10_dd_systems_systemid_stats_compression_measurements_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements | Start multiple compression measurements


# **rest_v10_dd_systems_systemid_stats_compression_measurements_delete**
> ServiceStatus rest_v10_dd_systems_systemid_stats_compression_measurements_delete(system_id, measurements_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete multiple compression measurements

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type=xs:string
measurements_delete = dd_sdk_1_0.RestPcrJobIds() # RestPcrJobIds | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete multiple compression measurements
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_delete(system_id, measurements_delete, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **measurements_delete** | [**RestPcrJobIds**](RestPcrJobIds.md)|  | 
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

# **rest_v10_dd_systems_systemid_stats_compression_measurements_get**
> RestPcrJobs rest_v10_dd_systems_systemid_stats_compression_measurements_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get the list of compression measurement information

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"measurement_id,description,state\". For descending order, prefix the key with a dash (-). Ex: -id  @#$type=restPcrSortQuery (optional)
filter = 'filter_example' # str | filter=\"measurement_id=value and description=value and state=value\". value should be a valid regular expression.  @#$type=restPcrFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get the list of compression measurement information
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;measurement_id,description,state\&quot;. For descending order, prefix the key with a dash (-). Ex: -id  @#$type&#x3D;restPcrSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;measurement_id&#x3D;value and description&#x3D;value and state&#x3D;value\&quot;. value should be a valid regular expression.  @#$type&#x3D;restPcrFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**RestPcrJobs**](RestPcrJobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_stats_compression_measurements_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_stats_compression_measurements_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete a compression measurement, which is not completed.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
id = 'id_example' # str | Measurement ID to specify in compression measurement information  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete a compression measurement, which is not completed.
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **id** | **str**| Measurement ID to specify in compression measurement information  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_stats_compression_measurements_id_get**
> RestPcrJobDetail rest_v10_dd_systems_systemid_stats_compression_measurements_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get the detailed information of a specified compression measurement

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
id = 'id_example' # str | Measurement ID to specify in compression measurement information  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get the detailed information of a specified compression measurement
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **id** | **str**| Measurement ID to specify in compression measurement information  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**RestPcrJobDetail**](RestPcrJobDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_stats_compression_measurements_id_put**
> RestPcrJob rest_v10_dd_systems_systemid_stats_compression_measurements_id_put(system_id, id, measurement_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Start this job or add more include and exclude paths to a compression measurement

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type=xs:string
id = 'id_example' # str | Measurement ID to specify in compression measurement information  @#$type=xs:string
measurement_modify = dd_sdk_1_0.RestPcrJobModify() # RestPcrJobModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Start this job or add more include and exclude paths to a compression measurement
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_id_put(system_id, id, measurement_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or urlencoded uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **id** | **str**| Measurement ID to specify in compression measurement information  @#$type&#x3D;xs:string | 
 **measurement_modify** | [**RestPcrJobModify**](RestPcrJobModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**RestPcrJob**](RestPcrJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_stats_compression_measurements_post**
> RestPcrJob rest_v10_dd_systems_systemid_stats_compression_measurements_post(system_id, measurement_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a compression measurement. Note that maximum request size is 64k. Client needs to use PUT /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements/{ID} to add more inclue/exclude paths if the total include/exclude paths causes the whole request exceed 64k

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type=xs:string
measurement_create = dd_sdk_1_0.RestPcrJobCreate() # RestPcrJobCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a compression measurement. Note that maximum request size is 64k. Client needs to use PUT /rest/v1.0/dd-systems/{SYSTEM-ID}/stats/compression/measurements/{ID} to add more inclue/exclude paths if the total include/exclude paths causes the whole request exceed 64k
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_post(system_id, measurement_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **measurement_create** | [**RestPcrJobCreate**](RestPcrJobCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**RestPcrJob**](RestPcrJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_stats_compression_measurements_put**
> ServiceStatus rest_v10_dd_systems_systemid_stats_compression_measurements_put(system_id, measurements_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Start multiple compression measurements

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.CompMeasurementsApi()
system_id = 'system_id_example' # str | DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type=xs:string
measurements_modify = dd_sdk_1_0.RestPcrJobsModify() # RestPcrJobsModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Start multiple compression measurements
    api_response = api_instance.rest_v10_dd_systems_systemid_stats_compression_measurements_put(system_id, measurements_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompMeasurementsApi->rest_v10_dd_systems_systemid_stats_compression_measurements_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DDR system identifier. It must be zero or uuid of the requesting DDR.  @#$type&#x3D;xs:string | 
 **measurements_modify** | [**RestPcrJobsModify**](RestPcrJobsModify.md)|  | 
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

