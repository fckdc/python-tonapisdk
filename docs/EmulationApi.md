# fdtapi.EmulationApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emulate_message_to_account_event**](EmulationApi.md#emulate_message_to_account_event) | **POST** /v2/accounts/{account_id}/events/emulate | 
[**emulate_message_to_event**](EmulationApi.md#emulate_message_to_event) | **POST** /v2/events/emulate | 
[**emulate_message_to_trace**](EmulationApi.md#emulate_message_to_trace) | **POST** /v2/traces/emulate | 
[**emulate_message_to_wallet**](EmulationApi.md#emulate_message_to_wallet) | **POST** /v2/wallet/emulate | 


# **emulate_message_to_account_event**
> AccountEvent emulate_message_to_account_event(account_id, emulate_message_to_event_request, accept_language=accept_language)



Emulate sending message to blockchain

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_event import AccountEvent
from fdtapi.models.emulate_message_to_event_request import EmulateMessageToEventRequest
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
    api_instance = fdtapi.EmulationApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    emulate_message_to_event_request = fdtapi.EmulateMessageToEventRequest() # EmulateMessageToEventRequest | bag-of-cells serialized to base64
    accept_language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.emulate_message_to_account_event(account_id, emulate_message_to_event_request, accept_language=accept_language)
        print("The response of EmulationApi->emulate_message_to_account_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->emulate_message_to_account_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **emulate_message_to_event_request** | [**EmulateMessageToEventRequest**](EmulateMessageToEventRequest.md)| bag-of-cells serialized to base64 | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**AccountEvent**](AccountEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | emulated message to account |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulate_message_to_event**
> Event emulate_message_to_event(emulate_message_to_event_request, accept_language=accept_language)



Emulate sending message to blockchain

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.emulate_message_to_event_request import EmulateMessageToEventRequest
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
    api_instance = fdtapi.EmulationApi(api_client)
    emulate_message_to_event_request = fdtapi.EmulateMessageToEventRequest() # EmulateMessageToEventRequest | bag-of-cells serialized to base64
    accept_language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.emulate_message_to_event(emulate_message_to_event_request, accept_language=accept_language)
        print("The response of EmulationApi->emulate_message_to_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->emulate_message_to_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emulate_message_to_event_request** | [**EmulateMessageToEventRequest**](EmulateMessageToEventRequest.md)| bag-of-cells serialized to base64 | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | emulated event |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulate_message_to_trace**
> Trace emulate_message_to_trace(emulate_message_to_event_request)



Emulate sending message to blockchain

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.emulate_message_to_event_request import EmulateMessageToEventRequest
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
    api_instance = fdtapi.EmulationApi(api_client)
    emulate_message_to_event_request = fdtapi.EmulateMessageToEventRequest() # EmulateMessageToEventRequest | bag-of-cells serialized to base64

    try:
        api_response = api_instance.emulate_message_to_trace(emulate_message_to_event_request)
        print("The response of EmulationApi->emulate_message_to_trace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->emulate_message_to_trace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emulate_message_to_event_request** | [**EmulateMessageToEventRequest**](EmulateMessageToEventRequest.md)| bag-of-cells serialized to base64 | 

### Return type

[**Trace**](Trace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | emulated trace |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulate_message_to_wallet**
> MessageConsequences emulate_message_to_wallet(emulate_message_to_event_request, accept_language=accept_language)



Emulate sending message to blockchain

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.emulate_message_to_event_request import EmulateMessageToEventRequest
from fdtapi.models.message_consequences import MessageConsequences
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
    api_instance = fdtapi.EmulationApi(api_client)
    emulate_message_to_event_request = fdtapi.EmulateMessageToEventRequest() # EmulateMessageToEventRequest | bag-of-cells serialized to base64
    accept_language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.emulate_message_to_wallet(emulate_message_to_event_request, accept_language=accept_language)
        print("The response of EmulationApi->emulate_message_to_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->emulate_message_to_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emulate_message_to_event_request** | [**EmulateMessageToEventRequest**](EmulateMessageToEventRequest.md)| bag-of-cells serialized to base64 | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MessageConsequences**](MessageConsequences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | emulated message |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

