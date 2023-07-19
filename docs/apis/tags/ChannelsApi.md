<a id="__pageTop"></a>
# openapi_client.apis.tags.channels_api.ChannelsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_channel_get**](#api_v2_channel_get) | **get** /api/v2/channel | List Channels
[**api_v2_channel_payment_get**](#api_v2_channel_payment_get) | **get** /api/v2/channel/payment | List Channel Payments
[**api_v2_channel_payment_uuid_get**](#api_v2_channel_payment_uuid_get) | **get** /api/v2/channel/payment/{uuid} | Get Channel Payment
[**api_v2_channel_post**](#api_v2_channel_post) | **post** /api/v2/channel | Create Channel
[**api_v2_channel_uuid_get**](#api_v2_channel_uuid_get) | **get** /api/v2/channel/{uuid} | Get Channel

# **api_v2_channel_get**
<a id="api_v2_channel_get"></a>
> [MerchantChannel] api_v2_channel_get()

List Channels

Retrieves all channels related to a Merchant ID.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import channels_api
from openapi_client.model.payment_status_dto import PaymentStatusDto
from openapi_client.model.merchant_channel import MerchantChannel
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
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
    api_instance = channels_api.ChannelsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'merchantId': "c02153ae-8ac8-4222-80e8-b2b2af85bd78",
    }
    try:
        # List Channels
        api_response = api_instance.api_v2_channel_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'merchantId': "c02153ae-8ac8-4222-80e8-b2b2af85bd78",
        'offset': "0",
        'max': "10",
        'sort': PaymentStatusDto("PENDING"),
        'order': "asc",
    }
    try:
        # List Channels
        api_response = api_instance.api_v2_channel_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_get: %s\n" % e)
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
merchantId | MerchantIdSchema | | 
offset | OffsetSchema | | optional
max | MaxSchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional


# MerchantIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "c02153ae-8ac8-4222-80e8-b2b2af85bd78"

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentStatusDto**](../../models/PaymentStatusDto.md) |  | 


# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v2_channel_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#api_v2_channel_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#api_v2_channel_get.ApiResponseFor500) | Unexpected Error

#### api_v2_channel_get.ApiResponseFor200
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
[**MerchantChannel**]({{complexTypePrefix}}MerchantChannel.md) | [**MerchantChannel**]({{complexTypePrefix}}MerchantChannel.md) | [**MerchantChannel**]({{complexTypePrefix}}MerchantChannel.md) |  | 

#### api_v2_channel_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v2_channel_get.ApiResponseFor500
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

# **api_v2_channel_payment_get**
<a id="api_v2_channel_payment_get"></a>
> [MerchantChannelPayment] api_v2_channel_payment_get()

List Channel Payments

Retrieves a list of payments to a channel on a specific Merchant ID.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import channels_api
from openapi_client.model.merchant_channel_payment import MerchantChannelPayment
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
    api_instance = channels_api.ChannelsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'merchantId': "c02153ae-8ac8-4222-80e8-b2b2af85bd78",
    }
    try:
        # List Channel Payments
        api_response = api_instance.api_v2_channel_payment_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_payment_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'merchantId': "c02153ae-8ac8-4222-80e8-b2b2af85bd78",
        'status': "COMPLETE",
        'fromDate': "2023-03-05",
        'toDate': "2023-05-03",
        'offset': "0",
        'max': "10",
        'order': "asc",
        'q': "q_example",
    }
    try:
        # List Channel Payments
        api_response = api_instance.api_v2_channel_payment_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_payment_get: %s\n" % e)
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
merchantId | MerchantIdSchema | | 
status | StatusSchema | | optional
fromDate | FromDateSchema | | optional
toDate | ToDateSchema | | optional
offset | OffsetSchema | | optional
max | MaxSchema | | optional
order | OrderSchema | | optional
q | QSchema | | optional


# MerchantIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "c02153ae-8ac8-4222-80e8-b2b2af85bd78"

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["DETECTED", "COMPLETE", "UNKNOWN", ] 

# FromDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v2_channel_payment_get.ApiResponseFor200) | OK

#### api_v2_channel_payment_get.ApiResponseFor200
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
[**MerchantChannelPayment**]({{complexTypePrefix}}MerchantChannelPayment.md) | [**MerchantChannelPayment**]({{complexTypePrefix}}MerchantChannelPayment.md) | [**MerchantChannelPayment**]({{complexTypePrefix}}MerchantChannelPayment.md) |  | 

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_v2_channel_payment_uuid_get**
<a id="api_v2_channel_payment_uuid_get"></a>
> MerchantChannelPayment api_v2_channel_payment_uuid_get()

Get Channel Payment

Retrieves a specific payment made into a channel.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import channels_api
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
from openapi_client.model.merchant_channel_payment import MerchantChannelPayment
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
    api_instance = channels_api.ChannelsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "c0dc9c14-0312-4a6b-a1a3-a6dcebdcc8a4",
    }
    try:
        # Get Channel Payment
        api_response = api_instance.api_v2_channel_payment_uuid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_payment_uuid_get: %s\n" % e)
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
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "c0dc9c14-0312-4a6b-a1a3-a6dcebdcc8a4"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v2_channel_payment_uuid_get.ApiResponseFor200) | 200
400 | [ApiResponseFor400](#api_v2_channel_payment_uuid_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_v2_channel_payment_uuid_get.ApiResponseFor404) | Not Found

#### api_v2_channel_payment_uuid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MerchantChannelPayment**](../../models/MerchantChannelPayment.md) |  | 


#### api_v2_channel_payment_uuid_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v2_channel_payment_uuid_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_v2_channel_post**
<a id="api_v2_channel_post"></a>
> MerchantChannel api_v2_channel_post()

Create Channel

Creates a channel that your end users can openly send payments to.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import channels_api
from openapi_client.model.merchant_channel_request import MerchantChannelRequest
from openapi_client.model.merchant_channel import MerchantChannel
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
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
    api_instance = channels_api.ChannelsApi(api_client)

    # example passing only optional values
    body = MerchantChannelRequest(
        merchant_id="0a12a214-1619-43fa-9be1-0029f6a440a0",
        pay_currency="ETH",
        display_currency="EUR",
        reference="c1b933d5-3354-4f83-a05f-0b53f1be85f2",
    )
    try:
        # Create Channel
        api_response = api_instance.api_v2_channel_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_post: %s\n" % e)
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
[**MerchantChannelRequest**](../../models/MerchantChannelRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#api_v2_channel_post.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#api_v2_channel_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#api_v2_channel_post.ApiResponseFor500) | Unexpected Error

#### api_v2_channel_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MerchantChannel**](../../models/MerchantChannel.md) |  | 


#### api_v2_channel_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v2_channel_post.ApiResponseFor500
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

# **api_v2_channel_uuid_get**
<a id="api_v2_channel_uuid_get"></a>
> MerchantChannel api_v2_channel_uuid_get()

Get Channel

Retrieves a specific channel by UUID.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import channels_api
from openapi_client.model.merchant_channel import MerchantChannel
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
    api_instance = channels_api.ChannelsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "9d1f67f2-a647-404b-9b02-247c77be81d0",
    }
    try:
        # Get Channel
        api_response = api_instance.api_v2_channel_uuid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->api_v2_channel_uuid_get: %s\n" % e)
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
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "9d1f67f2-a647-404b-9b02-247c77be81d0"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v2_channel_uuid_get.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#api_v2_channel_uuid_get.ApiResponseFor404) | Not Found

#### api_v2_channel_uuid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MerchantChannel**](../../models/MerchantChannel.md) |  | 


#### api_v2_channel_uuid_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

