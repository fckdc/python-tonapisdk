# MessageConsequences


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace** | [**Trace**](Trace.md) |  | 
**risk** | [**Risk**](Risk.md) |  | 
**event** | [**AccountEvent**](AccountEvent.md) |  | 

## Example

```python
from fdtapi.models.message_consequences import MessageConsequences

# TODO update the JSON string below
json = "{}"
# create an instance of MessageConsequences from a JSON string
message_consequences_instance = MessageConsequences.from_json(json)
# print the JSON string representation of the object
print MessageConsequences.to_json()

# convert the object into a dict
message_consequences_dict = message_consequences_instance.to_dict()
# create an instance of MessageConsequences from a dict
message_consequences_form_dict = message_consequences.from_dict(message_consequences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


