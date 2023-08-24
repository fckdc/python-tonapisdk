# fdtapi.WalletApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_seqno**](WalletApi.md#get_account_seqno) | **GET** /v2/wallet/{account_id}/seqno | 
[**get_wallet_backup**](WalletApi.md#get_wallet_backup) | **GET** /v2/wallet/backup | 
[**get_wallets_by_public_key**](WalletApi.md#get_wallets_by_public_key) | **GET** /v2/pubkeys/{public_key}/wallets | 
[**set_wallet_backup**](WalletApi.md#set_wallet_backup) | **PUT** /v2/wallet/backup | 
[**ton_connect_proof**](WalletApi.md#ton_connect_proof) | **POST** /v2/wallet/auth/proof | 


# **get_account_seqno**
> Seqno get_account_seqno(account_id)



Get account seqno

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.seqno import Seqno
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
    api_instance = fdtapi.WalletApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_account_seqno(account_id)
        print("The response of WalletApi->get_account_seqno:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_account_seqno: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**Seqno**](Seqno.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | account seqno |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_backup**
> GetWalletBackup200Response get_wallet_backup(x_ton_connect_auth)



Get backup info

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_wallet_backup200_response import GetWalletBackup200Response
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
    api_instance = fdtapi.WalletApi(api_client)
    x_ton_connect_auth = 'x_ton_connect_auth_example' # str | 

    try:
        api_response = api_instance.get_wallet_backup(x_ton_connect_auth)
        print("The response of WalletApi->get_wallet_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_wallet_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ton_connect_auth** | **str**|  | 

### Return type

[**GetWalletBackup200Response**](GetWalletBackup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get wallet dump |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallets_by_public_key**
> Accounts get_wallets_by_public_key(public_key)



Get wallets by public key

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.accounts import Accounts
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
    api_instance = fdtapi.WalletApi(api_client)
    public_key = 'NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ3...' # str | 

    try:
        api_response = api_instance.get_wallets_by_public_key(public_key)
        print("The response of WalletApi->get_wallets_by_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_wallets_by_public_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_key** | **str**|  | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of wallets |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_wallet_backup**
> set_wallet_backup(x_ton_connect_auth, body)



Set backup info

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
    api_instance = fdtapi.WalletApi(api_client)
    x_ton_connect_auth = 'x_ton_connect_auth_example' # str | 
    body = None # bytearray | Information for saving backup

    try:
        api_instance.set_wallet_backup(x_ton_connect_auth, body)
    except Exception as e:
        print("Exception when calling WalletApi->set_wallet_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ton_connect_auth** | **str**|  | 
 **body** | **bytearray**| Information for saving backup | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ton_connect_proof**
> TonConnectProof200Response ton_connect_proof(ton_connect_proof_request)



Account verification and token issuance

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.ton_connect_proof200_response import TonConnectProof200Response
from fdtapi.models.ton_connect_proof_request import TonConnectProofRequest
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
    api_instance = fdtapi.WalletApi(api_client)
    ton_connect_proof_request = fdtapi.TonConnectProofRequest() # TonConnectProofRequest | Data that is expected from TON Connect

    try:
        api_response = api_instance.ton_connect_proof(ton_connect_proof_request)
        print("The response of WalletApi->ton_connect_proof:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->ton_connect_proof: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ton_connect_proof_request** | [**TonConnectProofRequest**](TonConnectProofRequest.md)| Data that is expected from TON Connect | 

### Return type

[**TonConnectProof200Response**](TonConnectProof200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | auth token |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

