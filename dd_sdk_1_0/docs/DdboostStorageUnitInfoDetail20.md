# DdboostStorageUnitInfoDetail20

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | urlencoded Name | 
**name** | **str** |  | [optional] 
**del_status** | [**DdboostStorageUnitDeleteStatus**](DdboostStorageUnitDeleteStatus.md) | 0: not deleted; 1: deleted | [optional] 
**data_availability** | [**DataAvailability**](DataAvailability.md) | Possible values: full, partial, none | 
**num_affected_nodes** | **int** | Number of nodes affected | [optional] 
**data_access_ip** | **str** | Data access IP address | 
**quota_enabled** | **bool** | true: if quota is enabled | 
**pre_comp** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**report_physical_size** | **int** |  | [optional] 
**user** | **str** |  | [optional] 
**tenant_unit** | **str** |  | [optional] 
**logical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**quota_config** | [**QuotaConfig**](QuotaConfig.md) |  | [optional] 
**stream_limit_config** | [**StreamLimitConfig**](StreamLimitConfig.md) |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


