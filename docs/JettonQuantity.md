# JettonQuantity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | 
**wallet_address** | [**AccountAddress**](AccountAddress.md) |  | 
**jetton** | [**JettonPreview**](JettonPreview.md) |  | 

## Example

```python
from fdtapi.models.jetton_quantity import JettonQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of JettonQuantity from a JSON string
jetton_quantity_instance = JettonQuantity.from_json(json)
# print the JSON string representation of the object
print JettonQuantity.to_json()

# convert the object into a dict
jetton_quantity_dict = jetton_quantity_instance.to_dict()
# create an instance of JettonQuantity from a dict
jetton_quantity_form_dict = jetton_quantity.from_dict(jetton_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


