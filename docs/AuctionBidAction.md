# AuctionBidAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auction_type** | **str** |  | 
**amount** | [**Price**](Price.md) |  | 
**nft** | [**NftItem**](NftItem.md) |  | [optional] 
**bidder** | [**AccountAddress**](AccountAddress.md) |  | 
**auction** | [**AccountAddress**](AccountAddress.md) |  | 

## Example

```python
from fdtapi.models.auction_bid_action import AuctionBidAction

# TODO update the JSON string below
json = "{}"
# create an instance of AuctionBidAction from a JSON string
auction_bid_action_instance = AuctionBidAction.from_json(json)
# print the JSON string representation of the object
print AuctionBidAction.to_json()

# convert the object into a dict
auction_bid_action_dict = auction_bid_action_instance.to_dict()
# create an instance of AuctionBidAction from a dict
auction_bid_action_form_dict = auction_bid_action.from_dict(auction_bid_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


