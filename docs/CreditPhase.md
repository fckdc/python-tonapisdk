# CreditPhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees_collected** | **int** |  | 
**credit** | **int** |  | 

## Example

```python
from fdtapi.models.credit_phase import CreditPhase

# TODO update the JSON string below
json = "{}"
# create an instance of CreditPhase from a JSON string
credit_phase_instance = CreditPhase.from_json(json)
# print the JSON string representation of the object
print CreditPhase.to_json()

# convert the object into a dict
credit_phase_dict = credit_phase_instance.to_dict()
# create an instance of CreditPhase from a dict
credit_phase_form_dict = credit_phase.from_dict(credit_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


