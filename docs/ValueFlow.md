# ValueFlow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountAddress**](AccountAddress.md) |  | 
**ton** | **int** |  | 
**fees** | **int** |  | 
**jettons** | [**List[ValueFlowJettonsInner]**](ValueFlowJettonsInner.md) |  | [optional] 

## Example

```python
from fdtapi.models.value_flow import ValueFlow

# TODO update the JSON string below
json = "{}"
# create an instance of ValueFlow from a JSON string
value_flow_instance = ValueFlow.from_json(json)
# print the JSON string representation of the object
print ValueFlow.to_json()

# convert the object into a dict
value_flow_dict = value_flow_instance.to_dict()
# create an instance of ValueFlow from a dict
value_flow_form_dict = value_flow.from_dict(value_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


