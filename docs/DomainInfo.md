# DomainInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**expiring_at** | **int** | date of expiring. optional. not all domain in ton has expiration date | [optional] 
**item** | [**NftItem**](NftItem.md) |  | [optional] 

## Example

```python
from fdtapi.models.domain_info import DomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainInfo from a JSON string
domain_info_instance = DomainInfo.from_json(json)
# print the JSON string representation of the object
print DomainInfo.to_json()

# convert the object into a dict
domain_info_dict = domain_info_instance.to_dict()
# create an instance of DomainInfo from a dict
domain_info_form_dict = domain_info.from_dict(domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


