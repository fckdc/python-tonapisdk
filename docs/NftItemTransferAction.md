# NftItemTransferAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**recipient** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**nft** | **str** |  | 
**comment** | **str** |  | [optional] 
**encrypted_comment** | [**EncryptedComment**](EncryptedComment.md) |  | [optional] 
**payload** | **str** | raw hex encoded payload | [optional] 
**refund** | [**Refund**](Refund.md) |  | [optional] 

## Example

```python
from fdtapi.models.nft_item_transfer_action import NftItemTransferAction

# TODO update the JSON string below
json = "{}"
# create an instance of NftItemTransferAction from a JSON string
nft_item_transfer_action_instance = NftItemTransferAction.from_json(json)
# print the JSON string representation of the object
print NftItemTransferAction.to_json()

# convert the object into a dict
nft_item_transfer_action_dict = nft_item_transfer_action_instance.to_dict()
# create an instance of NftItemTransferAction from a dict
nft_item_transfer_action_form_dict = nft_item_transfer_action.from_dict(nft_item_transfer_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


