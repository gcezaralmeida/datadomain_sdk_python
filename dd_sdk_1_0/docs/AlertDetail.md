# AlertDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | urlencoded combination of system_id, node_id and alert_id. For DDR or managed DDR, the system_id and node_id is 0. | 
**alert_id** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**alert_gen_epoch** | **int** | alert post/generate epoch | [optional] 
**clear_epoch** | **int** | alert clear epoch | [optional] 
**msg** | **str** |  | [optional] 
**additional_info** | **str** |  | [optional] 
**clear_additional_info** | **str** |  | [optional] 
**status** | [**AlertStatus**](AlertStatus.md) |  | [optional] 
**_class** | [**AlertClass**](AlertClass.md) |  | [optional] 
**severity** | [**AlertSeverity**](AlertSeverity.md) |  | [optional] 
**action** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**node_id** | **int** |  | [optional] 
**system_name** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**tenant_name** | **str** |  | [optional] 
**ha_system_name** | **str** |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


