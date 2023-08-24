# fdtapi.AccountsApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_dns_back_resolve**](AccountsApi.md#account_dns_back_resolve) | **GET** /v2/accounts/{account_id}/dns/backresolve | 
[**get_account**](AccountsApi.md#get_account) | **GET** /v2/accounts/{account_id} | 
[**get_account_diff**](AccountsApi.md#get_account_diff) | **GET** /v2/accounts/{account_id}/diff | 
[**get_account_dns_expiring**](AccountsApi.md#get_account_dns_expiring) | **GET** /v2/accounts/{account_id}/dns/expiring | 
[**get_account_event**](AccountsApi.md#get_account_event) | **GET** /v2/accounts/{account_id}/events/{event_id} | 
[**get_account_events**](AccountsApi.md#get_account_events) | **GET** /v2/accounts/{account_id}/events | 
[**get_account_jetton_history_by_id**](AccountsApi.md#get_account_jetton_history_by_id) | **GET** /v2/accounts/{account_id}/jettons/{jetton_id}/history | 
[**get_account_jettons_balances**](AccountsApi.md#get_account_jettons_balances) | **GET** /v2/accounts/{account_id}/jettons | 
[**get_account_jettons_history**](AccountsApi.md#get_account_jettons_history) | **GET** /v2/accounts/{account_id}/jettons/history | 
[**get_account_nft_items**](AccountsApi.md#get_account_nft_items) | **GET** /v2/accounts/{account_id}/nfts | 
[**get_account_public_key**](AccountsApi.md#get_account_public_key) | **GET** /v2/accounts/{account_id}/publickey | 
[**get_account_subscriptions**](AccountsApi.md#get_account_subscriptions) | **GET** /v2/accounts/{account_id}/subscriptions | 
[**get_account_traces**](AccountsApi.md#get_account_traces) | **GET** /v2/accounts/{account_id}/traces | 
[**get_accounts**](AccountsApi.md#get_accounts) | **POST** /v2/accounts/_bulk | 
[**reindex_account**](AccountsApi.md#reindex_account) | **POST** /v2/accounts/{account_id}/reindex | 
[**search_accounts**](AccountsApi.md#search_accounts) | **GET** /v2/accounts/search | 


# **account_dns_back_resolve**
> DomainNames account_dns_back_resolve(account_id)



Get account's domains

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.domain_names import DomainNames
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.account_dns_back_resolve(account_id)
        print("The response of AccountsApi->account_dns_back_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->account_dns_back_resolve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**DomainNames**](DomainNames.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s domains |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(account_id)



Get human-friendly information about an account without low-level details.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account import Account
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_account(account_id)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_diff**
> GetAccountDiff200Response get_account_diff(account_id, start_date, end_date)



Get account's balance change

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_account_diff200_response import GetAccountDiff200Response
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    start_date = 1668436763 # int | 
    end_date = 1668436763 # int | 

    try:
        api_response = api_instance.get_account_diff(account_id, start_date, end_date)
        print("The response of AccountsApi->get_account_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_diff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **start_date** | **int**|  | 
 **end_date** | **int**|  | 

### Return type

[**GetAccountDiff200Response**](GetAccountDiff200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s balance change |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_dns_expiring**
> DnsExpiring get_account_dns_expiring(account_id, period=period)



Get expiring account .ton dns

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.dns_expiring import DnsExpiring
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    period = 56 # int | number of days before expiration (optional)

    try:
        api_response = api_instance.get_account_dns_expiring(account_id, period=period)
        print("The response of AccountsApi->get_account_dns_expiring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_dns_expiring: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **period** | **int**| number of days before expiration | [optional] 

### Return type

[**DnsExpiring**](DnsExpiring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s expiring .ton dns |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_event**
> AccountEvent get_account_event(account_id, event_id, accept_language=accept_language, subject_only=subject_only)



Get event for an account by event_id

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_event import AccountEvent
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    event_id = '97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | event ID or transaction hash in hex (without 0x) or base64url format
    accept_language = 'en' # str |  (optional) (default to 'en')
    subject_only = False # bool | filter actions where requested account is not real subject (for example sender or receiver jettons) (optional) (default to False)

    try:
        api_response = api_instance.get_account_event(account_id, event_id, accept_language=accept_language, subject_only=subject_only)
        print("The response of AccountsApi->get_account_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **event_id** | **str**| event ID or transaction hash in hex (without 0x) or base64url format | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]
 **subject_only** | **bool**| filter actions where requested account is not real subject (for example sender or receiver jettons) | [optional] [default to False]

### Return type

[**AccountEvent**](AccountEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s event |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_events**
> AccountEvents get_account_events(account_id, limit, accept_language=accept_language, subject_only=subject_only, before_lt=before_lt, start_date=start_date, end_date=end_date)



Get events for an account. Each event is built on top of a trace which is a series of transactions caused by one inbound message. TonAPI looks for known patterns inside the trace and splits the trace into actions, where a single action represents a meaningful high-level operation like a Jetton Transfer or an NFT Purchase. Actions are expected to be shown to users. It is advised not to build any logic on top of actions because actions can be changed at any time.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_events import AccountEvents
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    limit = 100 # int | 
    accept_language = 'en' # str |  (optional) (default to 'en')
    subject_only = False # bool | filter actions where requested account is not real subject (for example sender or receiver jettons) (optional) (default to False)
    before_lt = 25758317000002 # int | omit this parameter to get last events (optional)
    start_date = 1668436763 # int |  (optional)
    end_date = 1668436763 # int |  (optional)

    try:
        api_response = api_instance.get_account_events(account_id, limit, accept_language=accept_language, subject_only=subject_only, before_lt=before_lt, start_date=start_date, end_date=end_date)
        print("The response of AccountsApi->get_account_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **limit** | **int**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]
 **subject_only** | **bool**| filter actions where requested account is not real subject (for example sender or receiver jettons) | [optional] [default to False]
 **before_lt** | **int**| omit this parameter to get last events | [optional] 
 **start_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 

### Return type

[**AccountEvents**](AccountEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s events |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_jetton_history_by_id**
> AccountEvents get_account_jetton_history_by_id(account_id, jetton_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)



Get the transfer jetton history for account and jetton

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_events import AccountEvents
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    jetton_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | jetton ID
    limit = 100 # int | 
    accept_language = 'en' # str |  (optional) (default to 'en')
    before_lt = 25758317000002 # int | omit this parameter to get last events (optional)
    start_date = 1668436763 # int |  (optional)
    end_date = 1668436763 # int |  (optional)

    try:
        api_response = api_instance.get_account_jetton_history_by_id(account_id, jetton_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)
        print("The response of AccountsApi->get_account_jetton_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_jetton_history_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **jetton_id** | **str**| jetton ID | 
 **limit** | **int**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]
 **before_lt** | **int**| omit this parameter to get last events | [optional] 
 **start_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 

### Return type

[**AccountEvents**](AccountEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account jetton history |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_jettons_balances**
> JettonsBalances get_account_jettons_balances(account_id)



Get all Jettons balances by owner address

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.jettons_balances import JettonsBalances
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_account_jettons_balances(account_id)
        print("The response of AccountsApi->get_account_jettons_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_jettons_balances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**JettonsBalances**](JettonsBalances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account jettons balances |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_jettons_history**
> AccountEvents get_account_jettons_history(account_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)



Get the transfer jettons history for account

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.account_events import AccountEvents
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    limit = 100 # int | 
    accept_language = 'en' # str |  (optional) (default to 'en')
    before_lt = 25758317000002 # int | omit this parameter to get last events (optional)
    start_date = 1668436763 # int |  (optional)
    end_date = 1668436763 # int |  (optional)

    try:
        api_response = api_instance.get_account_jettons_history(account_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)
        print("The response of AccountsApi->get_account_jettons_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_jettons_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **limit** | **int**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en&#39;]
 **before_lt** | **int**| omit this parameter to get last events | [optional] 
 **start_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 

### Return type

[**AccountEvents**](AccountEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account jettons history |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_nft_items**
> NftItems get_account_nft_items(account_id, collection=collection, limit=limit, offset=offset, indirect_ownership=indirect_ownership)



Get all NFT items by owner address

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.nft_items import NftItems
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    collection = '0:06d811f426598591b32b2c49f29f66c821368e4acb1de16762b04e0174532465' # str | nft collection (optional)
    limit = 1000 # int |  (optional) (default to 1000)
    offset = 0 # int |  (optional) (default to 0)
    indirect_ownership = False # bool | Selling nft items in ton implemented usually via transfer items to special selling account. This option enables including items which owned not directly. (optional) (default to False)

    try:
        api_response = api_instance.get_account_nft_items(account_id, collection=collection, limit=limit, offset=offset, indirect_ownership=indirect_ownership)
        print("The response of AccountsApi->get_account_nft_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_nft_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **collection** | **str**| nft collection | [optional] 
 **limit** | **int**|  | [optional] [default to 1000]
 **offset** | **int**|  | [optional] [default to 0]
 **indirect_ownership** | **bool**| Selling nft items in ton implemented usually via transfer items to special selling account. This option enables including items which owned not directly. | [optional] [default to False]

### Return type

[**NftItems**](NftItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account nft items |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_public_key**
> GetAccountPublicKey200Response get_account_public_key(account_id)



Get public key by account id

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_account_public_key200_response import GetAccountPublicKey200Response
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_account_public_key(account_id)
        print("The response of AccountsApi->get_account_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_public_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**GetAccountPublicKey200Response**](GetAccountPublicKey200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s public key |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_subscriptions**
> Subscriptions get_account_subscriptions(account_id)



Get all subscriptions by wallet address

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.subscriptions import Subscriptions
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_account_subscriptions(account_id)
        print("The response of AccountsApi->get_account_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s subscriptions |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_traces**
> TraceIDs get_account_traces(account_id, limit=limit)



Get traces for account

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.trace_ids import TraceIDs
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    limit = 100 # int |  (optional) (default to 100)

    try:
        api_response = api_instance.get_account_traces(account_id, limit=limit)
        print("The response of AccountsApi->get_account_traces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_traces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**TraceIDs**](TraceIDs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account&#39;s traces |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> Accounts get_accounts(get_accounts_request=get_accounts_request)



Get human-friendly information about several accounts without low-level details.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.accounts import Accounts
from fdtapi.models.get_accounts_request import GetAccountsRequest
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
    api_instance = fdtapi.AccountsApi(api_client)
    get_accounts_request = fdtapi.GetAccountsRequest() # GetAccountsRequest | a list of account ids (optional)

    try:
        api_response = api_instance.get_accounts(get_accounts_request=get_accounts_request)
        print("The response of AccountsApi->get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_accounts_request** | [**GetAccountsRequest**](GetAccountsRequest.md)| a list of account ids | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of accounts |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reindex_account**
> reindex_account(account_id)



Update internal cache for a particular account

### Example

```python
import time
import os
import fdtapi
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
    api_instance = fdtapi.AccountsApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_instance.reindex_account(account_id)
    except Exception as e:
        print("Exception when calling AccountsApi->reindex_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_accounts**
> FoundAccounts search_accounts(name)



Search by account domain name

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.found_accounts import FoundAccounts
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
    api_instance = fdtapi.AccountsApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.search_accounts(name)
        print("The response of AccountsApi->search_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->search_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**FoundAccounts**](FoundAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | found accounts |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

