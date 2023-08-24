# JettonTransferAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**recipient** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**senders_wallet** | **str** |  | 
**recipients_wallet** | **str** |  | 
**amount** | **str** | amount in quanta of tokens | 
**comment** | **str** |  | [optional] 
**encrypted_comment** | [**EncryptedComment**](EncryptedComment.md) |  | [optional] 
**refund** | [**Refund**](Refund.md) |  | [optional] 
**jetton** | [**JettonPreview**](JettonPreview.md) |  | 

## Example

```python
from fdtapi.models.jetton_transfer_action import JettonTransferAction

# TODO update the JSON string below
json = "{}"
# create an instance of JettonTransferAction from a JSON string
jetton_transfer_action_instance = JettonTransferAction.from_json(json)
# print the JSON string representation of the object
print JettonTransferAction.to_json()

# convert the object into a dict
jetton_transfer_action_dict = jetton_transfer_action_instance.to_dict()
# create an instance of JettonTransferAction from a dict
jetton_transfer_action_form_dict = jetton_transfer_action.from_dict(jetton_transfer_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


