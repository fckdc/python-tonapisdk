# NftCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**next_item_index** | **int** |  | 
**owner** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**raw_collection_content** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fdtapi.models.nft_collection import NftCollection

# TODO update the JSON string below
json = "{}"
# create an instance of NftCollection from a JSON string
nft_collection_instance = NftCollection.from_json(json)
# print the JSON string representation of the object
print NftCollection.to_json()

# convert the object into a dict
nft_collection_dict = nft_collection_instance.to_dict()
# create an instance of NftCollection from a dict
nft_collection_form_dict = nft_collection.from_dict(nft_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


