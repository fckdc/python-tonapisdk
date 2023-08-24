# AccountEvents


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AccountEvent]**](AccountEvent.md) |  | 
**next_from** | **int** |  | 

## Example

```python
from fdtapi.models.account_events import AccountEvents

# TODO update the JSON string below
json = "{}"
# create an instance of AccountEvents from a JSON string
account_events_instance = AccountEvents.from_json(json)
# print the JSON string representation of the object
print AccountEvents.to_json()

# convert the object into a dict
account_events_dict = account_events_instance.to_dict()
# create an instance of AccountEvents from a dict
account_events_form_dict = account_events.from_dict(account_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


