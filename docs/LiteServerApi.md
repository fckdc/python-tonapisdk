# fdtapi.LiteServerApi

All URIs are relative to *https://tonapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_raw_shards_info**](LiteServerApi.md#get_all_raw_shards_info) | **GET** /v2/liteserver/get_all_shards_info/{block_id} | 
[**get_raw_account_state**](LiteServerApi.md#get_raw_account_state) | **GET** /v2/liteserver/get_account_state/{account_id} | 
[**get_raw_block_proof**](LiteServerApi.md#get_raw_block_proof) | **GET** /v2/liteserver/get_block_proof | 
[**get_raw_blockchain_block**](LiteServerApi.md#get_raw_blockchain_block) | **GET** /v2/liteserver/get_block/{block_id} | 
[**get_raw_blockchain_block_header**](LiteServerApi.md#get_raw_blockchain_block_header) | **GET** /v2/liteserver/get_block_header/{block_id} | 
[**get_raw_blockchain_block_state**](LiteServerApi.md#get_raw_blockchain_block_state) | **GET** /v2/liteserver/get_state/{block_id} | 
[**get_raw_config**](LiteServerApi.md#get_raw_config) | **GET** /v2/liteserver/get_config_all/{block_id} | 
[**get_raw_list_block_transactions**](LiteServerApi.md#get_raw_list_block_transactions) | **GET** /v2/liteserver/list_block_transactions/{block_id} | 
[**get_raw_masterchain_info**](LiteServerApi.md#get_raw_masterchain_info) | **GET** /v2/liteserver/get_masterchain_info | 
[**get_raw_masterchain_info_ext**](LiteServerApi.md#get_raw_masterchain_info_ext) | **GET** /v2/liteserver/get_masterchain_info_ext | 
[**get_raw_shard_block_proof**](LiteServerApi.md#get_raw_shard_block_proof) | **GET** /v2/liteserver/get_shard_block_proof/{block_id} | 
[**get_raw_shard_info**](LiteServerApi.md#get_raw_shard_info) | **GET** /v2/liteserver/get_shard_info/{block_id} | 
[**get_raw_time**](LiteServerApi.md#get_raw_time) | **GET** /v2/liteserver/get_time | 
[**get_raw_transactions**](LiteServerApi.md#get_raw_transactions) | **GET** /v2/liteserver/get_transactions/{account_id} | 
[**send_raw_message**](LiteServerApi.md#send_raw_message) | **POST** /v2/liteserver/send_message | 


# **get_all_raw_shards_info**
> GetAllRawShardsInfo200Response get_all_raw_shards_info(block_id)



Get all raw shards info

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_all_raw_shards_info200_response import GetAllRawShardsInfo200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)

    try:
        api_response = api_instance.get_all_raw_shards_info(block_id)
        print("The response of LiteServerApi->get_all_raw_shards_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_all_raw_shards_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 

### Return type

[**GetAllRawShardsInfo200Response**](GetAllRawShardsInfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | all raw shards info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_account_state**
> GetRawAccountState200Response get_raw_account_state(account_id)



Get raw account state

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_account_state200_response import GetRawAccountState200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID

    try:
        api_response = api_instance.get_raw_account_state(account_id)
        print("The response of LiteServerApi->get_raw_account_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_account_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 

### Return type

[**GetRawAccountState200Response**](GetRawAccountState200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw account state |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_block_proof**
> GetRawBlockProof200Response get_raw_block_proof(known_block, mode, target_block=target_block)



Get raw block proof

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_block_proof200_response import GetRawBlockProof200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    known_block = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | known block: (workchain,shard,seqno,root_hash,file_hash)
    mode = 0 # int | mode
    target_block = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | target block: (workchain,shard,seqno,root_hash,file_hash) (optional)

    try:
        api_response = api_instance.get_raw_block_proof(known_block, mode, target_block=target_block)
        print("The response of LiteServerApi->get_raw_block_proof:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_block_proof: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **known_block** | **str**| known block: (workchain,shard,seqno,root_hash,file_hash) | 
 **mode** | **int**| mode | 
 **target_block** | **str**| target block: (workchain,shard,seqno,root_hash,file_hash) | [optional] 

### Return type

[**GetRawBlockProof200Response**](GetRawBlockProof200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw block proof |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_blockchain_block**
> GetRawBlockchainBlock200Response get_raw_blockchain_block(block_id)



Get raw blockchain block

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_blockchain_block200_response import GetRawBlockchainBlock200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)

    try:
        api_response = api_instance.get_raw_blockchain_block(block_id)
        print("The response of LiteServerApi->get_raw_blockchain_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_blockchain_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 

### Return type

[**GetRawBlockchainBlock200Response**](GetRawBlockchainBlock200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw blockchain block |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_blockchain_block_header**
> GetRawBlockchainBlockHeader200Response get_raw_blockchain_block_header(block_id, mode)



Get raw blockchain block header

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_blockchain_block_header200_response import GetRawBlockchainBlockHeader200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)
    mode = 0 # int | mode

    try:
        api_response = api_instance.get_raw_blockchain_block_header(block_id, mode)
        print("The response of LiteServerApi->get_raw_blockchain_block_header:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_blockchain_block_header: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 
 **mode** | **int**| mode | 

### Return type

[**GetRawBlockchainBlockHeader200Response**](GetRawBlockchainBlockHeader200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw blockchain block header |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_blockchain_block_state**
> GetRawBlockchainBlockState200Response get_raw_blockchain_block_state(block_id)



Get raw blockchain block state

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_blockchain_block_state200_response import GetRawBlockchainBlockState200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)

    try:
        api_response = api_instance.get_raw_blockchain_block_state(block_id)
        print("The response of LiteServerApi->get_raw_blockchain_block_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_blockchain_block_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 

### Return type

[**GetRawBlockchainBlockState200Response**](GetRawBlockchainBlockState200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw blockchain block state |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_config**
> GetRawConfig200Response get_raw_config(block_id, mode)



Get raw config

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_config200_response import GetRawConfig200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)
    mode = 0 # int | mode

    try:
        api_response = api_instance.get_raw_config(block_id, mode)
        print("The response of LiteServerApi->get_raw_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 
 **mode** | **int**| mode | 

### Return type

[**GetRawConfig200Response**](GetRawConfig200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw config |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_list_block_transactions**
> GetRawListBlockTransactions200Response get_raw_list_block_transactions(block_id, mode, count, account_id=account_id, lt=lt)



Get raw list block transactions

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_list_block_transactions200_response import GetRawListBlockTransactions200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)
    mode = 0 # int | mode
    count = 100 # int | count
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID (optional)
    lt = 23814011000000 # int | lt (optional)

    try:
        api_response = api_instance.get_raw_list_block_transactions(block_id, mode, count, account_id=account_id, lt=lt)
        print("The response of LiteServerApi->get_raw_list_block_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_list_block_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 
 **mode** | **int**| mode | 
 **count** | **int**| count | 
 **account_id** | **str**| account ID | [optional] 
 **lt** | **int**| lt | [optional] 

### Return type

[**GetRawListBlockTransactions200Response**](GetRawListBlockTransactions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a list of raw block transactions |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_masterchain_info**
> GetRawMasterchainInfo200Response get_raw_masterchain_info()



Get raw masterchain info

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_masterchain_info200_response import GetRawMasterchainInfo200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)

    try:
        api_response = api_instance.get_raw_masterchain_info()
        print("The response of LiteServerApi->get_raw_masterchain_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_masterchain_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRawMasterchainInfo200Response**](GetRawMasterchainInfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw masterchain info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_masterchain_info_ext**
> GetRawMasterchainInfoExt200Response get_raw_masterchain_info_ext(mode)



Get raw masterchain info ext

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_masterchain_info_ext200_response import GetRawMasterchainInfoExt200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    mode = 0 # int | mode

    try:
        api_response = api_instance.get_raw_masterchain_info_ext(mode)
        print("The response of LiteServerApi->get_raw_masterchain_info_ext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_masterchain_info_ext: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **int**| mode | 

### Return type

[**GetRawMasterchainInfoExt200Response**](GetRawMasterchainInfoExt200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw masterchain info ext |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_shard_block_proof**
> GetRawShardBlockProof200Response get_raw_shard_block_proof(block_id)



Get raw shard block proof

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_shard_block_proof200_response import GetRawShardBlockProof200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)

    try:
        api_response = api_instance.get_raw_shard_block_proof(block_id)
        print("The response of LiteServerApi->get_raw_shard_block_proof:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_shard_block_proof: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 

### Return type

[**GetRawShardBlockProof200Response**](GetRawShardBlockProof200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw shard block proof |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_shard_info**
> GetRawShardInfo200Response get_raw_shard_info(block_id, workchain, shard, exact)



Get raw shard info

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_shard_info200_response import GetRawShardInfo200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    block_id = '(-1,8000000000000000,4234234,3E575DAB1D25...90D8,47192E5C46C...BB29)' # str | block ID: (workchain,shard,seqno,root_hash,file_hash)
    workchain = 1 # int | workchain
    shard = 1 # int | shard
    exact = false # bool | exact

    try:
        api_response = api_instance.get_raw_shard_info(block_id, workchain, shard, exact)
        print("The response of LiteServerApi->get_raw_shard_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_shard_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| block ID: (workchain,shard,seqno,root_hash,file_hash) | 
 **workchain** | **int**| workchain | 
 **shard** | **int**| shard | 
 **exact** | **bool**| exact | 

### Return type

[**GetRawShardInfo200Response**](GetRawShardInfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw shard info |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_time**
> GetRawTime200Response get_raw_time()



Get raw time

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_time200_response import GetRawTime200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)

    try:
        api_response = api_instance.get_raw_time()
        print("The response of LiteServerApi->get_raw_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_time: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRawTime200Response**](GetRawTime200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw time |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transactions**
> GetRawTransactions200Response get_raw_transactions(account_id, count, lt, hash)



Get raw transactions

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.get_raw_transactions200_response import GetRawTransactions200Response
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
    api_instance = fdtapi.LiteServerApi(api_client)
    account_id = '0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621' # str | account ID
    count = 100 # int | count
    lt = 23814011000000 # int | lt
    hash = '131D0C65055F04E9C19D687B51BC70F952FD9CA6F02C2801D3B89964A779DF85' # str | hash

    try:
        api_response = api_instance.get_raw_transactions(account_id, count, lt, hash)
        print("The response of LiteServerApi->get_raw_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->get_raw_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account ID | 
 **count** | **int**| count | 
 **lt** | **int**| lt | 
 **hash** | **str**| hash | 

### Return type

[**GetRawTransactions200Response**](GetRawTransactions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | raw transactions |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_message**
> SendRawMessage200Response send_raw_message(send_raw_message_request)



Send raw message to blockchain

### Example

```python
import time
import os
import fdtapi
from fdtapi.models.send_raw_message200_response import SendRawMessage200Response
from fdtapi.models.send_raw_message_request import SendRawMessageRequest
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
    api_instance = fdtapi.LiteServerApi(api_client)
    send_raw_message_request = fdtapi.SendRawMessageRequest() # SendRawMessageRequest | Data that is expected

    try:
        api_response = api_instance.send_raw_message(send_raw_message_request)
        print("The response of LiteServerApi->send_raw_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiteServerApi->send_raw_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_raw_message_request** | [**SendRawMessageRequest**](SendRawMessageRequest.md)| Data that is expected | 

### Return type

[**SendRawMessage200Response**](SendRawMessage200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | code |  -  |
**0** | Some error during request processing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

