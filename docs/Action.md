# Action


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | **str** |  | 
**ton_transfer** | [**TonTransferAction**](TonTransferAction.md) |  | [optional] 
**contract_deploy** | [**ContractDeployAction**](ContractDeployAction.md) |  | [optional] 
**jetton_transfer** | [**JettonTransferAction**](JettonTransferAction.md) |  | [optional] 
**nft_item_transfer** | [**NftItemTransferAction**](NftItemTransferAction.md) |  | [optional] 
**subscribe** | [**SubscriptionAction**](SubscriptionAction.md) |  | [optional] 
**un_subscribe** | [**UnSubscriptionAction**](UnSubscriptionAction.md) |  | [optional] 
**auction_bid** | [**AuctionBidAction**](AuctionBidAction.md) |  | [optional] 
**nft_purchase** | [**NftPurchaseAction**](NftPurchaseAction.md) |  | [optional] 
**deposit_stake** | [**DepositStakeAction**](DepositStakeAction.md) |  | [optional] 
**recover_stake** | [**RecoverStakeAction**](RecoverStakeAction.md) |  | [optional] 
**jetton_swap** | [**JettonSwapAction**](JettonSwapAction.md) |  | [optional] 
**smart_contract_exec** | [**SmartContractAction**](SmartContractAction.md) |  | [optional] 
**simple_preview** | [**ActionSimplePreview**](ActionSimplePreview.md) |  | 

## Example

```python
from fdtapi.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print Action.to_json()

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_form_dict = action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


