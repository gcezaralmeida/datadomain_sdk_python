# dd_sdk_1_0.SsoRegistrationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_sso_registration_id_delete**](SsoRegistrationApi.md#rest_v10_sso_registration_id_delete) | **DELETE** /rest/v1.0/sso-registration/{ID} | Delete OIDC provider info
[**rest_v10_sso_registration_id_put**](SsoRegistrationApi.md#rest_v10_sso_registration_id_put) | **PUT** /rest/v1.0/sso-registration/{ID} | Update OIDC provider info
[**rest_v10_sso_registration_post**](SsoRegistrationApi.md#rest_v10_sso_registration_post) | **POST** /rest/v1.0/sso-registration | Register DDR to OIDC provider.


# **rest_v10_sso_registration_id_delete**
> RegistrationDeleteStatus rest_v10_sso_registration_id_delete(id)

Delete OIDC provider info

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SsoRegistrationApi()
id = 'id_example' # str | SSO client identifier.  @#$type=xs:string

try:
    # Delete OIDC provider info
    api_response = api_instance.rest_v10_sso_registration_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SsoRegistrationApi->rest_v10_sso_registration_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SSO client identifier.  @#$type&#x3D;xs:string | 

### Return type

[**RegistrationDeleteStatus**](RegistrationDeleteStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sso_registration_id_put**
> RegistrationStatus rest_v10_sso_registration_id_put(id, registration_info)

Update OIDC provider info

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SsoRegistrationApi()
id = 'id_example' # str | SSO client identifier.  @#$type=xs:string
registration_info = dd_sdk_1_0.RegistrationInfo() # RegistrationInfo | 

try:
    # Update OIDC provider info
    api_response = api_instance.rest_v10_sso_registration_id_put(id, registration_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SsoRegistrationApi->rest_v10_sso_registration_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SSO client identifier.  @#$type&#x3D;xs:string | 
 **registration_info** | [**RegistrationInfo**](RegistrationInfo.md)|  | 

### Return type

[**RegistrationStatus**](RegistrationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sso_registration_post**
> RegistrationStatus rest_v10_sso_registration_post(registration_info)

Register DDR to OIDC provider.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.SsoRegistrationApi()
registration_info = dd_sdk_1_0.RegistrationInfo() # RegistrationInfo | 

try:
    # Register DDR to OIDC provider.
    api_response = api_instance.rest_v10_sso_registration_post(registration_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SsoRegistrationApi->rest_v10_sso_registration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_info** | [**RegistrationInfo**](RegistrationInfo.md)|  | 

### Return type

[**RegistrationStatus**](RegistrationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

