# GetRawMasterchainInfo200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | [**BlockRaw**](BlockRaw.md) |  | 
**state_root_hash** | **str** |  | 
**init** | [**InitStateRaw**](InitStateRaw.md) |  | 

## Example

```python
from fdtapi.models.get_raw_masterchain_info200_response import GetRawMasterchainInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawMasterchainInfo200Response from a JSON string
get_raw_masterchain_info200_response_instance = GetRawMasterchainInfo200Response.from_json(json)
# print the JSON string representation of the object
print GetRawMasterchainInfo200Response.to_json()

# convert the object into a dict
get_raw_masterchain_info200_response_dict = get_raw_masterchain_info200_response_instance.to_dict()
# create an instance of GetRawMasterchainInfo200Response from a dict
get_raw_masterchain_info200_response_form_dict = get_raw_masterchain_info200_response.from_dict(get_raw_masterchain_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


