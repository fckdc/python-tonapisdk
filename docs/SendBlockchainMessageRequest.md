# SendBlockchainMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boc** | **str** |  | [optional] 
**batch** | **List[str]** |  | [optional] 

## Example

```python
from fdtapi.models.send_blockchain_message_request import SendBlockchainMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendBlockchainMessageRequest from a JSON string
send_blockchain_message_request_instance = SendBlockchainMessageRequest.from_json(json)
# print the JSON string representation of the object
print SendBlockchainMessageRequest.to_json()

# convert the object into a dict
send_blockchain_message_request_dict = send_blockchain_message_request_instance.to_dict()
# create an instance of SendBlockchainMessageRequest from a dict
send_blockchain_message_request_form_dict = send_blockchain_message_request.from_dict(send_blockchain_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


