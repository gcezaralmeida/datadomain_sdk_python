# VdiskDevgrpCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | required device group name. Creation will fail if name contains \&quot;:\&quot; \&quot;\\\&quot; \&quot;/\&quot; \&quot;(\&quot; \&quot;)\&quot; \&quot;,\&quot; \&quot;?\&quot; or \&quot;*\&quot; or reserved words: \&quot;all\&quot;, \&quot;pool\&quot; and \&quot;device-group\&quot;. Maximum number of characters allowed is 32. | 
**pool_guid** | **str** | required pool guid | 
**_property** | [**list[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


