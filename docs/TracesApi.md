# fdtapi.TracesApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trace**](TracesApi.md#get_trace) | **GET** /v2/traces/{trace_id} | 


# **get_trace**
> Trace get_trace(trace_id)



Get the trace by trace ID or hash of any transaction in trace

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.trace import Trace
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
    api_instance = fdtapi.TracesApi(api_client)
    trace_id = '97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | trace ID or transaction hash in hex (without 0x) or base64url format

    try:
        api_response = api_instance.get_trace(trace_id)
        print("The response of TracesApi->get_trace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracesApi->get_trace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| trace ID or transaction hash in hex (without 0x) or base64url format | 

### Return type

[**Trace**](Trace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | trace |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

