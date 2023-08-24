# Sale


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**market** | [**AccountAddress**](AccountAddress.md) |  | 
**owner** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**price** | [**Price**](Price.md) |  | 

## Example

```python
from fdtapi.models.sale import Sale

# TODO update the JSON string below
json = "{}"
# create an instance of Sale from a JSON string
sale_instance = Sale.from_json(json)
# print the JSON string representation of the object
print Sale.to_json()

# convert the object into a dict
sale_dict = sale_instance.to_dict()
# create an instance of Sale from a dict
sale_form_dict = sale.from_dict(sale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


