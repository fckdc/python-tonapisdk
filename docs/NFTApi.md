# fdtapi.NFTApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_nft_history**](NFTApi.md#get_account_nft_history) | **GET** /v2/accounts/{account_id}/nfts/history | 
[**get_items_from_collection**](NFTApi.md#get_items_from_collection) | **GET** /v2/nfts/collections/{account_id}/items | 
[**get_nft_collection**](NFTApi.md#get_nft_collection) | **GET** /v2/nfts/collections/{account_id} | 
[**get_nft_collections**](NFTApi.md#get_nft_collections) | **GET** /v2/nfts/collections | 
[**get_nft_history_by_id**](NFTApi.md#get_nft_history_by_id) | **GET** /v2/nfts/{account_id}/history | 
[**get_nft_item_by_address**](NFTApi.md#get_nft_item_by_address) | **GET** /v2/nfts/{account_id} | 
[**get_nft_items_by_addresses**](NFTApi.md#get_nft_items_by_addresses) | **POST** /v2/nfts/_bulk | 


# **get_account_nft_history**
> AccountEvents get_account_nft_history(account_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)



Get the transfer nft history

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
    api_instance = fdtapi.NFTApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    limit = 100 # int | 
    accept_language = 'en' # str |  (optional) (default to 'en')
    before_lt = 25758317000002 # int | omit this parameter to get last events (optional)
    start_date = 1668436763 # int |  (optional)
    end_date = 1668436763 # int |  (optional)

    try:
        api_response = api_instance.get_account_nft_history(account_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)
        print("The response of NFTApi->get_account_nft_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_account_nft_history: %s\n" % e)
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
**200** | nft history |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_from_collection**
> NftItems get_items_from_collection(account_id, limit=limit, offset=offset)



Get NFT items from collection by collection address

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
    api_instance = fdtapi.NFTApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    limit = 1000 # int |  (optional) (default to 1000)
    offset = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.get_items_from_collection(account_id, limit=limit, offset=offset)
        print("The response of NFTApi->get_items_from_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_items_from_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **limit** | **int**|  | [optional] [default to 1000]
 **offset** | **int**|  | [optional] [default to 0]

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
**200** | nft items |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nft_collection**
> NftCollection get_nft_collection(account_id)



Get NFT collection by collection address

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.nft_collection import NftCollection
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
    api_instance = fdtapi.NFTApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_nft_collection(account_id)
        print("The response of NFTApi->get_nft_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_nft_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**NftCollection**](NftCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | nft collection |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nft_collections**
> NftCollections get_nft_collections(limit=limit, offset=offset)



Get NFT collections

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.nft_collections import NftCollections
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
    api_instance = fdtapi.NFTApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.get_nft_collections(limit=limit, offset=offset)
        print("The response of NFTApi->get_nft_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_nft_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**NftCollections**](NftCollections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | nft collections |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nft_history_by_id**
> AccountEvents get_nft_history_by_id(account_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)



Get the transfer nfts history for account

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
    api_instance = fdtapi.NFTApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    limit = 100 # int | 
    accept_language = 'en' # str |  (optional) (default to 'en')
    before_lt = 25758317000002 # int | omit this parameter to get last events (optional)
    start_date = 1668436763 # int |  (optional)
    end_date = 1668436763 # int |  (optional)

    try:
        api_response = api_instance.get_nft_history_by_id(account_id, limit, accept_language=accept_language, before_lt=before_lt, start_date=start_date, end_date=end_date)
        print("The response of NFTApi->get_nft_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_nft_history_by_id: %s\n" % e)
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
**200** | nft history |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nft_item_by_address**
> NftItem get_nft_item_by_address(account_id)



Get NFT item by its address

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.nft_item import NftItem
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
    api_instance = fdtapi.NFTApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_nft_item_by_address(account_id)
        print("The response of NFTApi->get_nft_item_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_nft_item_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**NftItem**](NftItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | nft item |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nft_items_by_addresses**
> NftItems get_nft_items_by_addresses(get_accounts_request=get_accounts_request)



Get NFT items by their addresses

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_accounts_request import GetAccountsRequest
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
    api_instance = fdtapi.NFTApi(api_client)
    get_accounts_request = fdtapi.GetAccountsRequest() # GetAccountsRequest | a list of account ids (optional)

    try:
        api_response = api_instance.get_nft_items_by_addresses(get_accounts_request=get_accounts_request)
        print("The response of NFTApi->get_nft_items_by_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTApi->get_nft_items_by_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_accounts_request** | [**GetAccountsRequest**](GetAccountsRequest.md)| a list of account ids | [optional] 

### Return type

[**NftItems**](NftItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | nft items |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

