# TonTransferAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | [**AccountAddress**](AccountAddress.md) |  | 
**recipient** | [**AccountAddress**](AccountAddress.md) |  | 
**amount** | **int** | amount in nanotons | 
**comment** | **str** |  | [optional] 
**encrypted_comment** | [**EncryptedComment**](EncryptedComment.md) |  | [optional] 
**refund** | [**Refund**](Refund.md) |  | [optional] 

## Example

```python
from fdtapi.models.ton_transfer_action import TonTransferAction

# TODO update the JSON string below
json = "{}"
# create an instance of TonTransferAction from a JSON string
ton_transfer_action_instance = TonTransferAction.from_json(json)
# print the JSON string representation of the object
print TonTransferAction.to_json()

# convert the object into a dict
ton_transfer_action_dict = ton_transfer_action_instance.to_dict()
# create an instance of TonTransferAction from a dict
ton_transfer_action_form_dict = ton_transfer_action.from_dict(ton_transfer_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


