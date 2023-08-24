# GetStakingPoolHistory200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apy** | [**List[ApyHistory]**](ApyHistory.md) |  | 

## Example

```python
from fdtapi.models.get_staking_pool_history200_response import GetStakingPoolHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStakingPoolHistory200Response from a JSON string
get_staking_pool_history200_response_instance = GetStakingPoolHistory200Response.from_json(json)
# print the JSON string representation of the object
print GetStakingPoolHistory200Response.to_json()

# convert the object into a dict
get_staking_pool_history200_response_dict = get_staking_pool_history200_response_instance.to_dict()
# create an instance of GetStakingPoolHistory200Response from a dict
get_staking_pool_history200_response_form_dict = get_staking_pool_history200_response.from_dict(get_staking_pool_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


