# Auction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**owner** | **str** |  | 
**price** | **int** |  | 
**bids** | **int** |  | 
**var_date** | **int** |  | 

## Example

```python
from fdtapi.models.auction import Auction

# TODO update the JSON string below
json = "{}"
# create an instance of Auction from a JSON string
auction_instance = Auction.from_json(json)
# print the JSON string representation of the object
print Auction.to_json()

# convert the object into a dict
auction_dict = auction_instance.to_dict()
# create an instance of Auction from a dict
auction_form_dict = auction.from_dict(auction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


