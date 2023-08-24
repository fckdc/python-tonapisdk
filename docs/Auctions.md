# Auctions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Auction]**](Auction.md) |  | 
**total** | **int** |  | 

## Example

```python
from fdtapi.models.auctions import Auctions

# TODO update the JSON string below
json = "{}"
# create an instance of Auctions from a JSON string
auctions_instance = Auctions.from_json(json)
# print the JSON string representation of the object
print Auctions.to_json()

# convert the object into a dict
auctions_dict = auctions_instance.to_dict()
# create an instance of Auctions from a dict
auctions_form_dict = auctions.from_dict(auctions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


