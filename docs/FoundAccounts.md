# FoundAccounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[FoundAccountsAddressesInner]**](FoundAccountsAddressesInner.md) |  | 

## Example

```python
from fdtapi.models.found_accounts import FoundAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of FoundAccounts from a JSON string
found_accounts_instance = FoundAccounts.from_json(json)
# print the JSON string representation of the object
print FoundAccounts.to_json()

# convert the object into a dict
found_accounts_dict = found_accounts_instance.to_dict()
# create an instance of FoundAccounts from a dict
found_accounts_form_dict = found_accounts.from_dict(found_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


