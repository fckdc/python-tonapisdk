# fdtapi.StorageApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_providers**](StorageApi.md#get_storage_providers) | **GET** /v2/storage/providers | 


# **get_storage_providers**
> GetStorageProviders200Response get_storage_providers()



Get TON storage providers deployed to the blockchain.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_storage_providers200_response import GetStorageProviders200Response
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
    api_instance = fdtapi.StorageApi(api_client)

    try:
        api_response = api_instance.get_storage_providers()
        print("The response of StorageApi->get_storage_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_storage_providers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStorageProviders200Response**](GetStorageProviders200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of storage providers |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

