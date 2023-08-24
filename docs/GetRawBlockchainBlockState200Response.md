# GetRawBlockchainBlockState200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BlockRaw**](BlockRaw.md) |  | 
**root_hash** | **str** |  | 
**file_hash** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from fdtapi.models.get_raw_blockchain_block_state200_response import GetRawBlockchainBlockState200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawBlockchainBlockState200Response from a JSON string
get_raw_blockchain_block_state200_response_instance = GetRawBlockchainBlockState200Response.from_json(json)
# print the JSON string representation of the object
print GetRawBlockchainBlockState200Response.to_json()

# convert the object into a dict
get_raw_blockchain_block_state200_response_dict = get_raw_blockchain_block_state200_response_instance.to_dict()
# create an instance of GetRawBlockchainBlockState200Response from a dict
get_raw_blockchain_block_state200_response_form_dict = get_raw_blockchain_block_state200_response.from_dict(get_raw_blockchain_block_state200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


