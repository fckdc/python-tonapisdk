# BlockchainConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** | config boc in base64 format | 
**var_0** | **str** | config address | 
**var_1** | **str** | elector address | 
**var_2** | **str** | minter address | 
**var_4** | **str** | dns root address | 
**var_32** | [**ValidatorsSet**](ValidatorsSet.md) |  | [optional] 
**var_33** | [**ValidatorsSet**](ValidatorsSet.md) |  | [optional] 
**var_34** | [**ValidatorsSet**](ValidatorsSet.md) |  | [optional] 
**var_35** | [**ValidatorsSet**](ValidatorsSet.md) |  | [optional] 
**var_36** | [**ValidatorsSet**](ValidatorsSet.md) |  | [optional] 
**var_37** | [**ValidatorsSet**](ValidatorsSet.md) |  | [optional] 

## Example

```python
from fdtapi.models.blockchain_config import BlockchainConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainConfig from a JSON string
blockchain_config_instance = BlockchainConfig.from_json(json)
# print the JSON string representation of the object
print BlockchainConfig.to_json()

# convert the object into a dict
blockchain_config_dict = blockchain_config_instance.to_dict()
# create an instance of BlockchainConfig from a dict
blockchain_config_form_dict = blockchain_config.from_dict(blockchain_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


