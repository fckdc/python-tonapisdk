# StorageProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**accept_new_contracts** | **bool** |  | 
**rate_per_mb_day** | **int** |  | 
**max_span** | **int** |  | 
**minimal_file_size** | **int** |  | 
**maximal_file_size** | **int** |  | 

## Example

```python
from fdtapi.models.storage_provider import StorageProvider

# TODO update the JSON string below
json = "{}"
# create an instance of StorageProvider from a JSON string
storage_provider_instance = StorageProvider.from_json(json)
# print the JSON string representation of the object
print StorageProvider.to_json()

# convert the object into a dict
storage_provider_dict = storage_provider_instance.to_dict()
# create an instance of StorageProvider from a dict
storage_provider_form_dict = storage_provider.from_dict(storage_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


