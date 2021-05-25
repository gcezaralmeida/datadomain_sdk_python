# UserCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**password** | [**Password**](Password.md) |  | 
**min_days_between_change** | **int** | min_days_between_change does not apply if role is security | [optional] 
**max_days_between_change** | **int** |  | [optional] 
**warn_days_before_expire** | **int** |  | [optional] 
**disable_days_after_expire** | **int** | disable_days_after_expire does not apply if role is security | [optional] 
**disable_date** | [**DateFormat**](DateFormat.md) | Date format is YYYY/MM/DD, does not apply if role is security | [optional] 
**force_password_change** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


