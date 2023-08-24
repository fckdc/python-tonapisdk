# fdtapi.RatesApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chart_rates**](RatesApi.md#get_chart_rates) | **GET** /v2/rates/chart | 
[**get_rates**](RatesApi.md#get_rates) | **GET** /v2/rates | 


# **get_chart_rates**
> GetChartRates200Response get_chart_rates(token, currency=currency, start_date=start_date, end_date=end_date)



Get chart by token

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_chart_rates200_response import GetChartRates200Response
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
    api_instance = fdtapi.RatesApi(api_client)
    token = 'token_example' # str | accept jetton master address
    currency = 'usd' # str |  (optional)
    start_date = 1668436763 # int |  (optional)
    end_date = 1668436763 # int |  (optional)

    try:
        api_response = api_instance.get_chart_rates(token, currency=currency, start_date=start_date, end_date=end_date)
        print("The response of RatesApi->get_chart_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatesApi->get_chart_rates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| accept jetton master address | 
 **currency** | **str**|  | [optional] 
 **start_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 

### Return type

[**GetChartRates200Response**](GetChartRates200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | token chart |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rates**
> GetRates200Response get_rates(tokens, currencies)



Get the token price to the currency

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_rates200_response import GetRates200Response
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
    api_instance = fdtapi.RatesApi(api_client)
    tokens = 'ton' # str | accept ton and jetton master addresses, separated by commas
    currencies = 'ton,usd,rub' # str | accept ton and all possible fiat currencies, separated by commas

    try:
        api_response = api_instance.get_rates(tokens, currencies)
        print("The response of RatesApi->get_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatesApi->get_rates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokens** | **str**| accept ton and jetton master addresses, separated by commas | 
 **currencies** | **str**| accept ton and all possible fiat currencies, separated by commas | 

### Return type

[**GetRates200Response**](GetRates200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tokens rates |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

