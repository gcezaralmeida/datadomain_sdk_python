# RestPcrJobDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**measurement_id** | **int** |  | 
**measurement_description** | **str** |  | 
**user_description** | **str** |  | 
**priority** | [**PcrJobPriority**](PcrJobPriority.md) |  | [optional] 
**state** | [**PcrJobState**](PcrJobState.md) |  | 
**creation_epoch** | **int** |  | 
**snapshot_epoch** | **int** |  | [optional] 
**start_epoch** | **int** |  | [optional] 
**finish_epoch** | **int** |  | [optional] 
**percent_done** | **int** |  | [optional] 
**files_seen_count** | **int** |  | [optional] 
**paths_not_found_count** | **int** |  | [optional] 
**active_tier** | [**TierCompInfo**](TierCompInfo.md) |  | [optional] 
**extended_retention_tier** | [**TierCompInfo**](TierCompInfo.md) |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


