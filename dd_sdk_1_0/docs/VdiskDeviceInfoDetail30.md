# VdiskDeviceInfoDetail30

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | urlencoded GUID | 
**guid** | **str** |  | 
**wwnn** | **str** |  | 
**name** | **str** |  | [optional] 
**capacity_in_bytes** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**geometry** | [**GeometryConfig**](GeometryConfig.md) |  | [optional] 
**devgrp_name** | **str** |  | [optional] 
**devgrp_guid** | **str** | urlencoded GUID | 
**pool_name** | **str** |  | [optional] 
**pool_guid** | **str** | urlencoded GUID | 
**_property** | [**list[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**lock_info** | [**VdiskLockInfo**](VdiskLockInfo.md) |  | [optional] 
**device_reads_in_bytes** | **int** |  | [optional] 
**device_writes_in_bytes** | **int** |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


