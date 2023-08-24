# Transactions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[Transaction]**](Transaction.md) |  | 

## Example

```python
from fdtapi.models.transactions import Transactions

# TODO update the JSON string below
json = "{}"
# create an instance of Transactions from a JSON string
transactions_instance = Transactions.from_json(json)
# print the JSON string representation of the object
print Transactions.to_json()

# convert the object into a dict
transactions_dict = transactions_instance.to_dict()
# create an instance of Transactions from a dict
transactions_form_dict = transactions.from_dict(transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


