# ContractDeployAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**interfaces** | **List[str]** |  | 

## Example

```python
from fdtapi.models.contract_deploy_action import ContractDeployAction

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDeployAction from a JSON string
contract_deploy_action_instance = ContractDeployAction.from_json(json)
# print the JSON string representation of the object
print ContractDeployAction.to_json()

# convert the object into a dict
contract_deploy_action_dict = contract_deploy_action_instance.to_dict()
# create an instance of ContractDeployAction from a dict
contract_deploy_action_form_dict = contract_deploy_action.from_dict(contract_deploy_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


