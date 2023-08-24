# MethodExecutionResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**exit_code** | **int** | tvm exit code | 
**stack** | [**List[TvmStackRecord]**](TvmStackRecord.md) |  | 
**decoded** | **object** |  | [optional] 

## Example

```python
from fdtapi.models.method_execution_result import MethodExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of MethodExecutionResult from a JSON string
method_execution_result_instance = MethodExecutionResult.from_json(json)
# print the JSON string representation of the object
print MethodExecutionResult.to_json()

# convert the object into a dict
method_execution_result_dict = method_execution_result_instance.to_dict()
# create an instance of MethodExecutionResult from a dict
method_execution_result_form_dict = method_execution_result.from_dict(method_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


