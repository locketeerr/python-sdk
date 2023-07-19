# swagger_client.CurrenciesApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_currencies_crypto**](CurrenciesApi.md#list_currencies_crypto) | **GET** /api/currency/crypto | List Crypto Currencies
[**list_currencies_deposit**](CurrenciesApi.md#list_currencies_deposit) | **GET** /api/currency/deposit | List Wallet Currencies
[**list_currencies_fiat**](CurrenciesApi.md#list_currencies_fiat) | **GET** /api/currency/fiat | List Fiat Currencies

# **list_currencies_crypto**
> list[Merchant] list_currencies_crypto(offset=offset, max=max, allow_deposits=allow_deposits)

List Crypto Currencies

Retrieves a list of all cryptocurrencies available on the BVNK platform. This list represents cryptocurrencies that end users can select whilst making a payment.  For sandbox, only Ethereum (ETH) is fully functional.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CurrenciesApi()
offset = 0 # float | Offset (optional) (default to 0)
max = 200 # float | Maximum number of items in response (optional) (default to 200)
allow_deposits = false # bool | list currencies that only allow deposits (optional) (default to false)

try:
    # List Crypto Currencies
    api_response = api_instance.list_currencies_crypto(offset=offset, max=max, allow_deposits=allow_deposits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_currencies_crypto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| Offset | [optional] [default to 0]
 **max** | **float**| Maximum number of items in response | [optional] [default to 200]
 **allow_deposits** | **bool**| list currencies that only allow deposits | [optional] [default to false]

### Return type

[**list[Merchant]**](Merchant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currencies_deposit**
> list[Merchant] list_currencies_deposit(offset=offset, max=max)

List Wallet Currencies

These are the currencies that can be used to create a new wallet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CurrenciesApi()
offset = 0 # float | Offset (optional) (default to 0)
max = 200 # float | Maximum number of items in response (optional) (default to 200)

try:
    # List Wallet Currencies
    api_response = api_instance.list_currencies_deposit(offset=offset, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_currencies_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| Offset | [optional] [default to 0]
 **max** | **float**| Maximum number of items in response | [optional] [default to 200]

### Return type

[**list[Merchant]**](Merchant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currencies_fiat**
> list[Merchant] list_currencies_fiat(offset=offset, max=max, usable=usable)

List Fiat Currencies

Retrieves a list of all display fiat currencies available on BVNK's Crypto Payments API. This list refers to currencies merchants can display on a payment page to an end user. It does not represent the list of currencies that can be held on the platform in wallets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CurrenciesApi()
offset = 0 # float | Offset (optional) (default to 0)
max = 200 # float | Maximum number of items in response (optional) (default to 200)
usable = false # bool | list currencies that are usable (optional) (default to false)

try:
    # List Fiat Currencies
    api_response = api_instance.list_currencies_fiat(offset=offset, max=max, usable=usable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_currencies_fiat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| Offset | [optional] [default to 0]
 **max** | **float**| Maximum number of items in response | [optional] [default to 200]
 **usable** | **bool**| list currencies that are usable | [optional] [default to false]

### Return type

[**list[Merchant]**](Merchant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

