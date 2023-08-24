# GetStorageProviders200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[StorageProvider]**](StorageProvider.md) |  | 

## Example

```python
from fdtapi.models.get_storage_providers200_response import GetStorageProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStorageProviders200Response from a JSON string
get_storage_providers200_response_instance = GetStorageProviders200Response.from_json(json)
# print the JSON string representation of the object
print GetStorageProviders200Response.to_json()

# convert the object into a dict
get_storage_providers200_response_dict = get_storage_providers200_response_instance.to_dict()
# create an instance of GetStorageProviders200Response from a dict
get_storage_providers200_response_form_dict = get_storage_providers200_response.from_dict(get_storage_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


