# swagger_client.PaymentsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_pay_summary_get**](PaymentsApi.md#api_v1_pay_summary_get) | **GET** /api/v1/pay/summary | List Payments
[**api_v1_pay_summary_post**](PaymentsApi.md#api_v1_pay_summary_post) | **POST** /api/v1/pay/summary | Create payment
[**api_v1_pay_uuid_summary_get**](PaymentsApi.md#api_v1_pay_uuid_summary_get) | **GET** /api/v1/pay/{uuid}/summary | Get Payment
[**api_v1_pay_validate_put**](PaymentsApi.md#api_v1_pay_validate_put) | **PUT** /api/v1/pay/validate | Validate Address

# **api_v1_pay_summary_get**
> list[SummaryPaymentDto] api_v1_pay_summary_get(merchant_id, customer_reference=customer_reference, payment_external_id=payment_external_id, from_date=from_date, to_date=to_date, offset=offset, max=max, status=status, order=order)

List Payments

Retrieves a list of payments on a specific Merchant ID

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
merchant_id = '5C8D8D78-366A-4AFB-B658-A64CE543C5DB' # str | Merchant identifier (default to 5C8D8D78-366A-4AFB-B658-A64CE543C5DB)
customer_reference = 'customer_reference_example' # str | Customer reference (optional)
payment_external_id = 'payment_external_id_example' # str | Merchant payment uuid (optional)
from_date = 'from_date_example' # str | Start date (optional)
to_date = 'to_date_example' # str | End date (optional)
offset = 1.2 # float | Offset (optional)
max = 1.2 # float | Maximum number of items in response (optional)
status = swagger_client.PaymentStatusDto() # PaymentStatusDto |  (optional)
order = 'order_example' # str | Ordering direction (optional)

try:
    # List Payments
    api_response = api_instance.api_v1_pay_summary_get(merchant_id, customer_reference=customer_reference, payment_external_id=payment_external_id, from_date=from_date, to_date=to_date, offset=offset, max=max, status=status, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->api_v1_pay_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Merchant identifier | [default to 5C8D8D78-366A-4AFB-B658-A64CE543C5DB]
 **customer_reference** | **str**| Customer reference | [optional] 
 **payment_external_id** | **str**| Merchant payment uuid | [optional] 
 **from_date** | **str**| Start date | [optional] 
 **to_date** | **str**| End date | [optional] 
 **offset** | **float**| Offset | [optional] 
 **max** | **float**| Maximum number of items in response | [optional] 
 **status** | [**PaymentStatusDto**](.md)|  | [optional] 
 **order** | **str**| Ordering direction | [optional] 

### Return type

[**list[SummaryPaymentDto]**](SummaryPaymentDto.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_pay_summary_post**
> SummaryPaymentDto api_v1_pay_summary_post(body)

Create payment

Creates a payment, either type IN or type OUT.

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PayRequestDto() # PayRequestDto | 

try:
    # Create payment
    api_response = api_instance.api_v1_pay_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->api_v1_pay_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayRequestDto**](PayRequestDto.md)|  | 

### Return type

[**SummaryPaymentDto**](SummaryPaymentDto.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_pay_uuid_summary_get**
> SummaryPaymentDto api_v1_pay_uuid_summary_get(uuid)

Get Payment

Retrieves details of a specific payment using the UUID of the payment.

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | merchant payment uuid

try:
    # Get Payment
    api_response = api_instance.api_v1_pay_uuid_summary_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->api_v1_pay_uuid_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| merchant payment uuid | 

### Return type

[**SummaryPaymentDto**](SummaryPaymentDto.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_pay_validate_put**
> api_v1_pay_validate_put(body)

Validate Address

Validates that a crypto address is correct.  Use this endpoint to validate that an address exists, is correctly formatted, and includes all the required data. This endpoint can help prevent your end users losing funds when submitting a payout.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
body = swagger_client.PayOutDetailDto() # PayOutDetailDto | 

try:
    # Validate Address
    api_instance.api_v1_pay_validate_put(body)
except ApiException as e:
    print("Exception when calling PaymentsApi->api_v1_pay_validate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayOutDetailDto**](PayOutDetailDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

