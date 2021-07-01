# MtreeInfoDetail30

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**data_access_ip** | **str** |  | [optional] 
**data_availability** | **str** |  | 
**is_degraded** | [**MtreeIsdegraded**](MtreeIsdegraded.md) | true: MTree degraded status | [optional] 
**degraded_by** | [**MtreeDegradedby**](MtreeDegradedby.md) | Mtree Degraded by: ips; | [optional] 
**deletable** | [**MtreeIsDeletable**](MtreeIsDeletable.md) | False when there is a protocol attached on this MTree | [optional] 
**del_status** | [**MtreeIsDeleted**](MtreeIsDeleted.md) | 0: not deleted; 1: deleted | [optional] 
**ro_status** | [**MtreeIsReadOnly**](MtreeIsReadOnly.md) | 0: RW; 1: RO | [optional] 
**data_type** | [**MtreeDataType**](MtreeDataType.md) | 0: local; 1: replica; 2: mixed | [optional] 
**replication_info** | [**MtreeReplicationInfo**](MtreeReplicationInfo.md) | Mtree replication information | [optional] 
**repl_destination** | [**MtreeIsReplDest**](MtreeIsReplDest.md) | true: MTree is a replication destination | [optional] 
**mtree_rl_detail** | [**RetentionLockDetail**](RetentionLockDetail.md) | Retention lock detail: mode; status; retention period limits; uuid | [optional] 
**tenant** | **str** |  | [optional] 
**tenant_unit** | **str** |  | [optional] 
**physical_capacity** | [**Capacity**](Capacity.md) | Physical capacity is currently available | [optional] 
**logical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**capacity_usage_details** | [**list[CapacityUsageDetails]**](CapacityUsageDetails.md) | include tier information | [optional] 
**quota_config** | [**QuotaConfig**](QuotaConfig.md) |  | [optional] 
**protocol_config** | [**list[ProtocolName]**](ProtocolName.md) |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


