# Risk

Risk specifies assets that could be lost if a message would be sent to a malicious smart contract. It makes sense to understand the risk BEFORE sending a message to the blockchain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_all_remaining_balance** | **bool** | transfer all the remaining balance of the wallet. | 
**ton** | **int** |  | 
**jettons** | [**List[JettonQuantity]**](JettonQuantity.md) |  | 
**nfts** | [**List[NftItem]**](NftItem.md) |  | 

## Example

```python
from fdtapi.models.risk import Risk

# TODO update the JSON string below
json = "{}"
# create an instance of Risk from a JSON string
risk_instance = Risk.from_json(json)
# print the JSON string representation of the object
print Risk.to_json()

# convert the object into a dict
risk_dict = risk_instance.to_dict()
# create an instance of Risk from a dict
risk_form_dict = risk.from_dict(risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


