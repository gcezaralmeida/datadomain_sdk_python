# ManagedSystemInfo30

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | url-encoded system uuid | 
**name** | **str** |  | [optional] 
**type** | **str** | Possible values: standalone, HA | [optional] 
**version** | **str** |  | [optional] 
**user_role** | **str** |  | [optional] 
**serialno** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**uptime** | **str** |  | [optional] 
**uptime_secs** | **int** |  | [optional] 
**state** | **str** | Possible values: adding, managed, suspended, unmanaged, deleting | [optional] 
**status** | **str** | Possible values: online, not-responding, not-transmitting, upgrading | [optional] 
**added_epoch** | **int** |  | [optional] 
**hd_sync_epoch** | **int** |  | [optional] 
**cd_sync_epoch** | **int** |  | [optional] 
**admin_email** | **str** |  | [optional] 
**admin_host** | **str** |  | [optional] 
**mem_size** | **int** |  | [optional] 
**partition_size** | **int** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**physical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**logical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**compression_factor** | **float** |  | [optional] 
**capacity_usage_details** | [**list[CapacityUsageDetails]**](CapacityUsageDetails.md) | include tier information | [optional] 
**subscribed_capacity** | **int** |  | [optional] 
**license** | [**list[LicenseInfo]**](LicenseInfo.md) |  | [optional] 
**location** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**system_status** | **str** | HA system status. | [optional] 
**upgrade_schedule_progress_info** | [**UpgradeScheduleProgressInfo**](UpgradeScheduleProgressInfo.md) |  | 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


