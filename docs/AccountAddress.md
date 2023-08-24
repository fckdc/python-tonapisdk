# AccountAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** | Display name. Data collected from different sources like moderation lists, dns, collections names and over. | [optional] 
**is_scam** | **bool** | Is this account was marked as part of scammers activity | 
**icon** | **str** |  | [optional] 

## Example

```python
from fdtapi.models.account_address import AccountAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAddress from a JSON string
account_address_instance = AccountAddress.from_json(json)
# print the JSON string representation of the object
print AccountAddress.to_json()

# convert the object into a dict
account_address_dict = account_address_instance.to_dict()
# create an instance of AccountAddress from a dict
account_address_form_dict = account_address.from_dict(account_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


