# AccountStaking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pools** | [**List[AccountStakingInfo]**](AccountStakingInfo.md) |  | 

## Example

```python
from fdtapi.models.account_staking import AccountStaking

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStaking from a JSON string
account_staking_instance = AccountStaking.from_json(json)
# print the JSON string representation of the object
print AccountStaking.to_json()

# convert the object into a dict
account_staking_dict = account_staking_instance.to_dict()
# create an instance of AccountStaking from a dict
account_staking_form_dict = account_staking.from_dict(account_staking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


