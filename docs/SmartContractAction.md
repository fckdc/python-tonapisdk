# SmartContractAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executor** | [**AccountAddress**](AccountAddress.md) |  | 
**contract** | [**AccountAddress**](AccountAddress.md) |  | 
**ton_attached** | **int** | amount in nanotons | 
**operation** | **str** |  | 
**payload** | **str** |  | [optional] 
**refund** | [**Refund**](Refund.md) |  | [optional] 

## Example

```python
from fdtapi.models.smart_contract_action import SmartContractAction

# TODO update the JSON string below
json = "{}"
# create an instance of SmartContractAction from a JSON string
smart_contract_action_instance = SmartContractAction.from_json(json)
# print the JSON string representation of the object
print SmartContractAction.to_json()

# convert the object into a dict
smart_contract_action_dict = smart_contract_action_instance.to_dict()
# create an instance of SmartContractAction from a dict
smart_contract_action_form_dict = smart_contract_action.from_dict(smart_contract_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


