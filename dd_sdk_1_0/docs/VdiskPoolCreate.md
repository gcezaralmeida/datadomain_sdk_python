# VdiskPoolCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | required pool name. Creation will fail if name contains \&quot;:\&quot; \&quot;\\\&quot; \&quot;/\&quot; \&quot;(\&quot; \&quot;)\&quot; \&quot;,\&quot; \&quot;?\&quot; or \&quot;*\&quot; or reserved words: \&quot;all\&quot;, \&quot;pool\&quot; and \&quot;device-group\&quot;. Maximum number of characters allowed is 32. | 
**user** | **str** | required user name | 
**tenant_unit** | **str** |  | [optional] 
**quota_config** | [**QuotaConfig**](QuotaConfig.md) |  | [optional] 
**_property** | [**list[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**enable** | **bool** | If \&quot;register\&quot; is TRUE, then pool is created from mtree replica | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


