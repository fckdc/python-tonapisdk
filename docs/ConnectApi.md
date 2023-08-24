# fdtapi.ConnectApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_info_by_state_init**](ConnectApi.md#get_account_info_by_state_init) | **POST** /v2/tonconnect/stateinit | 
[**get_ton_connect_payload**](ConnectApi.md#get_ton_connect_payload) | **GET** /v2/tonconnect/payload | 


# **get_account_info_by_state_init**
> AccountInfoByStateInit get_account_info_by_state_init(get_account_info_by_state_init_request)



Get account info by state init

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_info_by_state_init import AccountInfoByStateInit
from fdtapi.models.get_account_info_by_state_init_request import GetAccountInfoByStateInitRequest
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
    api_instance = fdtapi.ConnectApi(api_client)
    get_account_info_by_state_init_request = fdtapi.GetAccountInfoByStateInitRequest() # GetAccountInfoByStateInitRequest | Data that is expected

    try:
        api_response = api_instance.get_account_info_by_state_init(get_account_info_by_state_init_request)
        print("The response of ConnectApi->get_account_info_by_state_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectApi->get_account_info_by_state_init: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_account_info_by_state_init_request** | [**GetAccountInfoByStateInitRequest**](GetAccountInfoByStateInitRequest.md)| Data that is expected | 

### Return type

[**AccountInfoByStateInit**](AccountInfoByStateInit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ton_connect_payload**
> GetTonConnectPayload200Response get_ton_connect_payload()



Get a payload for further token receipt

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_ton_connect_payload200_response import GetTonConnectPayload200Response
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
    api_instance = fdtapi.ConnectApi(api_client)

    try:
        api_response = api_instance.get_ton_connect_payload()
        print("The response of ConnectApi->get_ton_connect_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectApi->get_ton_connect_payload: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTonConnectPayload200Response**](GetTonConnectPayload200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | payload |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

