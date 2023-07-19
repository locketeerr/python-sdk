<a id="__pageTop"></a>
# openapi_client.apis.tags.wallets_api.WalletsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_report**](#transaction_report) | **get** /api/transaction/report | Transactions Report
[**wallet_balance_list**](#wallet_balance_list) | **get** /api/wallet/balances | List Wallet Balances
[**wallet_create**](#wallet_create) | **post** /api/wallet | Create Wallet
[**wallet_list**](#wallet_list) | **get** /api/wallet | List Wallets
[**wallet_r_get**](#wallet_r_get) | **get** /api/wallet/{id} | Get Wallet

# **transaction_report**
<a id="transaction_report"></a>
> [TransactionReport] transaction_report()

Transactions Report

Report all transactions from wallet in specified format. Report will be generated and sent to main account email in the specified format

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import wallets_api
from openapi_client.model.transaction_report import TransactionReport
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Hawk
configuration.api_key['Hawk'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Hawk'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)

    # example passing only optional values
    query_params = {
        'walletId': 255861,
        'fromDate': "2022-09-17",
        'toDate': "2023-03-17",
        'format': "csv",
        'transactionType': "transactionType_example",
    }
    try:
        # Transactions Report
        api_response = api_instance.transaction_report(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletsApi->transaction_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
walletId | WalletIdSchema | | optional
fromDate | FromDateSchema | | optional
toDate | ToDateSchema | | optional
format | FormatSchema | | optional
transactionType | TransactionTypeSchema | | optional


# WalletIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 255861value must be a 64 bit integer

# FromDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "2022-09-17"

# ToDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "2023-03-17"

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "csv"

# TransactionTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#transaction_report.ApiResponseFor200) | OK

#### transaction_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionReport**]({{complexTypePrefix}}TransactionReport.md) | [**TransactionReport**]({{complexTypePrefix}}TransactionReport.md) | [**TransactionReport**]({{complexTypePrefix}}TransactionReport.md) |  | 

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wallet_balance_list**
<a id="wallet_balance_list"></a>
> [Balance] wallet_balance_list()

List Wallet Balances

Retrieves the balances of your wallets on platform.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import wallets_api
from openapi_client.model.balance import Balance
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Hawk
configuration.api_key['Hawk'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Hawk'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)

    # example passing only optional values
    query_params = {
        'date': "2020-03-17",
    }
    try:
        # List Wallet Balances
        api_response = api_instance.wallet_balance_list(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletsApi->wallet_balance_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
date | DateSchema | | optional


# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wallet_balance_list.ApiResponseFor200) | OK

#### wallet_balance_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Balance**]({{complexTypePrefix}}Balance.md) | [**Balance**]({{complexTypePrefix}}Balance.md) | [**Balance**]({{complexTypePrefix}}Balance.md) |  | 

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wallet_create**
<a id="wallet_create"></a>
> Wallet wallet_create()

Create Wallet

Creates a wallet on the BVNK platform.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import wallets_api
from openapi_client.model.wallet import Wallet
from openapi_client.model.wallet_request import WalletRequest
from openapi_client.model.server_error_dto import ServerErrorDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Hawk
configuration.api_key['Hawk'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Hawk'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)

    # example passing only optional values
    body = WalletRequest(
        currency="ETH",
        description="My 2nd EUR Wallet",
    )
    try:
        # Create Wallet
        api_response = api_instance.wallet_create(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletsApi->wallet_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WalletRequest**](../../models/WalletRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#wallet_create.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#wallet_create.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#wallet_create.ApiResponseFor500) | Unexpected Error

#### wallet_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Wallet**](../../models/Wallet.md) |  | 


#### wallet_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### wallet_create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerErrorDto**](../../models/ServerErrorDto.md) |  | 


### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wallet_list**
<a id="wallet_list"></a>
> [Wallet] wallet_list()

List Wallets

Retrieves a list of wallets on your account.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import wallets_api
from openapi_client.model.wallet import Wallet
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Hawk
configuration.api_key['Hawk'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Hawk'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 1,
        'max': 10,
    }
    try:
        # List Wallets
        api_response = api_instance.wallet_list(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletsApi->wallet_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
offset | OffsetSchema | | optional
max | MaxSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wallet_list.ApiResponseFor200) | OK

#### wallet_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Wallet**]({{complexTypePrefix}}Wallet.md) | [**Wallet**]({{complexTypePrefix}}Wallet.md) | [**Wallet**]({{complexTypePrefix}}Wallet.md) |  | 

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wallet_r_get**
<a id="wallet_r_get"></a>
> Wallet wallet_r_get()

Get Wallet

Retrieves a specific wallet.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import wallets_api
from openapi_client.model.wallet import Wallet
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Hawk
configuration.api_key['Hawk'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Hawk'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 255861,
    }
    try:
        # Get Wallet
        api_response = api_instance.wallet_r_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WalletsApi->wallet_r_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 255861value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wallet_r_get.ApiResponseFor200) | OK

#### wallet_r_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Wallet**](../../models/Wallet.md) |  | 


### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

