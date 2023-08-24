# ActionPhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**total_actions** | **int** |  | 
**skipped_actions** | **int** |  | 
**fwd_fees** | **int** |  | 
**total_fees** | **int** |  | 

## Example

```python
from fdtapi.models.action_phase import ActionPhase

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPhase from a JSON string
action_phase_instance = ActionPhase.from_json(json)
# print the JSON string representation of the object
print ActionPhase.to_json()

# convert the object into a dict
action_phase_dict = action_phase_instance.to_dict()
# create an instance of ActionPhase from a dict
action_phase_form_dict = action_phase.from_dict(action_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


