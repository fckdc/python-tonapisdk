# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | 
**lt** | **int** |  | 
**account** | [**AccountAddress**](AccountAddress.md) |  | 
**success** | **bool** |  | 
**utime** | **int** |  | 
**orig_status** | [**AccountStatus**](AccountStatus.md) |  | 
**end_status** | [**AccountStatus**](AccountStatus.md) |  | 
**total_fees** | **int** |  | 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | 
**state_update_old** | **str** |  | 
**state_update_new** | **str** |  | 
**in_msg** | [**Message**](Message.md) |  | [optional] 
**out_msgs** | [**List[Message]**](Message.md) |  | 
**block** | **str** |  | 
**prev_trans_hash** | **str** |  | [optional] 
**prev_trans_lt** | **int** |  | [optional] 
**compute_phase** | [**ComputePhase**](ComputePhase.md) |  | [optional] 
**storage_phase** | [**StoragePhase**](StoragePhase.md) |  | [optional] 
**credit_phase** | [**CreditPhase**](CreditPhase.md) |  | [optional] 
**action_phase** | [**ActionPhase**](ActionPhase.md) |  | [optional] 
**bounce_phase** | [**BouncePhaseType**](BouncePhaseType.md) |  | [optional] 
**aborted** | **bool** |  | 
**destroyed** | **bool** |  | 

## Example

```python
from fdtapi.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print Transaction.to_json()

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


