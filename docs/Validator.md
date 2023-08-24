# Validator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 

## Example

```python
from fdtapi.models.validator import Validator

# TODO update the JSON string below
json = "{}"
# create an instance of Validator from a JSON string
validator_instance = Validator.from_json(json)
# print the JSON string representation of the object
print Validator.to_json()

# convert the object into a dict
validator_dict = validator_instance.to_dict()
# create an instance of Validator from a dict
validator_form_dict = validator.from_dict(validator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


