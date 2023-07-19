# swagger_client.WalletsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_report**](WalletsApi.md#transaction_report) | **GET** /api/transaction/report | Transactions Report
[**wallet_balance_list**](WalletsApi.md#wallet_balance_list) | **GET** /api/wallet/balances | List Wallet Balances
[**wallet_create**](WalletsApi.md#wallet_create) | **POST** /api/wallet | Create Wallet
[**wallet_list**](WalletsApi.md#wallet_list) | **GET** /api/wallet | List Wallets
[**wallet_r_get**](WalletsApi.md#wallet_r_get) | **GET** /api/wallet/{id} | Get Wallet

# **transaction_report**
> list[TransactionReport] transaction_report(wallet_id=wallet_id, from_date=from_date, to_date=to_date, format=format, transaction_type=transaction_type)

Transactions Report

Report all transactions from wallet in specified format. Report will be generated and sent to main account email in the specified format

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Hawk
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
wallet_id = 255861 # int | Date at to retrieve balances (optional) (default to 255861)
from_date = '2022-09-17' # str | Export range from date in format 'yyyy-MM-dd' (optional) (default to 2022-09-17)
to_date = '2023-03-17' # str | Export range to date in format 'yyyy-MM-dd' (optional) (default to 2023-03-17)
format = 'csv' # str | 'json' - json format, 'csv' - csv format (optional) (default to csv)
transaction_type = 'transaction_type_example' # str | Transaction type code (optional)

try:
    # Transactions Report
    api_response = api_instance.transaction_report(wallet_id=wallet_id, from_date=from_date, to_date=to_date, format=format, transaction_type=transaction_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->transaction_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**| Date at to retrieve balances | [optional] [default to 255861]
 **from_date** | **str**| Export range from date in format &#x27;yyyy-MM-dd&#x27; | [optional] [default to 2022-09-17]
 **to_date** | **str**| Export range to date in format &#x27;yyyy-MM-dd&#x27; | [optional] [default to 2023-03-17]
 **format** | **str**| &#x27;json&#x27; - json format, &#x27;csv&#x27; - csv format | [optional] [default to csv]
 **transaction_type** | **str**| Transaction type code | [optional] 

### Return type

[**list[TransactionReport]**](TransactionReport.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_balance_list**
> list[Balance] wallet_balance_list(_date=_date)

List Wallet Balances

Retrieves the balances of your wallets on platform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Hawk
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
_date = '_date_example' # str | Date at to retrieve balances (optional)

try:
    # List Wallet Balances
    api_response = api_instance.wallet_balance_list(_date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallet_balance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**| Date at to retrieve balances | [optional] 

### Return type

[**list[Balance]**](Balance.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_create**
> Wallet wallet_create(body=body)

Create Wallet

Creates a wallet on the BVNK platform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Hawk
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
body = swagger_client.WalletRequest() # WalletRequest |  (optional)

try:
    # Create Wallet
    api_response = api_instance.wallet_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallet_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WalletRequest**](WalletRequest.md)|  | [optional] 

### Return type

[**Wallet**](Wallet.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_list**
> list[Wallet] wallet_list(offset=offset, max=max)

List Wallets

Retrieves a list of wallets on your account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Hawk
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
offset = 56 # int | start offset (optional)
max = 10 # int | max number results (optional) (default to 10)

try:
    # List Wallets
    api_response = api_instance.wallet_list(offset=offset, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallet_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| start offset | [optional] 
 **max** | **int**| max number results | [optional] [default to 10]

### Return type

[**list[Wallet]**](Wallet.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_r_get**
> Wallet wallet_r_get(id)

Get Wallet

Retrieves a specific wallet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Hawk
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
id = 789 # int | start offset

try:
    # Get Wallet
    api_response = api_instance.wallet_r_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallet_r_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| start offset | 

### Return type

[**Wallet**](Wallet.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

