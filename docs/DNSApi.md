# fdtapi.DNSApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_resolve**](DNSApi.md#dns_resolve) | **GET** /v2/dns/{domain_name}/resolve | 
[**get_all_auctions**](DNSApi.md#get_all_auctions) | **GET** /v2/dns/auctions | 
[**get_dns_info**](DNSApi.md#get_dns_info) | **GET** /v2/dns/{domain_name} | 
[**get_domain_bids**](DNSApi.md#get_domain_bids) | **GET** /v2/dns/{domain_name}/bids | 


# **dns_resolve**
> DnsRecord dns_resolve(domain_name)



DNS resolve for domain name

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.dns_record import DnsRecord
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
    api_instance = fdtapi.DNSApi(api_client)
    domain_name = 'wallet.ton' # str | domain name with .ton or .t.me

    try:
        api_response = api_instance.dns_resolve(domain_name)
        print("The response of DNSApi->dns_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_resolve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain name with .ton or .t.me | 

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | dns record |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_auctions**
> Auctions get_all_auctions(tld=tld)



Get all auctions

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.auctions import Auctions
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
    api_instance = fdtapi.DNSApi(api_client)
    tld = 'ton' # str | domain filter for current auctions \"ton\" or \"t.me\" (optional)

    try:
        api_response = api_instance.get_all_auctions(tld=tld)
        print("The response of DNSApi->get_all_auctions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->get_all_auctions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| domain filter for current auctions \&quot;ton\&quot; or \&quot;t.me\&quot; | [optional] 

### Return type

[**Auctions**](Auctions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | auctions |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_info**
> DomainInfo get_dns_info(domain_name)



Get full information about domain name

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.domain_info import DomainInfo
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
    api_instance = fdtapi.DNSApi(api_client)
    domain_name = 'wallet.ton' # str | domain name with .ton or .t.me

    try:
        api_response = api_instance.get_dns_info(domain_name)
        print("The response of DNSApi->get_dns_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->get_dns_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain name with .ton or .t.me | 

### Return type

[**DomainInfo**](DomainInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | domain info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_bids**
> DomainBids get_domain_bids(domain_name)



Get domain bids

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.domain_bids import DomainBids
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
    api_instance = fdtapi.DNSApi(api_client)
    domain_name = 'wallet.ton' # str | domain name with .ton or .t.me

    try:
        api_response = api_instance.get_domain_bids(domain_name)
        print("The response of DNSApi->get_domain_bids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->get_domain_bids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| domain name with .ton or .t.me | 

### Return type

[**DomainBids**](DomainBids.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | domain bids |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

