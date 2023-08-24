# BlockRaw


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workchain** | **int** |  | 
**shard** | **int** |  | 
**seqno** | **int** |  | 
**root_hash** | **str** |  | 
**file_hash** | **str** |  | 

## Example

```python
from fdtapi.models.block_raw import BlockRaw

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRaw from a JSON string
block_raw_instance = BlockRaw.from_json(json)
# print the JSON string representation of the object
print BlockRaw.to_json()

# convert the object into a dict
block_raw_dict = block_raw_instance.to_dict()
# create an instance of BlockRaw from a dict
block_raw_form_dict = block_raw.from_dict(block_raw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


