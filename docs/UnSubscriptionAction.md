# UnSubscriptionAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriber** | [**AccountAddress**](AccountAddress.md) |  | 
**subscription** | **str** |  | 
**beneficiary** | [**AccountAddress**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.un_subscription_action import UnSubscriptionAction

# TODO update the JSON string below
json = "{}"
# create an instance of UnSubscriptionAction from a JSON string
un_subscription_action_instance = UnSubscriptionAction.from_json(json)
# print the JSON string representation of the object
print UnSubscriptionAction.to_json()

# convert the object into a dict
un_subscription_action_dict = un_subscription_action_instance.to_dict()
# create an instance of UnSubscriptionAction from a dict
un_subscription_action_form_dict = un_subscription_action.from_dict(un_subscription_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


