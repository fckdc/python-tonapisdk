# PoolInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | 
**total_amount** | **int** |  | 
**implementation** | **str** |  | 
**apy** | **float** | APY in percent | 
**min_stake** | **int** |  | 
**cycle_start** | **int** | current nomination cycle beginning timestamp | 
**cycle_end** | **int** | current nomination cycle ending timestamp | 
**verified** | **bool** | this pool has verified source code or managed by trusted company | 
**current_nominators** | **int** | current number of nominators | 
**max_nominators** | **int** | maximum number of nominators | 
**liquid_jetton_master** | **str** | for liquid staking master account of jetton | [optional] 
**nominators_stake** | **int** | total stake of all nominators | 
**validator_stake** | **int** | stake of validator | 

## Example

```python
from fdtapi.models.pool_info import PoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PoolInfo from a JSON string
pool_info_instance = PoolInfo.from_json(json)
# print the JSON string representation of the object
print PoolInfo.to_json()

# convert the object into a dict
pool_info_dict = pool_info_instance.to_dict()
# create an instance of PoolInfo from a dict
pool_info_form_dict = pool_info.from_dict(pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


