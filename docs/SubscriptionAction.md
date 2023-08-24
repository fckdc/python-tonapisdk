# SubscriptionAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriber** | [**AccountAddress**](AccountAddress.md) |  | 
**subscription** | **str** |  | 
**beneficiary** | [**AccountAddress**](AccountAddress.md) |  | 
**amount** | **int** |  | 
**initial** | **bool** |  | 

## Example

```python
from fdtapi.models.subscription_action import SubscriptionAction

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAction from a JSON string
subscription_action_instance = SubscriptionAction.from_json(json)
# print the JSON string representation of the object
print SubscriptionAction.to_json()

# convert the object into a dict
subscription_action_dict = subscription_action_instance.to_dict()
# create an instance of SubscriptionAction from a dict
subscription_action_form_dict = subscription_action.from_dict(subscription_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


