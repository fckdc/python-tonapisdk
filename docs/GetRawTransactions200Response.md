# GetRawTransactions200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[BlockRaw]**](BlockRaw.md) |  | 
**transactions** | **str** |  | 

## Example

```python
from fdtapi.models.get_raw_transactions200_response import GetRawTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawTransactions200Response from a JSON string
get_raw_transactions200_response_instance = GetRawTransactions200Response.from_json(json)
# print the JSON string representation of the object
print GetRawTransactions200Response.to_json()

# convert the object into a dict
get_raw_transactions200_response_dict = get_raw_transactions200_response_instance.to_dict()
# create an instance of GetRawTransactions200Response from a dict
get_raw_transactions200_response_form_dict = get_raw_transactions200_response.from_dict(get_raw_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


