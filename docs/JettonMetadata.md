# JettonMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 
**decimals** | **str** |  | 
**image** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**social** | **List[str]** |  | [optional] 
**websites** | **List[str]** |  | [optional] 
**catalogs** | **List[str]** |  | [optional] 

## Example

```python
from fdtapi.models.jetton_metadata import JettonMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of JettonMetadata from a JSON string
jetton_metadata_instance = JettonMetadata.from_json(json)
# print the JSON string representation of the object
print JettonMetadata.to_json()

# convert the object into a dict
jetton_metadata_dict = jetton_metadata_instance.to_dict()
# create an instance of JettonMetadata from a dict
jetton_metadata_form_dict = jetton_metadata.from_dict(jetton_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


