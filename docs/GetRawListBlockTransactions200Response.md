# GetRawListBlockTransactions200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BlockRaw**](BlockRaw.md) |  | 
**req_count** | **int** |  | 
**incomplete** | **bool** |  | 
**ids** | [**List[GetRawListBlockTransactions200ResponseIdsInner]**](GetRawListBlockTransactions200ResponseIdsInner.md) |  | 
**proof** | **str** |  | 

## Example

```python
from fdtapi.models.get_raw_list_block_transactions200_response import GetRawListBlockTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawListBlockTransactions200Response from a JSON string
get_raw_list_block_transactions200_response_instance = GetRawListBlockTransactions200Response.from_json(json)
# print the JSON string representation of the object
print GetRawListBlockTransactions200Response.to_json()

# convert the object into a dict
get_raw_list_block_transactions200_response_dict = get_raw_list_block_transactions200_response_instance.to_dict()
# create an instance of GetRawListBlockTransactions200Response from a dict
get_raw_list_block_transactions200_response_form_dict = get_raw_list_block_transactions200_response.from_dict(get_raw_list_block_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


