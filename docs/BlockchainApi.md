# fdtapi.BlockchainApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exec_get_method_for_blockchain_account**](BlockchainApi.md#exec_get_method_for_blockchain_account) | **GET** /v2/blockchain/accounts/{account_id}/methods/{method_name} | 
[**get_blockchain_account_transactions**](BlockchainApi.md#get_blockchain_account_transactions) | **GET** /v2/blockchain/accounts/{account_id}/transactions | 
[**get_blockchain_block**](BlockchainApi.md#get_blockchain_block) | **GET** /v2/blockchain/blocks/{block_id} | 
[**get_blockchain_block_transactions**](BlockchainApi.md#get_blockchain_block_transactions) | **GET** /v2/blockchain/blocks/{block_id}/transactions | 
[**get_blockchain_config**](BlockchainApi.md#get_blockchain_config) | **GET** /v2/blockchain/config | 
[**get_blockchain_masterchain_head**](BlockchainApi.md#get_blockchain_masterchain_head) | **GET** /v2/blockchain/masterchain-head | 
[**get_blockchain_raw_account**](BlockchainApi.md#get_blockchain_raw_account) | **GET** /v2/blockchain/accounts/{account_id} | 
[**get_blockchain_transaction**](BlockchainApi.md#get_blockchain_transaction) | **GET** /v2/blockchain/transactions/{transaction_id} | 
[**get_blockchain_transaction_by_message_hash**](BlockchainApi.md#get_blockchain_transaction_by_message_hash) | **GET** /v2/blockchain/messages/{msg_id}/transaction | 
[**get_blockchain_validators**](BlockchainApi.md#get_blockchain_validators) | **GET** /v2/blockchain/validators | 
[**send_blockchain_message**](BlockchainApi.md#send_blockchain_message) | **POST** /v2/blockchain/message | 


# **exec_get_method_for_blockchain_account**
> MethodExecutionResult exec_get_method_for_blockchain_account(account_id, method_name, args=args)



Execute get method for account

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.method_execution_result import MethodExecutionResult
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
    api_instance = fdtapi.BlockchainApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    method_name = 'get_wallet_address' # str | contract get method name
    args = ['[\"0:9a33970f617bcd71acf2cd28357c067aa31859c02820d8f01d74c88063a8f4d8\"]'] # List[str] |  (optional)

    try:
        api_response = api_instance.exec_get_method_for_blockchain_account(account_id, method_name, args=args)
        print("The response of BlockchainApi->exec_get_method_for_blockchain_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->exec_get_method_for_blockchain_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **method_name** | **str**| contract get method name | 
 **args** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**MethodExecutionResult**](MethodExecutionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | method execution result |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_account_transactions**
> Transactions get_blockchain_account_transactions(account_id, after_lt=after_lt, before_lt=before_lt, limit=limit)



Get account transactions

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.transactions import Transactions
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
    api_instance = fdtapi.BlockchainApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    after_lt = 39787624000003 # int | omit this parameter to get last transactions (optional)
    before_lt = 39787624000003 # int | omit this parameter to get last transactions (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        api_response = api_instance.get_blockchain_account_transactions(account_id, after_lt=after_lt, before_lt=before_lt, limit=limit)
        print("The response of BlockchainApi->get_blockchain_account_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_account_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **after_lt** | **int**| omit this parameter to get last transactions | [optional] 
 **before_lt** | **int**| omit this parameter to get last transactions | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**Transactions**](Transactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain account transactions |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_block**
> BlockchainBlock get_blockchain_block(block_id)



Get blockchain block data

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.blockchain_block import BlockchainBlock
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
    api_instance = fdtapi.BlockchainApi(api_client)
    block_id = '(-1,8000000000000000,4234234)' # str | block ID

    try:
        api_response = api_instance.get_blockchain_block(block_id)
        print("The response of BlockchainApi->get_blockchain_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID | 

### Return type

[**BlockchainBlock**](BlockchainBlock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain block |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_block_transactions**
> Transactions get_blockchain_block_transactions(block_id)



Get transactions from block

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.transactions import Transactions
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
    api_instance = fdtapi.BlockchainApi(api_client)
    block_id = '(-1,8000000000000000,4234234)' # str | block ID

    try:
        api_response = api_instance.get_blockchain_block_transactions(block_id)
        print("The response of BlockchainApi->get_blockchain_block_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_block_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID | 

### Return type

[**Transactions**](Transactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain block transactions |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_config**
> BlockchainConfig get_blockchain_config()



Get blockchain config

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.blockchain_config import BlockchainConfig
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
    api_instance = fdtapi.BlockchainApi(api_client)

    try:
        api_response = api_instance.get_blockchain_config()
        print("The response of BlockchainApi->get_blockchain_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockchainConfig**](BlockchainConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain config |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_masterchain_head**
> BlockchainBlock get_blockchain_masterchain_head()



Get last known masterchain block

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.blockchain_block import BlockchainBlock
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
    api_instance = fdtapi.BlockchainApi(api_client)

    try:
        api_response = api_instance.get_blockchain_masterchain_head()
        print("The response of BlockchainApi->get_blockchain_masterchain_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_masterchain_head: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockchainBlock**](BlockchainBlock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain masterchain head |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_raw_account**
> BlockchainRawAccount get_blockchain_raw_account(account_id)



Get low-level information about an account taken directly from the blockchain.

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.blockchain_raw_account import BlockchainRawAccount
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
    api_instance = fdtapi.BlockchainApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_blockchain_raw_account(account_id)
        print("The response of BlockchainApi->get_blockchain_raw_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_raw_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**BlockchainRawAccount**](BlockchainRawAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw account |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_transaction**
> Transaction get_blockchain_transaction(transaction_id)



Get transaction data

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.transaction import Transaction
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
    api_instance = fdtapi.BlockchainApi(api_client)
    transaction_id = '97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | transaction ID

    try:
        api_response = api_instance.get_blockchain_transaction(transaction_id)
        print("The response of BlockchainApi->get_blockchain_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| transaction ID | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain transaction |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_transaction_by_message_hash**
> Transaction get_blockchain_transaction_by_message_hash(msg_id)



Get transaction data by message hash

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.transaction import Transaction
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
    api_instance = fdtapi.BlockchainApi(api_client)
    msg_id = '97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | message ID

    try:
        api_response = api_instance.get_blockchain_transaction_by_message_hash(msg_id)
        print("The response of BlockchainApi->get_blockchain_transaction_by_message_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_transaction_by_message_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| message ID | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transaction by message hash |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_validators**
> Validators get_blockchain_validators()



Get blockchain validators

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.validators import Validators
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
    api_instance = fdtapi.BlockchainApi(api_client)

    try:
        api_response = api_instance.get_blockchain_validators()
        print("The response of BlockchainApi->get_blockchain_validators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->get_blockchain_validators: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Validators**](Validators.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blockchain validators |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_blockchain_message**
> send_blockchain_message(send_blockchain_message_request)



Send message to blockchain

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.send_blockchain_message_request import SendBlockchainMessageRequest
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
    api_instance = fdtapi.BlockchainApi(api_client)
    send_blockchain_message_request = fdtapi.SendBlockchainMessageRequest() # SendBlockchainMessageRequest | both a single boc and a batch of boc serialized in base64 are accepted

    try:
        api_instance.send_blockchain_message(send_blockchain_message_request)
    except Exception as e:
        print("Exception when calling BlockchainApi->send_blockchain_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_blockchain_message_request** | [**SendBlockchainMessageRequest**](SendBlockchainMessageRequest.md)| both a single boc and a batch of boc serialized in base64 are accepted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the message has been sent |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

