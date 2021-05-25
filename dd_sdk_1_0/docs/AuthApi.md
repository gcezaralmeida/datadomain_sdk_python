# dd_sdk_1_0.AuthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_auth_delete**](AuthApi.md#rest_v10_auth_delete) | **DELETE** /rest/v1.0/auth | Delete authentication token.
[**rest_v10_auth_post**](AuthApi.md#rest_v10_auth_post) | **POST** /rest/v1.0/auth | Create authentication token.


# **rest_v10_auth_delete**
> ServiceStatus rest_v10_auth_delete(authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete authentication token.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AuthApi()
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete authentication token.
    api_response = api_instance.rest_v10_auth_delete(authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->rest_v10_auth_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_v10_auth_post**
> ServiceStatus rest_v10_auth_post(auth_info)

Create authentication token.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.AuthApi()
auth_info = dd_sdk_1_0.AuthInfo() # AuthInfo | 

try:
    # Create authentication token.
    api_response = api_instance.rest_v10_auth_post(auth_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->rest_v10_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_info** | [**AuthInfo**](AuthInfo.md)|  | 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

