# DnsExpiring


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DnsExpiringItemsInner]**](DnsExpiringItemsInner.md) |  | 

## Example

```python
from fdtapi.models.dns_expiring import DnsExpiring

# TODO update the JSON string below
json = "{}"
# create an instance of DnsExpiring from a JSON string
dns_expiring_instance = DnsExpiring.from_json(json)
# print the JSON string representation of the object
print DnsExpiring.to_json()

# convert the object into a dict
dns_expiring_dict = dns_expiring_instance.to_dict()
# create an instance of DnsExpiring from a dict
dns_expiring_form_dict = dns_expiring.from_dict(dns_expiring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


