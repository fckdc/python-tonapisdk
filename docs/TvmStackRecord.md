# TvmStackRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**cell** | **str** |  | [optional] 
**slice** | **str** |  | [optional] 
**num** | **str** |  | [optional] 
**tuple** | [**List[TvmStackRecord]**](TvmStackRecord.md) |  | [optional] 

## Example

```python
from fdtapi.models.tvm_stack_record import TvmStackRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TvmStackRecord from a JSON string
tvm_stack_record_instance = TvmStackRecord.from_json(json)
# print the JSON string representation of the object
print TvmStackRecord.to_json()

# convert the object into a dict
tvm_stack_record_dict = tvm_stack_record_instance.to_dict()
# create an instance of TvmStackRecord from a dict
tvm_stack_record_form_dict = tvm_stack_record.from_dict(tvm_stack_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


