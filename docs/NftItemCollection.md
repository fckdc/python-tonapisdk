# NftItemCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from fdtapi.models.nft_item_collection import NftItemCollection

# TODO update the JSON string below
json = "{}"
# create an instance of NftItemCollection from a JSON string
nft_item_collection_instance = NftItemCollection.from_json(json)
# print the JSON string representation of the object
print NftItemCollection.to_json()

# convert the object into a dict
nft_item_collection_dict = nft_item_collection_instance.to_dict()
# create an instance of NftItemCollection from a dict
nft_item_collection_form_dict = nft_item_collection.from_dict(nft_item_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


