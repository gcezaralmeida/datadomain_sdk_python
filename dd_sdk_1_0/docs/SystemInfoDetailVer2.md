# SystemInfoDetailVer2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_history** | [**list[VersionHistoryInfo]**](VersionHistoryInfo.md) | List of historical versions | [optional] 
**serialno** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**uptime** | **str** |  | [optional] 
**uptime_secs** | **int** |  | [optional] 
**admin_email** | **str** |  | [optional] 
**admin_host** | **str** |  | [optional] 
**mem_size** | **int** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**physical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**logical_capacity** | [**Capacity**](Capacity.md) |  | [optional] 
**compression_factor** | **float** |  | [optional] 
**capacity_usage_details** | [**list[CapacityUsageDetails]**](CapacityUsageDetails.md) | include tier information | [optional] 
**license** | [**list[LicenseInfo]**](LicenseInfo.md) |  | [optional] 
**location** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**current_epoch** | **int** |  | [optional] 
**partitions** | [**Partitions**](Partitions.md) |  | [optional] 
**storage_policy** | [**StoragePolicy**](StoragePolicy.md) |  | [optional] 
**compute_policy** | [**ComputePolicy**](ComputePolicy.md) |  | [optional] 
**adopted_node_id** | **int** |  | [optional] 
**cluster_deploy** | [**ClusterInfo**](ClusterInfo.md) | cluster deploy information | [optional] 
**cluster_adopt** | [**ClusterInfo**](ClusterInfo.md) | cluster adopt information | [optional] 
**pphrase_info** | [**PphraseInfo**](PphraseInfo.md) |  | [optional] 
**controller_type** | [**ClusterType**](ClusterType.md) |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**power_action_info** | [**list[PowerActionInfo]**](PowerActionInfo.md) |  | [optional] 
**headswap_action_info** | [**HeadswapResultInfo**](HeadswapResultInfo.md) |  | [optional] 
**disaster_recovery_config_info** | [**list[DrConfigInfo]**](DrConfigInfo.md) | Disaster recovery configuration information | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


