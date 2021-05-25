# dd_sdk_1_0.MtreesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_dd_systems_systemid_mtrees_get**](MtreesApi.md#rest_v10_dd_systems_systemid_mtrees_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/mtrees | Get MTree information.
[**rest_v10_dd_systems_systemid_mtrees_id_delete**](MtreesApi.md#rest_v10_dd_systems_systemid_mtrees_id_delete) | **DELETE** /rest/v1.0/dd-systems/{SYSTEM-ID}/mtrees/{ID} | Delete an MTree.
[**rest_v10_dd_systems_systemid_mtrees_id_get**](MtreesApi.md#rest_v10_dd_systems_systemid_mtrees_id_get) | **GET** /rest/v1.0/dd-systems/{SYSTEM-ID}/mtrees/{ID} | Get an MTree.
[**rest_v10_dd_systems_systemid_mtrees_id_put**](MtreesApi.md#rest_v10_dd_systems_systemid_mtrees_id_put) | **PUT** /rest/v1.0/dd-systems/{SYSTEM-ID}/mtrees/{ID} | Modify an MTree.
[**rest_v10_dd_systems_systemid_mtrees_post**](MtreesApi.md#rest_v10_dd_systems_systemid_mtrees_post) | **POST** /rest/v1.0/dd-systems/{SYSTEM-ID}/mtrees | Create an MTree.
[**rest_v20_dd_systems_systemid_mtrees_get**](MtreesApi.md#rest_v20_dd_systems_systemid_mtrees_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/mtrees | Get MTree information.
[**rest_v20_dd_systems_systemid_mtrees_id_get**](MtreesApi.md#rest_v20_dd_systems_systemid_mtrees_id_get) | **GET** /rest/v2.0/dd-systems/{SYSTEM-ID}/mtrees/{ID} | Get an MTree.
[**rest_v20_dd_systems_systemid_mtrees_id_put**](MtreesApi.md#rest_v20_dd_systems_systemid_mtrees_id_put) | **PUT** /rest/v2.0/dd-systems/{SYSTEM-ID}/mtrees/{ID} | Modify an MTree.
[**rest_v30_dd_systems_systemid_mtrees_get**](MtreesApi.md#rest_v30_dd_systems_systemid_mtrees_get) | **GET** /rest/v3.0/dd-systems/{SYSTEM-ID}/mtrees | Get MTree information.
[**rest_v30_dd_systems_systemid_mtrees_id_get**](MtreesApi.md#rest_v30_dd_systems_systemid_mtrees_id_get) | **GET** /rest/v3.0/dd-systems/{SYSTEM-ID}/mtrees/{ID} | Get an MTree.


# **rest_v10_dd_systems_systemid_mtrees_get**
> MtreeInfos rest_v10_dd_systems_systemid_mtrees_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get MTree information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,repl_dst,tenant_unit,avail_cap_pct,used_cap_pct\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=mtreeSortQuery (optional)
filter = 'filter_example' # str | filter=\"name=regex and avail_cap_pct=range and used_cap_pct=range and repl_dst=true_or_false and tenant_unit=regex\". The range should be (min, max) or (,max) or (min,). value is percentage, e.g we use 20 to represent 20 percentage. regex means regular expression.  @#$type=mtreeFilterQuery (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get MTree information.
    api_response = api_instance.rest_v10_dd_systems_systemid_mtrees_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v10_dd_systems_systemid_mtrees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,repl_dst,tenant_unit,avail_cap_pct,used_cap_pct\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;mtreeSortQuery | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;regex and avail_cap_pct&#x3D;range and used_cap_pct&#x3D;range and repl_dst&#x3D;true_or_false and tenant_unit&#x3D;regex\&quot;. The range should be (min, max) or (,max) or (min,). value is percentage, e.g we use 20 to represent 20 percentage. regex means regular expression.  @#$type&#x3D;mtreeFilterQuery | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeInfos**](MtreeInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_mtrees_id_delete**
> ServiceStatus rest_v10_dd_systems_systemid_mtrees_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Delete an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Delete an MTree.
    api_response = api_instance.rest_v10_dd_systems_systemid_mtrees_id_delete(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v10_dd_systems_systemid_mtrees_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
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

# **rest_v10_dd_systems_systemid_mtrees_id_get**
> MtreeInfoDetail rest_v10_dd_systems_systemid_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get an MTree.
    api_response = api_instance.rest_v10_dd_systems_systemid_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v10_dd_systems_systemid_mtrees_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeInfoDetail**](MtreeInfoDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_mtrees_id_put**
> MtreeInfo rest_v10_dd_systems_systemid_mtrees_id_put(system_id, id, mtree_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
mtree_modify = dd_sdk_1_0.MtreeModify() # MtreeModify | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an MTree.
    api_response = api_instance.rest_v10_dd_systems_systemid_mtrees_id_put(system_id, id, mtree_modify, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v10_dd_systems_systemid_mtrees_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **mtree_modify** | [**MtreeModify**](MtreeModify.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**MtreeInfo**](MtreeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_dd_systems_systemid_mtrees_post**
> MtreeInfo rest_v10_dd_systems_systemid_mtrees_post(system_id, mtree_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Create an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
mtree_create = dd_sdk_1_0.MtreeCreate() # MtreeCreate | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Create an MTree.
    api_response = api_instance.rest_v10_dd_systems_systemid_mtrees_post(system_id, mtree_create, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v10_dd_systems_systemid_mtrees_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **mtree_create** | [**MtreeCreate**](MtreeCreate.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**MtreeInfo**](MtreeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_mtrees_get**
> MtreeInfos rest_v20_dd_systems_systemid_mtrees_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get MTree information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,repl_dst,tenant_unit,avail_cap_pct,used_cap_pct,used_cap_bytes,data_availability\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=mtreeSortQuery_2_0 (optional)
filter = 'filter_example' # str | filter=\"name=regex and avail_cap_pct=range and used_cap_pct=range and repl_dst=true_or_false and tenant_unit=regex and used_cap_bytes=range and access_protocol=regex and data_availability=full, partial or none\". The range should be (min, max) or (,max) or (min,). regex means regular expression. access_protocol can be CIFS, NFS, DD Boost, VTL, vDisk  @#$type=mtreeFilterQuery_2_0 (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get MTree information.
    api_response = api_instance.rest_v20_dd_systems_systemid_mtrees_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v20_dd_systems_systemid_mtrees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,repl_dst,tenant_unit,avail_cap_pct,used_cap_pct,used_cap_bytes,data_availability\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;mtreeSortQuery_2_0 | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;regex and avail_cap_pct&#x3D;range and used_cap_pct&#x3D;range and repl_dst&#x3D;true_or_false and tenant_unit&#x3D;regex and used_cap_bytes&#x3D;range and access_protocol&#x3D;regex and data_availability&#x3D;full, partial or none\&quot;. The range should be (min, max) or (,max) or (min,). regex means regular expression. access_protocol can be CIFS, NFS, DD Boost, VTL, vDisk  @#$type&#x3D;mtreeFilterQuery_2_0 | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeInfos**](MtreeInfos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_mtrees_id_get**
> MtreeInfoDetail20 rest_v20_dd_systems_systemid_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get an MTree.
    api_response = api_instance.rest_v20_dd_systems_systemid_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v20_dd_systems_systemid_mtrees_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeInfoDetail20**](MtreeInfoDetail20.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_dd_systems_systemid_mtrees_id_put**
> MtreeInfo rest_v20_dd_systems_systemid_mtrees_id_put(system_id, id, mtree_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)

Modify an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
mtree_modify_2_0 = dd_sdk_1_0.MtreeModify20() # MtreeModify20 | 
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)

try:
    # Modify an MTree.
    api_response = api_instance.rest_v20_dd_systems_systemid_mtrees_id_put(system_id, id, mtree_modify_2_0, authorization=authorization, x_dd_auth_token=x_dd_auth_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v20_dd_systems_systemid_mtrees_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **mtree_modify_2_0** | [**MtreeModify20**](MtreeModify20.md)|  | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 

### Return type

[**MtreeInfo**](MtreeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v30_dd_systems_systemid_mtrees_get**
> MtreeInfos30 rest_v30_dd_systems_systemid_mtrees_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)

Get MTree information.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
page = 56 # int | page number, starting from 0  @#$type=xs:unsignedInt (optional)
size = 56 # int | Paging size  @#$type=xs:unsignedInt (optional)
sort = 'sort_example' # str | sort=\"name,repl_dst,tenant_unit,avail_cap_pct,used_cap_pct,used_cap_bytes,data_availability\". For descending order, prefix the key with a dash (-). Ex: -name  @#$type=mtreeSortQuery_3_0 (optional)
filter = 'filter_example' # str | filter=\"name=regex and avail_cap_pct=range and used_cap_pct=range and repl_dst=true_or_false and is_degraded=true or false and tenant_unit=regex and used_cap_bytes=range and access_protocol=regex and data_availability=full, partial or none\". The range should be (min, max) or (,max) or (min,). regex means regular expression. access_protocol can be CIFS, NFS, DD Boost, VTL, vDisk  @#$type=mtreeFilterQuery_3_0 (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get MTree information.
    api_response = api_instance.rest_v30_dd_systems_systemid_mtrees_get(system_id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, page=page, size=size, sort=sort, filter=filter, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v30_dd_systems_systemid_mtrees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **page** | **int**| page number, starting from 0  @#$type&#x3D;xs:unsignedInt | [optional] 
 **size** | **int**| Paging size  @#$type&#x3D;xs:unsignedInt | [optional] 
 **sort** | **str**| sort&#x3D;\&quot;name,repl_dst,tenant_unit,avail_cap_pct,used_cap_pct,used_cap_bytes,data_availability\&quot;. For descending order, prefix the key with a dash (-). Ex: -name  @#$type&#x3D;mtreeSortQuery_3_0 | [optional] 
 **filter** | **str**| filter&#x3D;\&quot;name&#x3D;regex and avail_cap_pct&#x3D;range and used_cap_pct&#x3D;range and repl_dst&#x3D;true_or_false and is_degraded&#x3D;true or false and tenant_unit&#x3D;regex and used_cap_bytes&#x3D;range and access_protocol&#x3D;regex and data_availability&#x3D;full, partial or none\&quot;. The range should be (min, max) or (,max) or (min,). regex means regular expression. access_protocol can be CIFS, NFS, DD Boost, VTL, vDisk  @#$type&#x3D;mtreeFilterQuery_3_0 | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeInfos30**](MtreeInfos30.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v30_dd_systems_systemid_mtrees_id_get**
> MtreeInfoDetail30 rest_v30_dd_systems_systemid_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)

Get an MTree.

### Example
```python
from __future__ import print_function
import time
import dd_sdk_1_0
from dd_sdk_1_0.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dd_sdk_1_0.MtreesApi()
system_id = 'system_id_example' # str | DD system identifier.  @#$type=xs:string
id = 'id_example' # str | MTree identifier.  @#$type=xs:string
authorization = 'authorization_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
x_dd_auth_token = 'x_dd_auth_token_example' # str | Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type=xs:string (optional)
exclude_fields = 'exclude_fields_example' # str | Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)
include_fields = 'include_fields_example' # str | Comma separated list of fields to be included in response object. For example, \"msg, status,severity\" for an alert.  @#$type=commaSeparatedStrings (optional)

try:
    # Get an MTree.
    api_response = api_instance.rest_v30_dd_systems_systemid_mtrees_id_get(system_id, id, authorization=authorization, x_dd_auth_token=x_dd_auth_token, exclude_fields=exclude_fields, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtreesApi->rest_v30_dd_systems_systemid_mtrees_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| DD system identifier.  @#$type&#x3D;xs:string | 
 **id** | **str**| MTree identifier.  @#$type&#x3D;xs:string | 
 **authorization** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **x_dd_auth_token** | **str**| Clients need to specify Authorization or X-DD-AUTH-TOKEN.  @#$type&#x3D;xs:string | [optional] 
 **exclude_fields** | **str**| Comma separated list of fields to be excluded from response object. Required and general fields such as paging will not be excluded. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 
 **include_fields** | **str**| Comma separated list of fields to be included in response object. For example, \&quot;msg, status,severity\&quot; for an alert.  @#$type&#x3D;commaSeparatedStrings | [optional] 

### Return type

[**MtreeInfoDetail30**](MtreeInfoDetail30.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

