# GetRawAccountState200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BlockRaw**](BlockRaw.md) |  | 
**shardblk** | [**BlockRaw**](BlockRaw.md) |  | 
**shard_proof** | **str** |  | 
**proof** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from fdtapi.models.get_raw_account_state200_response import GetRawAccountState200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawAccountState200Response from a JSON string
get_raw_account_state200_response_instance = GetRawAccountState200Response.from_json(json)
# print the JSON string representation of the object
print GetRawAccountState200Response.to_json()

# convert the object into a dict
get_raw_account_state200_response_dict = get_raw_account_state200_response_instance.to_dict()
# create an instance of GetRawAccountState200Response from a dict
get_raw_account_state200_response_form_dict = get_raw_account_state200_response.from_dict(get_raw_account_state200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


