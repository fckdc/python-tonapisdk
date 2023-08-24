# NftItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nft_items** | [**List[NftItem]**](NftItem.md) |  | 

## Example

```python
from fdtapi.models.nft_items import NftItems

# TODO update the JSON string below
json = "{}"
# create an instance of NftItems from a JSON string
nft_items_instance = NftItems.from_json(json)
# print the JSON string representation of the object
print NftItems.to_json()

# convert the object into a dict
nft_items_dict = nft_items_instance.to_dict()
# create an instance of NftItems from a dict
nft_items_form_dict = nft_items.from_dict(nft_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


