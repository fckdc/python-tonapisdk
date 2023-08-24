# JettonSwapAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dex** | **str** |  | 
**amount_in** | **str** |  | 
**amount_out** | **str** |  | 
**user_wallet** | [**AccountAddress**](AccountAddress.md) |  | 
**router** | [**AccountAddress**](AccountAddress.md) |  | 
**jetton_wallet_in** | **str** |  | 
**jetton_master_in** | [**JettonPreview**](JettonPreview.md) |  | 
**jetton_wallet_out** | **str** |  | 
**jetton_master_out** | [**JettonPreview**](JettonPreview.md) |  | 

## Example

```python
from fdtapi.models.jetton_swap_action import JettonSwapAction

# TODO update the JSON string below
json = "{}"
# create an instance of JettonSwapAction from a JSON string
jetton_swap_action_instance = JettonSwapAction.from_json(json)
# print the JSON string representation of the object
print JettonSwapAction.to_json()

# convert the object into a dict
jetton_swap_action_dict = jetton_swap_action_instance.to_dict()
# create an instance of JettonSwapAction from a dict
jetton_swap_action_form_dict = jetton_swap_action.from_dict(jetton_swap_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


