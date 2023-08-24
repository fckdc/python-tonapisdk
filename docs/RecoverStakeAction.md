# RecoverStakeAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**staker** | [**AccountAddress**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.recover_stake_action import RecoverStakeAction

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverStakeAction from a JSON string
recover_stake_action_instance = RecoverStakeAction.from_json(json)
# print the JSON string representation of the object
print RecoverStakeAction.to_json()

# convert the object into a dict
recover_stake_action_dict = recover_stake_action_instance.to_dict()
# create an instance of RecoverStakeAction from a dict
recover_stake_action_form_dict = recover_stake_action.from_dict(recover_stake_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


