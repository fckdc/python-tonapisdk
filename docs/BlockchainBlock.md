# BlockchainBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workchain_id** | **int** |  | 
**shard** | **str** |  | 
**seqno** | **int** |  | 
**root_hash** | **str** |  | 
**file_hash** | **str** |  | 
**global_id** | **int** |  | 
**version** | **int** |  | 
**after_merge** | **bool** |  | 
**before_split** | **bool** |  | 
**after_split** | **bool** |  | 
**want_split** | **bool** |  | 
**want_merge** | **bool** |  | 
**key_block** | **bool** |  | 
**gen_utime** | **int** |  | 
**start_lt** | **int** |  | 
**end_lt** | **int** |  | 
**vert_seqno** | **int** |  | 
**gen_catchain_seqno** | **int** |  | 
**min_ref_mc_seqno** | **int** |  | 
**prev_key_block_seqno** | **int** |  | 
**gen_software_version** | **int** |  | [optional] 
**gen_software_capabilities** | **int** |  | [optional] 
**master_ref** | **str** |  | [optional] 
**prev_refs** | **List[str]** |  | 
**in_msg_descr_length** | **int** |  | 
**out_msg_descr_length** | **int** |  | 
**rand_seed** | **str** |  | 
**created_by** | **str** |  | 

## Example

```python
from fdtapi.models.blockchain_block import BlockchainBlock

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainBlock from a JSON string
blockchain_block_instance = BlockchainBlock.from_json(json)
# print the JSON string representation of the object
print BlockchainBlock.to_json()

# convert the object into a dict
blockchain_block_dict = blockchain_block_instance.to_dict()
# create an instance of BlockchainBlock from a dict
blockchain_block_form_dict = blockchain_block.from_dict(blockchain_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


