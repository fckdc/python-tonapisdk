# ApyHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apy** | **float** |  | 
**time** | **int** |  | 

## Example

```python
from fdtapi.models.apy_history import ApyHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ApyHistory from a JSON string
apy_history_instance = ApyHistory.from_json(json)
# print the JSON string representation of the object
print ApyHistory.to_json()

# convert the object into a dict
apy_history_dict = apy_history_instance.to_dict()
# create an instance of ApyHistory from a dict
apy_history_form_dict = apy_history.from_dict(apy_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


