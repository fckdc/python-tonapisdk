# TraceIDs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traces** | [**List[TraceID]**](TraceID.md) |  | 

## Example

```python
from fdtapi.models.trace_ids import TraceIDs

# TODO update the JSON string below
json = "{}"
# create an instance of TraceIDs from a JSON string
trace_ids_instance = TraceIDs.from_json(json)
# print the JSON string representation of the object
print TraceIDs.to_json()

# convert the object into a dict
trace_ids_dict = trace_ids_instance.to_dict()
# create an instance of TraceIDs from a dict
trace_ids_form_dict = trace_ids.from_dict(trace_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


