# AccountEvent

An event is built on top of a trace which is a series of transactions caused by one inbound message. TonAPI looks for known patterns inside the trace and splits the trace into actions, where a single action represents a meaningful high-level operation like a Jetton Transfer or an NFT Purchase. Actions are expected to be shown to users. It is advised not to build any logic on top of actions because actions can be changed at any time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**account** | [**AccountAddress**](AccountAddress.md) |  | 
**timestamp** | **int** |  | 
**actions** | [**List[Action]**](Action.md) |  | 
**is_scam** | **bool** | scam | 
**lt** | **int** |  | 
**in_progress** | **bool** | Event is not finished yet. Transactions still happening | 
**extra** | **int** | TODO | 

## Example

```python
from fdtapi.models.account_event import AccountEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountEvent from a JSON string
account_event_instance = AccountEvent.from_json(json)
# print the JSON string representation of the object
print AccountEvent.to_json()

# convert the object into a dict
account_event_dict = account_event_instance.to_dict()
# create an instance of AccountEvent from a dict
account_event_form_dict = account_event.from_dict(account_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


