# JettonsBalances


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[JettonBalance]**](JettonBalance.md) |  | 

## Example

```python
from fdtapi.models.jettons_balances import JettonsBalances

# TODO update the JSON string below
json = "{}"
# create an instance of JettonsBalances from a JSON string
jettons_balances_instance = JettonsBalances.from_json(json)
# print the JSON string representation of the object
print JettonsBalances.to_json()

# convert the object into a dict
jettons_balances_dict = jettons_balances_instance.to_dict()
# create an instance of JettonsBalances from a dict
jettons_balances_form_dict = jettons_balances.from_dict(jettons_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


