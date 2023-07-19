# swagger_client.ChannelsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_channel_get**](ChannelsApi.md#api_v2_channel_get) | **GET** /api/v2/channel | List Channels
[**api_v2_channel_payment_get**](ChannelsApi.md#api_v2_channel_payment_get) | **GET** /api/v2/channel/payment | List Channel Payments
[**api_v2_channel_payment_uuid_get**](ChannelsApi.md#api_v2_channel_payment_uuid_get) | **GET** /api/v2/channel/payment/{uuid} | Get Channel Payment
[**api_v2_channel_post**](ChannelsApi.md#api_v2_channel_post) | **POST** /api/v2/channel | Create Channel
[**api_v2_channel_uuid_get**](ChannelsApi.md#api_v2_channel_uuid_get) | **GET** /api/v2/channel/{uuid} | Get Channel

# **api_v2_channel_get**
> list[MerchantChannel] api_v2_channel_get(merchant_id, offset=offset, max=max, sort=sort, order=order)

List Channels

Retrieves all channels related to a Merchant ID.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
merchant_id = 'c02153ae-8ac8-4222-80e8-b2b2af85bd78' # str | The merchant ID that the channels belong to (default to c02153ae-8ac8-4222-80e8-b2b2af85bd78)
offset = 'offset_example' # str | Offset (optional)
max = 'max_example' # str | Maximum number of items in response (optional)
sort = swagger_client.PaymentStatusDto() # PaymentStatusDto | The attribute used to sort the data (optional)
order = 'order_example' # str | Ordering direction (optional)

try:
    # List Channels
    api_response = api_instance.api_v2_channel_get(merchant_id, offset=offset, max=max, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->api_v2_channel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The merchant ID that the channels belong to | [default to c02153ae-8ac8-4222-80e8-b2b2af85bd78]
 **offset** | **str**| Offset | [optional] 
 **max** | **str**| Maximum number of items in response | [optional] 
 **sort** | [**PaymentStatusDto**](.md)| The attribute used to sort the data | [optional] 
 **order** | **str**| Ordering direction | [optional] 

### Return type

[**list[MerchantChannel]**](MerchantChannel.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_channel_payment_get**
> list[MerchantChannelPayment] api_v2_channel_payment_get(merchant_id, status=status, from_date=from_date, to_date=to_date, offset=offset, max=max, order=order, q=q)

List Channel Payments

Retrieves a list of payments to a channel on a specific Merchant ID.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
merchant_id = 'c02153ae-8ac8-4222-80e8-b2b2af85bd78' # str | The Merchant ID (default to c02153ae-8ac8-4222-80e8-b2b2af85bd78)
status = 'status_example' # str |  (optional)
from_date = 'from_date_example' # str | From which date to start searching. (optional)
to_date = 'to_date_example' # str | At which date to stop searching. (optional)
offset = 'offset_example' # str | Where to start fetching records. (optional)
max = 'max_example' # str | Maximum number of items in response (optional)
order = 'order_example' # str | Ordering direction (optional)
q = 'q_example' # str | Can be UUID of the payment, reference, channel UUID, transaction hash, or wallet code. (optional)

try:
    # List Channel Payments
    api_response = api_instance.api_v2_channel_payment_get(merchant_id, status=status, from_date=from_date, to_date=to_date, offset=offset, max=max, order=order, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->api_v2_channel_payment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The Merchant ID | [default to c02153ae-8ac8-4222-80e8-b2b2af85bd78]
 **status** | **str**|  | [optional] 
 **from_date** | **str**| From which date to start searching. | [optional] 
 **to_date** | **str**| At which date to stop searching. | [optional] 
 **offset** | **str**| Where to start fetching records. | [optional] 
 **max** | **str**| Maximum number of items in response | [optional] 
 **order** | **str**| Ordering direction | [optional] 
 **q** | **str**| Can be UUID of the payment, reference, channel UUID, transaction hash, or wallet code. | [optional] 

### Return type

[**list[MerchantChannelPayment]**](MerchantChannelPayment.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_channel_payment_uuid_get**
> MerchantChannelPayment api_v2_channel_payment_uuid_get(uuid)

Get Channel Payment

Retrieves a specific payment made into a channel.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the payment you are querying.

try:
    # Get Channel Payment
    api_response = api_instance.api_v2_channel_payment_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->api_v2_channel_payment_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the payment you are querying. | 

### Return type

[**MerchantChannelPayment**](MerchantChannelPayment.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_channel_post**
> MerchantChannel api_v2_channel_post(body=body)

Create Channel

Creates a channel that your end users can openly send payments to.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MerchantChannelRequest() # MerchantChannelRequest |  (optional)

try:
    # Create Channel
    api_response = api_instance.api_v2_channel_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->api_v2_channel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantChannelRequest**](MerchantChannelRequest.md)|  | [optional] 

### Return type

[**MerchantChannel**](MerchantChannel.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_channel_uuid_get**
> MerchantChannel api_v2_channel_uuid_get(uuid)

Get Channel

Retrieves a specific channel by UUID.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID of the channel you are querying

try:
    # Get Channel
    api_response = api_instance.api_v2_channel_uuid_get(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->api_v2_channel_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID of the channel you are querying | 

### Return type

[**MerchantChannel**](MerchantChannel.md)

### Authorization

[Hawk](../README.md#Hawk)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

