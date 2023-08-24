# SendRawMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 

## Example

```python
from fdtapi.models.send_raw_message_request import SendRawMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendRawMessageRequest from a JSON string
send_raw_message_request_instance = SendRawMessageRequest.from_json(json)
# print the JSON string representation of the object
print SendRawMessageRequest.to_json()

# convert the object into a dict
send_raw_message_request_dict = send_raw_message_request_instance.to_dict()
# create an instance of SendRawMessageRequest from a dict
send_raw_message_request_form_dict = send_raw_message_request.from_dict(send_raw_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


