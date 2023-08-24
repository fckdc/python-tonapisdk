# WalletDNS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**is_wallet** | **bool** |  | 
**has_method_pubkey** | **bool** |  | 
**has_method_seqno** | **bool** |  | 
**names** | **List[str]** |  | 

## Example

```python
from fdtapi.models.wallet_dns import WalletDNS

# TODO update the JSON string below
json = "{}"
# create an instance of WalletDNS from a JSON string
wallet_dns_instance = WalletDNS.from_json(json)
# print the JSON string representation of the object
print WalletDNS.to_json()

# convert the object into a dict
wallet_dns_dict = wallet_dns_instance.to_dict()
# create an instance of WalletDNS from a dict
wallet_dns_form_dict = wallet_dns.from_dict(wallet_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


