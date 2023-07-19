# swagger_client.MerchantIDsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_id_create**](MerchantIDsApi.md#merchant_id_create) | **POST** /api/v1/merchant | Create Merchant ID
[**merchant_id_list**](MerchantIDsApi.md#merchant_id_list) | **GET** /api/v1/merchant | List Merchant IDs

# **merchant_id_create**
> SummaryPaymentDto merchant_id_create(body=body)

Create Merchant ID

Generate a Merchant ID for your account to process pay-ins and pay-outs through our API.  A Merchant ID is essential as it designates the account wallet where incoming pay-ins will be settled. For instance, if a Merchant ID is associated with a EUR wallet ID, any incoming USDT payment will be automatically converted to EUR and deposited in the designated EUR wallet.  Vice versa, any outgoing USDT payment will be automatically converted and withdrawn from the designated EUR wallet.  For further information, please visit https://docs.bvnk.com/docs/creating-your-first-merchant to learn more about creating your first Merchant ID.

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
api_instance = swagger_client.MerchantIDsApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1MerchantBody() # V1MerchantBody |  (optional)

try:
    # Create Merchant ID
    api_response = api_instance.merchant_id_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantIDsApi->merchant_id_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MerchantBody**](V1MerchantBody.md)|  | [optional] 

### Return type

[**SummaryPaymentDto**](SummaryPaymentDto.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_id_list**
> list[Merchant] merchant_id_list()

List Merchant IDs

Retrieves merchant IDs setup on your account.

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
api_instance = swagger_client.MerchantIDsApi(swagger_client.ApiClient(configuration))

try:
    # List Merchant IDs
    api_response = api_instance.merchant_id_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantIDsApi->merchant_id_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Merchant]**](Merchant.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

