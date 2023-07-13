<a id="__pageTop"></a>
# openapi_client.apis.tags.currencies_api.CurrenciesApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_currencies_crypto**](#list_currencies_crypto) | **get** /api/currency/crypto | List Crypto Currencies
[**list_currencies_deposit**](#list_currencies_deposit) | **get** /api/currency/deposit | List Wallet Currencies
[**list_currencies_fiat**](#list_currencies_fiat) | **get** /api/currency/fiat | List Fiat Currencies

# **list_currencies_crypto**
<a id="list_currencies_crypto"></a>
> [Merchant] list_currencies_crypto()

List Crypto Currencies

Retrieves a list of all cryptocurrencies available on the BVNK platform. This list represents cryptocurrencies that end users can select whilst making a payment.  For sandbox, only Ethereum (ETH) is fully functional.

### Example

```python
import openapi_client
from openapi_client.apis.tags import currencies_api
from openapi_client.model.merchant import Merchant
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'max': 200,
        'allowDeposits': False,
    }
    try:
        # List Crypto Currencies
        api_response = api_instance.list_currencies_crypto(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_currencies_crypto: %s\n" % e)
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
allowDeposits | AllowDepositsSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 200

# AllowDepositsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_currencies_crypto.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_currencies_crypto.ApiResponseFor400) | Bad Request

#### list_currencies_crypto.ApiResponseFor200
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
[**Merchant**]({{complexTypePrefix}}Merchant.md) | [**Merchant**]({{complexTypePrefix}}Merchant.md) | [**Merchant**]({{complexTypePrefix}}Merchant.md) |  | 

#### list_currencies_crypto.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_currencies_deposit**
<a id="list_currencies_deposit"></a>
> [Merchant] list_currencies_deposit()

List Wallet Currencies

These are the currencies that can be used to create a new wallet.

### Example

```python
import openapi_client
from openapi_client.apis.tags import currencies_api
from openapi_client.model.merchant import Merchant
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'max': 200,
    }
    try:
        # List Wallet Currencies
        api_response = api_instance.list_currencies_deposit(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_currencies_deposit: %s\n" % e)
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
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 200

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_currencies_deposit.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_currencies_deposit.ApiResponseFor400) | Bad Request

#### list_currencies_deposit.ApiResponseFor200
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
[**Merchant**]({{complexTypePrefix}}Merchant.md) | [**Merchant**]({{complexTypePrefix}}Merchant.md) | [**Merchant**]({{complexTypePrefix}}Merchant.md) |  | 

#### list_currencies_deposit.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_currencies_fiat**
<a id="list_currencies_fiat"></a>
> [Merchant] list_currencies_fiat()

List Fiat Currencies

Retrieves a list of all display fiat currencies available on BVNK's Crypto Payments API. This list refers to currencies merchants can display on a payment page to an end user. It does not represent the list of currencies that can be held on the platform in wallets.

### Example

```python
import openapi_client
from openapi_client.apis.tags import currencies_api
from openapi_client.model.merchant import Merchant
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'max': 200,
        'usable': False,
    }
    try:
        # List Fiat Currencies
        api_response = api_instance.list_currencies_fiat(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_currencies_fiat: %s\n" % e)
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
usable | UsableSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 200

# UsableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_currencies_fiat.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_currencies_fiat.ApiResponseFor400) | Bad Request

#### list_currencies_fiat.ApiResponseFor200
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
[**Merchant**]({{complexTypePrefix}}Merchant.md) | [**Merchant**]({{complexTypePrefix}}Merchant.md) | [**Merchant**]({{complexTypePrefix}}Merchant.md) |  | 

#### list_currencies_fiat.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

