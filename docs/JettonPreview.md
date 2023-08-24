# JettonPreview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 
**decimals** | **int** |  | 
**image** | **str** |  | 
**verification** | [**JettonVerificationType**](JettonVerificationType.md) |  | 

## Example

```python
from fdtapi.models.jetton_preview import JettonPreview

# TODO update the JSON string below
json = "{}"
# create an instance of JettonPreview from a JSON string
jetton_preview_instance = JettonPreview.from_json(json)
# print the JSON string representation of the object
print JettonPreview.to_json()

# convert the object into a dict
jetton_preview_dict = jetton_preview_instance.to_dict()
# create an instance of JettonPreview from a dict
jetton_preview_form_dict = jetton_preview.from_dict(jetton_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


