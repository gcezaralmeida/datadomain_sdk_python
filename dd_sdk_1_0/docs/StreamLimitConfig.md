# StreamLimitConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**write_stream_soft_limit** | **int** | write_stream_soft_limit should be less than the corresponding DD System Limit and no greater than the combined limit. For \&quot;Modify\&quot;, set value to -1 to reset. | [optional] 
**read_stream_soft_limit** | **int** | read_stream_soft_limit should be less than the corresponding DD System Limit and no greater than the combined limit. For \&quot;Modify\&quot;, set value to -1 to reset. | [optional] 
**repl_stream_soft_limit** | **int** | repl_stream_soft_limit should be less than the corresponding DD System Limit and no greater than the combined limit. For \&quot;Modify\&quot;, set value to -1 to reset. | [optional] 
**combined_stream_soft_limit** | **int** | combined_stream_soft_limit should be less than the corresponding DD System Limit and no less than a single limit. For \&quot;Modify\&quot;, set value to -1 to reset. | [optional] 
**combined_stream_hard_limit** | **int** | combined_stream_hard_limit should be less than the corresponding DD System Limit and no less than a single limit. For \&quot;Modify\&quot;, set value to -1 to reset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


