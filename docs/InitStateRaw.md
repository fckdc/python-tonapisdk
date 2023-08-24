# InitStateRaw


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workchain** | **int** |  | 
**root_hash** | **str** |  | 
**file_hash** | **str** |  | 

## Example

```python
from fdtapi.models.init_state_raw import InitStateRaw

# TODO update the JSON string below
json = "{}"
# create an instance of InitStateRaw from a JSON string
init_state_raw_instance = InitStateRaw.from_json(json)
# print the JSON string representation of the object
print InitStateRaw.to_json()

# convert the object into a dict
init_state_raw_dict = init_state_raw_instance.to_dict()
# create an instance of InitStateRaw from a dict
init_state_raw_form_dict = init_state_raw.from_dict(init_state_raw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


