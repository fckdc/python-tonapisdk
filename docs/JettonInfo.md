# JettonInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mintable** | **bool** |  | 
**total_supply** | **str** |  | 
**metadata** | [**JettonMetadata**](JettonMetadata.md) |  | 
**verification** | [**JettonVerificationType**](JettonVerificationType.md) |  | 
**holders_count** | **int** |  | 

## Example

```python
from fdtapi.models.jetton_info import JettonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JettonInfo from a JSON string
jetton_info_instance = JettonInfo.from_json(json)
# print the JSON string representation of the object
print JettonInfo.to_json()

# convert the object into a dict
jetton_info_dict = jetton_info_instance.to_dict()
# create an instance of JettonInfo from a dict
jetton_info_form_dict = jetton_info.from_dict(jetton_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


