# ActionSimplePreview

shortly describes what this action is about.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**action_image** | **str** | a link to an image for this particular action. | [optional] 
**value** | **str** |  | [optional] 
**value_image** | **str** | a link to an image that depicts this action&#39;s asset. | [optional] 
**accounts** | [**List[AccountAddress]**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.action_simple_preview import ActionSimplePreview

# TODO update the JSON string below
json = "{}"
# create an instance of ActionSimplePreview from a JSON string
action_simple_preview_instance = ActionSimplePreview.from_json(json)
# print the JSON string representation of the object
print ActionSimplePreview.to_json()

# convert the object into a dict
action_simple_preview_dict = action_simple_preview_instance.to_dict()
# create an instance of ActionSimplePreview from a dict
action_simple_preview_form_dict = action_simple_preview.from_dict(action_simple_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


