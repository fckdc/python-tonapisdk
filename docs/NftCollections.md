# NftCollections


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nft_collections** | [**List[NftCollection]**](NftCollection.md) |  | 

## Example

```python
from fdtapi.models.nft_collections import NftCollections

# TODO update the JSON string below
json = "{}"
# create an instance of NftCollections from a JSON string
nft_collections_instance = NftCollections.from_json(json)
# print the JSON string representation of the object
print NftCollections.to_json()

# convert the object into a dict
nft_collections_dict = nft_collections_instance.to_dict()
# create an instance of NftCollections from a dict
nft_collections_form_dict = nft_collections.from_dict(nft_collections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


