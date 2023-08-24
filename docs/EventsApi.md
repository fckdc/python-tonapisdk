# fdtapi.EventsApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /v2/events/{event_id} | 


# **get_event**
> Event get_event(event_id, accept_language=accept_language)



Get an event either by event ID or a hash of any transaction in a trace. An event is built on top of a trace which is a series of transactions caused by one inbound message. TonAPI looks for known patterns inside the trace and splits the trace into actions, where a single action represents a meaningful high-level operation like a Jetton Transfer or an NFT Purchase. Actions are expected to be shown to users. It is advised not to build any logic on top of actions because actions can be changed at any time.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.event import Event
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
    api_instance = fdtapi.EventsApi(api_client)
    event_id = '97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | event ID or transaction hash in hex (without 0x) or base64url format
    accept_language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.get_event(event_id, accept_language=accept_language)
        print("The response of EventsApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| event ID or transaction hash in hex (without 0x) or base64url format | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | event |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

