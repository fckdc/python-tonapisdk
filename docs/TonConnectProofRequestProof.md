# TonConnectProofRequestProof


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**domain** | [**TonConnectProofRequestProofDomain**](TonConnectProofRequestProofDomain.md) |  | 
**signature** | **str** |  | 
**payload** | **str** |  | 
**state_init** | **str** |  | [optional] 

## Example

```python
from fdtapi.models.ton_connect_proof_request_proof import TonConnectProofRequestProof

# TODO update the JSON string below
json = "{}"
# create an instance of TonConnectProofRequestProof from a JSON string
ton_connect_proof_request_proof_instance = TonConnectProofRequestProof.from_json(json)
# print the JSON string representation of the object
print TonConnectProofRequestProof.to_json()

# convert the object into a dict
ton_connect_proof_request_proof_dict = ton_connect_proof_request_proof_instance.to_dict()
# create an instance of TonConnectProofRequestProof from a dict
ton_connect_proof_request_proof_form_dict = ton_connect_proof_request_proof.from_dict(ton_connect_proof_request_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


