# DnsExpiringItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiring_at** | **int** |  | 
**name** | **str** |  | 
**dns_item** | [**NftItem**](NftItem.md) |  | [optional] 

## Example

```python
from fdtapi.models.dns_expiring_items_inner import DnsExpiringItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsExpiringItemsInner from a JSON string
dns_expiring_items_inner_instance = DnsExpiringItemsInner.from_json(json)
# print the JSON string representation of the object
print DnsExpiringItemsInner.to_json()

# convert the object into a dict
dns_expiring_items_inner_dict = dns_expiring_items_inner_instance.to_dict()
# create an instance of DnsExpiringItemsInner from a dict
dns_expiring_items_inner_form_dict = dns_expiring_items_inner.from_dict(dns_expiring_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


