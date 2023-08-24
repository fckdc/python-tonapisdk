# JettonBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **str** |  | 
**wallet_address** | [**AccountAddress**](AccountAddress.md) |  | 
**jetton** | [**JettonPreview**](JettonPreview.md) |  | 

## Example

```python
from fdtapi.models.jetton_balance import JettonBalance

# TODO update the JSON string below
json = "{}"
# create an instance of JettonBalance from a JSON string
jetton_balance_instance = JettonBalance.from_json(json)
# print the JSON string representation of the object
print JettonBalance.to_json()

# convert the object into a dict
jetton_balance_dict = jetton_balance_instance.to_dict()
# create an instance of JettonBalance from a dict
jetton_balance_form_dict = jetton_balance.from_dict(jetton_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


