# StoragePhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees_collected** | **int** |  | 
**fees_due** | **int** |  | [optional] 
**status_change** | [**AccStatusChange**](AccStatusChange.md) |  | 

## Example

```python
from fdtapi.models.storage_phase import StoragePhase

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePhase from a JSON string
storage_phase_instance = StoragePhase.from_json(json)
# print the JSON string representation of the object
print StoragePhase.to_json()

# convert the object into a dict
storage_phase_dict = storage_phase_instance.to_dict()
# create an instance of StoragePhase from a dict
storage_phase_form_dict = storage_phase.from_dict(storage_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


