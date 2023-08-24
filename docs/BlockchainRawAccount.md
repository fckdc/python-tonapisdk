# BlockchainRawAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**balance** | **int** |  | 
**extra_balance** | **Dict[str, str]** |  | [optional] 
**code** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**last_transaction_lt** | **int** |  | 
**status** | **str** |  | 
**storage** | [**AccountStorageInfo**](AccountStorageInfo.md) |  | 

## Example

```python
from fdtapi.models.blockchain_raw_account import BlockchainRawAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainRawAccount from a JSON string
blockchain_raw_account_instance = BlockchainRawAccount.from_json(json)
# print the JSON string representation of the object
print BlockchainRawAccount.to_json()

# convert the object into a dict
blockchain_raw_account_dict = blockchain_raw_account_instance.to_dict()
# create an instance of BlockchainRawAccount from a dict
blockchain_raw_account_form_dict = blockchain_raw_account.from_dict(blockchain_raw_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


