# Validators


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validators** | [**List[Validator]**](Validator.md) |  | 

## Example

```python
from fdtapi.models.validators import Validators

# TODO update the JSON string below
json = "{}"
# create an instance of Validators from a JSON string
validators_instance = Validators.from_json(json)
# print the JSON string representation of the object
print Validators.to_json()

# convert the object into a dict
validators_dict = validators_instance.to_dict()
# create an instance of Validators from a dict
validators_form_dict = validators.from_dict(validators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


