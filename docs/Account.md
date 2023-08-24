# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**balance** | **int** |  | 
**last_activity** | **int** | unix timestamp | 
**status** | **str** |  | 
**interfaces** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**is_scam** | **bool** |  | [optional] 
**icon** | **str** |  | [optional] 
**memo_required** | **bool** |  | [optional] 
**get_methods** | **List[str]** |  | 

## Example

```python
from fdtapi.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


