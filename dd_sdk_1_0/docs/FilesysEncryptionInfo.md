# FilesysEncryptionInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_info** | [**list[EncryptionInfo]**](EncryptionInfo.md) |  | [optional] 
**algorithm_info** | [**AlgorithmInfo**](AlgorithmInfo.md) |  | [optional] 
**filesys_lock_info** | **str** |  | [optional] 
**key_manager_in_use** | **str** |  | [optional] 
**key_manager_server** | [**HostStr**](HostStr.md) |  | [optional] 
**key_manager_port** | [**PortNumber**](PortNumber.md) |  | [optional] 
**key_manager_fips_mode** | [**KeyManagerFipsMode**](KeyManagerFipsMode.md) |  | [optional] 
**key_manager_key_class** | **str** |  | [optional] 
**key_manager_kmip_user** | **str** |  | [optional] 
**key_rotation_period** | [**KeyManagerKeyRotationPolicy**](KeyManagerKeyRotationPolicy.md) |  | [optional] 
**last_key_rotation_date** | **int** |  | [optional] 
**next_key_rotation_date** | **int** |  | [optional] 
**key_rotation_without_fs_restart** | **bool** |  | [optional] 
**system_wide_encryption** | **bool** |  | [optional] 
**cloud_tier_wide_encryption** | **bool** |  | [optional] 
**active_tier_wide_encryption** | **bool** |  | [optional] 
**action_needed** | **str** |  | [optional] 
**abort_or_apply_change_status** | **str** |  | [optional] 
**link** | [**list[RestLinkRep]**](RestLinkRep.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


