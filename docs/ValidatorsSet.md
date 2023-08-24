# ValidatorsSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utime_since** | **int** |  | 
**utime_until** | **int** |  | 
**total** | **int** |  | 
**main** | **int** |  | 
**total_weight** | **int** |  | [optional] 
**list** | [**List[ValidatorsSetListInner]**](ValidatorsSetListInner.md) |  | 

## Example

```python
from fdtapi.models.validators_set import ValidatorsSet

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorsSet from a JSON string
validators_set_instance = ValidatorsSet.from_json(json)
# print the JSON string representation of the object
print ValidatorsSet.to_json()

# convert the object into a dict
validators_set_dict = validators_set_instance.to_dict()
# create an instance of ValidatorsSet from a dict
validators_set_form_dict = validators_set.from_dict(validators_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


