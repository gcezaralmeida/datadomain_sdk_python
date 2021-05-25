# MtreeInfoDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**deletable** | **bool** | False when there is a protocol attached on this Mtree | [optional] 
**del_status** | **int** | 0: not deleted; 1: deleted | [optional] 
**ro_status** | **int** | 0: RW; 1: RO | [optional] 
**repl_destination** | **bool** | true: Mtree is a replication destination | [optional] 
**rl_status** | **int** | Retention lock status: 0: never enabled; 1: currently enabled; 2: previously enabled | [optional] 
**rl_mode** | **int** | Retention lock mode: 0: none; 1: governance; 2: compliance | [optional] 
**tenant** | **str** |  | [optional] 
**tenant_unit** | **str** |  | [optional] 
**physical_capacity** | [**Capacity**](Capacity.md) | Physical capacity is currently available | [optional] 
**logical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**capacity_usage_details** | [**list[CapacityUsageDetails]**](CapacityUsageDetails.md) | include tier information | [optional] 
**quota_config** | [**QuotaConfig**](QuotaConfig.md) |  | [optional] 
**protocol_config** | [**list[ProtocolName]**](ProtocolName.md) |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


