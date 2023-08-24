# DomainBid


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [default to False]
**value** | **int** |  | 
**tx_time** | **int** |  | 
**tx_hash** | **str** |  | 
**bidder** | [**AccountAddress**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.domain_bid import DomainBid

# TODO update the JSON string below
json = "{}"
# create an instance of DomainBid from a JSON string
domain_bid_instance = DomainBid.from_json(json)
# print the JSON string representation of the object
print DomainBid.to_json()

# convert the object into a dict
domain_bid_dict = domain_bid_instance.to_dict()
# create an instance of DomainBid from a dict
domain_bid_form_dict = domain_bid.from_dict(domain_bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


