# dd_sdk_1_0.TrustApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_trust_delete**](TrustApi.md#rest_v10_trust_delete) | **DELETE** /rest/v1.0/trust | 
[**rest_v10_trust_get**](TrustApi.md#rest_v10_trust_get) | **GET** /rest/v1.0/trust | Establish mutual trust with DDR.
[**rest_v10_trust_post**](TrustApi.md#rest_v10_trust_post) | **POST** /rest/v1.0/trust | 
[**rest_v10_trust_put**](TrustApi.md#rest_v10_trust_put) | **PUT** /rest/v1.0/trust | 


# **rest_v10_trust_delete**
> MtrustStatus rest_v10_trust_delete(ca_info)



### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.TrustApi()
ca_info = dd_sdk_1_0.CaInfo() # CaInfo | 

try:
    api_response = api_instance.rest_v10_trust_delete(ca_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustApi->rest_v10_trust_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_info** | [**CaInfo**](CaInfo.md)|  | 

### Return type

[**MtrustStatus**](MtrustStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_trust_get**
> TrustInfo rest_v10_trust_get(exclude_fields=exclude_fields, include_fields=include_fields)

Establish mutual trust with DDR.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.TrustApi()
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Establish mutual trust with DDR.
    api_response = api_instance.rest_v10_trust_get(exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustApi->rest_v10_trust_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**TrustInfo**](TrustInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_trust_post**
> MtrustStatus rest_v10_trust_post(ca_info)



### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.TrustApi()
ca_info = dd_sdk_1_0.CaInfo() # CaInfo | 

try:
    api_response = api_instance.rest_v10_trust_post(ca_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustApi->rest_v10_trust_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_info** | [**CaInfo**](CaInfo.md)|  | 

### Return type

[**MtrustStatus**](MtrustStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_trust_put**
> MtrustStatus rest_v10_trust_put(ca_info)



### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.TrustApi()
ca_info = dd_sdk_1_0.CaInfo() # CaInfo | 

try:
    api_response = api_instance.rest_v10_trust_put(ca_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustApi->rest_v10_trust_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_info** | [**CaInfo**](CaInfo.md)|  | 

### Return type

[**MtrustStatus**](MtrustStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

