# Accounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[Account]**](Account.md) |  | 

## Example

```python
from fdtapi.models.accounts import Accounts

# TODO update the JSON string below
json = "{}"
# create an instance of Accounts from a JSON string
accounts_instance = Accounts.from_json(json)
# print the JSON string representation of the object
print Accounts.to_json()

# convert the object into a dict
accounts_dict = accounts_instance.to_dict()
# create an instance of Accounts from a dict
accounts_form_dict = accounts.from_dict(accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


