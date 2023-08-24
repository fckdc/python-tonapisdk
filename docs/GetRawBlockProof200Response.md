# GetRawBlockProof200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** |  | 
**var_from** | [**BlockRaw**](BlockRaw.md) |  | 
**to** | [**BlockRaw**](BlockRaw.md) |  | 
**steps** | [**List[GetRawBlockProof200ResponseStepsInner]**](GetRawBlockProof200ResponseStepsInner.md) |  | 

## Example

```python
from fdtapi.models.get_raw_block_proof200_response import GetRawBlockProof200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawBlockProof200Response from a JSON string
get_raw_block_proof200_response_instance = GetRawBlockProof200Response.from_json(json)
# print the JSON string representation of the object
print GetRawBlockProof200Response.to_json()

# convert the object into a dict
get_raw_block_proof200_response_dict = get_raw_block_proof200_response_instance.to_dict()
# create an instance of GetRawBlockProof200Response from a dict
get_raw_block_proof200_response_form_dict = get_raw_block_proof200_response.from_dict(get_raw_block_proof200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


