# swagger_client.TradingAndConversionsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_accept**](TradingAndConversionsApi.md#quote_accept) | **PUT** /api/v1/quote/accept/{uuid} | Accept Quote
[**quote_create**](TradingAndConversionsApi.md#quote_create) | **POST** /api/v1/quote | Create Quote
[**quote_list**](TradingAndConversionsApi.md#quote_list) | **GET** /api/v1/quote/{merchantId} | List Quotes
[**quote_read**](TradingAndConversionsApi.md#quote_read) | **GET** /api/v1/quote/{uuid} | Read Quote

# **quote_accept**
> AcceptedQuote quote_accept(uuid)

Accept Quote

Executes a quote.

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
api_instance = swagger_client.TradingAndConversionsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The quote UUID you are accepting.

try:
    # Accept Quote
    api_response = api_instance.quote_accept(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAndConversionsApi->quote_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote UUID you are accepting. | 

### Return type

[**AcceptedQuote**](AcceptedQuote.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_create**
> Quote quote_create(body=body, estimate=estimate)

Create Quote

Creates a quote to convert between wallets.

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
api_instance = swagger_client.TradingAndConversionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuoteRequest() # QuoteRequest |  (optional)
estimate = false # bool | Create estimate quote (optional) (default to false)

try:
    # Create Quote
    api_response = api_instance.quote_create(body=body, estimate=estimate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAndConversionsApi->quote_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuoteRequest**](QuoteRequest.md)|  | [optional] 
 **estimate** | **bool**| Create estimate quote | [optional] [default to false]

### Return type

[**Quote**](Quote.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_list**
> list[Quote] quote_list(merchant_id)

List Quotes

Retrieves all quotes on a specific Merchant ID.

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
api_instance = swagger_client.TradingAndConversionsApi(swagger_client.ApiClient(configuration))
merchant_id = 'merchant_id_example' # str | Merchant ID you are retrieving quotes from.

try:
    # List Quotes
    api_response = api_instance.quote_list(merchant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAndConversionsApi->quote_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Merchant ID you are retrieving quotes from. | 

### Return type

[**list[Quote]**](Quote.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_read**
> Quote quote_read(uuid)

Read Quote

Retrieves a specific quote.

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
api_instance = swagger_client.TradingAndConversionsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the quote you are retrieving.

try:
    # Read Quote
    api_response = api_instance.quote_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingAndConversionsApi->quote_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the quote you are retrieving. | 

### Return type

[**Quote**](Quote.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

