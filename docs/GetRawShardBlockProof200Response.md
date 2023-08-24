# GetRawShardBlockProof200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**masterchain_id** | [**BlockRaw**](BlockRaw.md) |  | 
**links** | [**List[GetRawShardBlockProof200ResponseLinksInner]**](GetRawShardBlockProof200ResponseLinksInner.md) |  | 

## Example

```python
from fdtapi.models.get_raw_shard_block_proof200_response import GetRawShardBlockProof200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawShardBlockProof200Response from a JSON string
get_raw_shard_block_proof200_response_instance = GetRawShardBlockProof200Response.from_json(json)
# print the JSON string representation of the object
print GetRawShardBlockProof200Response.to_json()

# convert the object into a dict
get_raw_shard_block_proof200_response_dict = get_raw_shard_block_proof200_response_instance.to_dict()
# create an instance of GetRawShardBlockProof200Response from a dict
get_raw_shard_block_proof200_response_form_dict = get_raw_shard_block_proof200_response.from_dict(get_raw_shard_block_proof200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


