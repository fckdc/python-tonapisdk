# GetRawConfig200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** |  | 
**id** | [**BlockRaw**](BlockRaw.md) |  | 
**state_proof** | **str** |  | 
**config_proof** | **str** |  | 

## Example

```python
from fdtapi.models.get_raw_config200_response import GetRawConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawConfig200Response from a JSON string
get_raw_config200_response_instance = GetRawConfig200Response.from_json(json)
# print the JSON string representation of the object
print GetRawConfig200Response.to_json()

# convert the object into a dict
get_raw_config200_response_dict = get_raw_config200_response_instance.to_dict()
# create an instance of GetRawConfig200Response from a dict
get_raw_config200_response_form_dict = get_raw_config200_response.from_dict(get_raw_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


