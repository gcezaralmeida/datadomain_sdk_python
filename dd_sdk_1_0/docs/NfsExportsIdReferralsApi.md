# dd_sdk_1_0.NfsExportsIdReferralsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_delete**](NfsExportsIdReferralsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_delete) | **DELETE** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/referrals | Delete referrals of an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_get**](NfsExportsIdReferralsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/referrals | List all referrals of an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_post**](NfsExportsIdReferralsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_post) | **POST** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/referrals | Create a referral on an NFS export.
[**rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_put**](NfsExportsIdReferralsApi.md#rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/protocols/nfs/exports/{ID}/referrals | Modify a referral of an NFS export.


# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_delete**
> ServiceStatus rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, referral_list=referral_list)

Delete referrals of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdReferralsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
referral_list = 'referral_list_example' # str | Comma seperated list of referrals  @#$type=referralFilterQuery_2_0 (optional)

try:
    # Delete referrals of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, referral_list=referral_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdReferralsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **referral_list** | **str**| Comma seperated list of referrals  @#$type&#x3D;referralFilterQuery_2_0 | [optional] 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_get**
> ExportReferralsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

List all referrals of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdReferralsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # List all referrals of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdReferralsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**ExportReferralsInfo20**](ExportReferralsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_post**
> ExportReferralsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_post(system_id, id, nfs_export_referral_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create a referral on an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdReferralsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
nfs_export_referral_create_2_0 = dd_sdk_1_0.ExportReferralCreate20() # ExportReferralCreate20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create a referral on an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_post(system_id, id, nfs_export_referral_create_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdReferralsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_referral_create_2_0** | [**ExportReferralCreate20**](ExportReferralCreate20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportReferralsInfo20**](ExportReferralsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_put**
> ExportReferralsInfo20 rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_put(system_id, id, nfs_export_referral_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify a referral of an NFS export.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.NfsExportsIdReferralsApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | NFS export identifier.  @#$type=xs:string
nfs_export_referral_modify_2_0 = dd_sdk_1_0.ExportReferralModify20() # ExportReferralModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify a referral of an NFS export.
    api_response = api_instance.rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_put(system_id, id, nfs_export_referral_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsIdReferralsApi->rest_v20_dd_systems_systemid_protocols_nfs_exports_id_referrals_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| NFS export identifier.  @#$type&#x3D;xs:string | 
 **nfs_export_referral_modify_2_0** | [**ExportReferralModify20**](ExportReferralModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**ExportReferralsInfo20**](ExportReferralsInfo20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

