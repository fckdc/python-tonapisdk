# GetAccountsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **List[str]** |  | 

## Example

```python
from fdtapi.models.get_accounts_request import GetAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsRequest from a JSON string
get_accounts_request_instance = GetAccountsRequest.from_json(json)
# print the JSON string representation of the object
print GetAccountsRequest.to_json()

# convert the object into a dict
get_accounts_request_dict = get_accounts_request_instance.to_dict()
# create an instance of GetAccountsRequest from a dict
get_accounts_request_form_dict = get_accounts_request.from_dict(get_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


