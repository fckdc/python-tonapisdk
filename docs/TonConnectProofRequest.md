# TonConnectProofRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**proof** | [**TonConnectProofRequestProof**](TonConnectProofRequestProof.md) |  | 

## Example

```python
from fdtapi.models.ton_connect_proof_request import TonConnectProofRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TonConnectProofRequest from a JSON string
ton_connect_proof_request_instance = TonConnectProofRequest.from_json(json)
# print the JSON string representation of the object
print TonConnectProofRequest.to_json()

# convert the object into a dict
ton_connect_proof_request_dict = ton_connect_proof_request_instance.to_dict()
# create an instance of TonConnectProofRequest from a dict
ton_connect_proof_request_form_dict = ton_connect_proof_request.from_dict(ton_connect_proof_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


