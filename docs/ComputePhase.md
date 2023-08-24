# ComputePhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skipped** | **bool** |  | 
**skip_reason** | [**ComputeSkipReason**](ComputeSkipReason.md) |  | [optional] 
**success** | **bool** |  | [optional] 
**gas_fees** | **int** |  | [optional] 
**gas_used** | **int** |  | [optional] 
**vm_steps** | **int** |  | [optional] 
**exit_code** | **int** |  | [optional] 

## Example

```python
from fdtapi.models.compute_phase import ComputePhase

# TODO update the JSON string below
json = "{}"
# create an instance of ComputePhase from a JSON string
compute_phase_instance = ComputePhase.from_json(json)
# print the JSON string representation of the object
print ComputePhase.to_json()

# convert the object into a dict
compute_phase_dict = compute_phase_instance.to_dict()
# create an instance of ComputePhase from a dict
compute_phase_form_dict = compute_phase.from_dict(compute_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


