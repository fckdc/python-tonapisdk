# AccountInfoByStateInit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | 
**address** | **str** |  | 

## Example

```python
from fdtapi.models.account_info_by_state_init import AccountInfoByStateInit

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoByStateInit from a JSON string
account_info_by_state_init_instance = AccountInfoByStateInit.from_json(json)
# print the JSON string representation of the object
print AccountInfoByStateInit.to_json()

# convert the object into a dict
account_info_by_state_init_dict = account_info_by_state_init_instance.to_dict()
# create an instance of AccountInfoByStateInit from a dict
account_info_by_state_init_form_dict = account_info_by_state_init.from_dict(account_info_by_state_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


