# AccountStakingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | **str** |  | 
**amount** | **int** |  | 
**pending_deposit** | **int** |  | 
**pending_withdraw** | **int** |  | 
**ready_withdraw** | **int** |  | 

## Example

```python
from fdtapi.models.account_staking_info import AccountStakingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStakingInfo from a JSON string
account_staking_info_instance = AccountStakingInfo.from_json(json)
# print the JSON string representation of the object
print AccountStakingInfo.to_json()

# convert the object into a dict
account_staking_info_dict = account_staking_info_instance.to_dict()
# create an instance of AccountStakingInfo from a dict
account_staking_info_form_dict = account_staking_info.from_dict(account_staking_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


