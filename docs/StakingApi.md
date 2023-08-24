# fdtapi.StakingApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_nominators_pools**](StakingApi.md#get_account_nominators_pools) | **GET** /v2/staking/nominator/{account_id}/pools | 
[**get_staking_pool_history**](StakingApi.md#get_staking_pool_history) | **GET** /v2/staking/pool/{account_id}/history | 
[**get_staking_pool_info**](StakingApi.md#get_staking_pool_info) | **GET** /v2/staking/pool/{account_id} | 
[**get_staking_pools**](StakingApi.md#get_staking_pools) | **GET** /v2/staking/pools | 


# **get_account_nominators_pools**
> AccountStaking get_account_nominators_pools(account_id)



All pools where account participates

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_staking import AccountStaking
from fdtapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tonapi.io
# See configuration.py for a list of all supported configuration parameters.
configuration = fdtapi.Configuration(
    host = "https://tonapi.io"
)


# Enter a context with an instance of the API client
with fdtapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fdtapi.StakingApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_account_nominators_pools(account_id)
        print("The response of StakingApi->get_account_nominators_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_account_nominators_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**AccountStaking**](AccountStaking.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s pools |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_pool_history**
> GetStakingPoolHistory200Response get_staking_pool_history(account_id)



Pool history

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_staking_pool_history200_response import GetStakingPoolHistory200Response
from fdtapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tonapi.io
# See configuration.py for a list of all supported configuration parameters.
configuration = fdtapi.Configuration(
    host = "https://tonapi.io"
)


# Enter a context with an instance of the API client
with fdtapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fdtapi.StakingApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_staking_pool_history(account_id)
        print("The response of StakingApi->get_staking_pool_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_staking_pool_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**GetStakingPoolHistory200Response**](GetStakingPoolHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pool history |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_pool_info**
> GetStakingPoolInfo200Response get_staking_pool_info(account_id, accept_language=accept_language)



Stacking pool info

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_staking_pool_info200_response import GetStakingPoolInfo200Response
from fdtapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tonapi.io
# See configuration.py for a list of all supported configuration parameters.
configuration = fdtapi.Configuration(
    host = "https://tonapi.io"
)


# Enter a context with an instance of the API client
with fdtapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fdtapi.StakingApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    accept_language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.get_staking_pool_info(account_id, accept_language=accept_language)
        print("The response of StakingApi->get_staking_pool_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_staking_pool_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**GetStakingPoolInfo200Response**](GetStakingPoolInfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | stacking pool info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_pools**
> GetStakingPools200Response get_staking_pools(available_for=available_for, include_unverified=include_unverified, accept_language=accept_language)



All pools available in network

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_staking_pools200_response import GetStakingPools200Response
from fdtapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tonapi.io
# See configuration.py for a list of all supported configuration parameters.
configuration = fdtapi.Configuration(
    host = "https://tonapi.io"
)


# Enter a context with an instance of the API client
with fdtapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fdtapi.StakingApi(api_client)
    available_for = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID (optional)
    include_unverified = false # bool | return also pools not from white list - just compatible by interfaces (maybe dangerous!) (optional)
    accept_language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.get_staking_pools(available_for=available_for, include_unverified=include_unverified, accept_language=accept_language)
        print("The response of StakingApi->get_staking_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_staking_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_for** | **str**| account ID | [optional] 
 **include_unverified** | **bool**| return also pools not from white list - just compatible by interfaces (maybe dangerous!) | [optional] 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**GetStakingPools200Response**](GetStakingPools200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of pools |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

