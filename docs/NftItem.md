# NftItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**index** | **int** |  | 
**owner** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**collection** | [**NftItemCollection**](NftItemCollection.md) |  | [optional] 
**verified** | **bool** |  | 
**metadata** | **Dict[str, object]** |  | 
**sale** | [**Sale**](Sale.md) |  | [optional] 
**previews** | [**List[ImagePreview]**](ImagePreview.md) |  | [optional] 
**dns** | **str** |  | [optional] 
**approved_by** | **List[str]** |  | 

## Example

```python
from fdtapi.models.nft_item import NftItem

# TODO update the JSON string below
json = "{}"
# create an instance of NftItem from a JSON string
nft_item_instance = NftItem.from_json(json)
# print the JSON string representation of the object
print NftItem.to_json()

# convert the object into a dict
nft_item_dict = nft_item_instance.to_dict()
# create an instance of NftItem from a dict
nft_item_form_dict = nft_item.from_dict(nft_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


