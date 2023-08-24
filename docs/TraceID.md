# TraceID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**utime** | **int** |  | 

## Example

```python
from fdtapi.models.trace_id import TraceID

# TODO update the JSON string below
json = "{}"
# create an instance of TraceID from a JSON string
trace_id_instance = TraceID.from_json(json)
# print the JSON string representation of the object
print TraceID.to_json()

# convert the object into a dict
trace_id_dict = trace_id_instance.to_dict()
# create an instance of TraceID from a dict
trace_id_form_dict = trace_id.from_dict(trace_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


