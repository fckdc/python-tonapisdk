# fdtapi.JettonsApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jetton_info**](JettonsApi.md#get_jetton_info) | **GET** /v2/jettons/{account_id} | 
[**get_jettons**](JettonsApi.md#get_jettons) | **GET** /v2/jettons | 


# **get_jetton_info**
> JettonInfo get_jetton_info(account_id)



Get jetton metadata by jetton master address

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.jetton_info import JettonInfo
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
    api_instance = fdtapi.JettonsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_jetton_info(account_id)
        print("The response of JettonsApi->get_jetton_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JettonsApi->get_jetton_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**JettonInfo**](JettonInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | jetton info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jettons**
> Jettons get_jettons(limit=limit, offset=offset)



Get a list of all indexed jetton masters in the blockchain.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.jettons import Jettons
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
    api_instance = fdtapi.JettonsApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.get_jettons(limit=limit, offset=offset)
        print("The response of JettonsApi->get_jettons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JettonsApi->get_jettons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**Jettons**](Jettons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of jettons |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

