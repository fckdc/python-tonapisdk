# DomainBids


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainBid]**](DomainBid.md) |  | 

## Example

```python
from fdtapi.models.domain_bids import DomainBids

# TODO update the JSON string below
json = "{}"
# create an instance of DomainBids from a JSON string
domain_bids_instance = DomainBids.from_json(json)
# print the JSON string representation of the object
print DomainBids.to_json()

# convert the object into a dict
domain_bids_dict = domain_bids_instance.to_dict()
# create an instance of DomainBids from a dict
domain_bids_form_dict = domain_bids.from_dict(domain_bids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


