# DepositStakeAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**staker** | [**AccountAddress**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.deposit_stake_action import DepositStakeAction

# TODO update the JSON string below
json = "{}"
# create an instance of DepositStakeAction from a JSON string
deposit_stake_action_instance = DepositStakeAction.from_json(json)
# print the JSON string representation of the object
print DepositStakeAction.to_json()

# convert the object into a dict
deposit_stake_action_dict = deposit_stake_action_instance.to_dict()
# create an instance of DepositStakeAction from a dict
deposit_stake_action_form_dict = deposit_stake_action.from_dict(deposit_stake_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


