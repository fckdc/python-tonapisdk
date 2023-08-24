# NftPurchaseAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auction_type** | **str** |  | 
**amount** | [**Price**](Price.md) |  | 
**nft** | [**NftItem**](NftItem.md) |  | 
**seller** | [**AccountAddress**](AccountAddress.md) |  | 
**buyer** | [**AccountAddress**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.nft_purchase_action import NftPurchaseAction

# TODO update the JSON string below
json = "{}"
# create an instance of NftPurchaseAction from a JSON string
nft_purchase_action_instance = NftPurchaseAction.from_json(json)
# print the JSON string representation of the object
print NftPurchaseAction.to_json()

# convert the object into a dict
nft_purchase_action_dict = nft_purchase_action_instance.to_dict()
# create an instance of NftPurchaseAction from a dict
nft_purchase_action_form_dict = nft_purchase_action.from_dict(nft_purchase_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


