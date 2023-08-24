# Message


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_lt** | **int** |  | 
**ihr_disabled** | **bool** |  | 
**bounce** | **bool** |  | 
**bounced** | **bool** |  | 
**value** | **int** |  | 
**fwd_fee** | **int** |  | 
**ihr_fee** | **int** |  | 
**destination** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**source** | [**AccountAddress**](AccountAddress.md) |  | [optional] 
**import_fee** | **int** |  | 
**created_at** | **int** |  | 
**op_code** | **str** |  | [optional] 
**init** | [**StateInit**](StateInit.md) |  | [optional] 
**raw_body** | **str** | hex-encoded BoC with raw message body | [optional] 
**decoded_op_name** | **str** |  | [optional] 
**decoded_body** | **object** |  | [optional] 

## Example

```python
from fdtapi.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print Message.to_json()

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_form_dict = message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


