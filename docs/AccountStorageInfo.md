# AccountStorageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_cells** | **int** |  | 
**used_bits** | **int** |  | 
**used_public_cells** | **int** |  | 
**last_paid** | **int** |  | 
**due_payment** | **int** |  | 

## Example

```python
from fdtapi.models.account_storage_info import AccountStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStorageInfo from a JSON string
account_storage_info_instance = AccountStorageInfo.from_json(json)
# print the JSON string representation of the object
print AccountStorageInfo.to_json()

# convert the object into a dict
account_storage_info_dict = account_storage_info_instance.to_dict()
# create an instance of AccountStorageInfo from a dict
account_storage_info_form_dict = account_storage_info.from_dict(account_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


