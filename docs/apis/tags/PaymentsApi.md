<a id="__pageTop"></a>
# openapi_client.apis.tags.payments_api.PaymentsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_pay_summary_get**](#api_v1_pay_summary_get) | **get** /api/v1/pay/summary | List Payments
[**api_v1_pay_summary_post**](#api_v1_pay_summary_post) | **post** /api/v1/pay/summary | Create payment
[**api_v1_pay_uuid_summary_get**](#api_v1_pay_uuid_summary_get) | **get** /api/v1/pay/{uuid}/summary | Get Payment
[**api_v1_pay_validate_put**](#api_v1_pay_validate_put) | **put** /api/v1/pay/validate | Validate Address

# **api_v1_pay_summary_get**
<a id="api_v1_pay_summary_get"></a>
> [SummaryPaymentDto] api_v1_pay_summary_get()

List Payments

Retrieves a list of payments on a specific Merchant ID

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import payments_api
from openapi_client.model.payment_status_dto import PaymentStatusDto
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
from openapi_client.model.summary_payment_dto import SummaryPaymentDto
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
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'merchantId': "5C8D8D78-366A-4AFB-B658-A64CE543C5DB",
    }
    try:
        # List Payments
        api_response = api_instance.api_v1_pay_summary_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->api_v1_pay_summary_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'merchantId': "5C8D8D78-366A-4AFB-B658-A64CE543C5DB",
        'customerReference': "REF123",
        'paymentExternalId': "5C8D8D78-366A-4AFB-B658-A64CE543C5DB",
        'fromDate': "2023-03-30",
        'toDate': "2023-03-30",
        'offset': 0,
        'max': 20,
        'status': PaymentStatusDto("PENDING"),
        'order': "asc",
    }
    try:
        # List Payments
        api_response = api_instance.api_v1_pay_summary_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->api_v1_pay_summary_get: %s\n" % e)
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
customerReference | CustomerReferenceSchema | | optional
paymentExternalId | PaymentExternalIdSchema | | optional
fromDate | FromDateSchema | | optional
toDate | ToDateSchema | | optional
offset | OffsetSchema | | optional
max | MaxSchema | | optional
status | StatusSchema | | optional
order | OrderSchema | | optional


# MerchantIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "5C8D8D78-366A-4AFB-B658-A64CE543C5DB"

# CustomerReferenceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaymentExternalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# StatusSchema
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
200 | [ApiResponseFor200](#api_v1_pay_summary_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#api_v1_pay_summary_get.ApiResponseFor400) | Bad request
500 | [ApiResponseFor500](#api_v1_pay_summary_get.ApiResponseFor500) | Unexpected Error

#### api_v1_pay_summary_get.ApiResponseFor200
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
[**SummaryPaymentDto**]({{complexTypePrefix}}SummaryPaymentDto.md) | [**SummaryPaymentDto**]({{complexTypePrefix}}SummaryPaymentDto.md) | [**SummaryPaymentDto**]({{complexTypePrefix}}SummaryPaymentDto.md) |  | 

#### api_v1_pay_summary_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v1_pay_summary_get.ApiResponseFor500
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

# **api_v1_pay_summary_post**
<a id="api_v1_pay_summary_post"></a>
> SummaryPaymentDto api_v1_pay_summary_post(pay_request_dto)

Create payment

Creates a payment, either type IN or type OUT.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import payments_api
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
from openapi_client.model.pay_request_dto import PayRequestDto
from openapi_client.model.summary_payment_dto import SummaryPaymentDto
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
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    body = PayRequestDto(
        merchant_id="5C8D8D78-366A-4AFB-B658-A64CE543C5DB",
        amount=223.05,
        expiry_minutes=20,
        currency="EUR",
        return_url="https://my-shop.com/payment-complete?ref=xyz",
        reference="myUniqueRef333",
        type=DirectionDto("IN"),
        pay_in_details=PayInDetailDto(
            currency="ETH",
        ),
        pay_out_details=PayOutDetailDto(
            code="crypto",
            currency="ETH",
            address="0xb794f5ea0ba39494ce839613fffba74279579268",
            tag="",
            protocol="ERC20",
        ),
    )
    try:
        # Create payment
        api_response = api_instance.api_v1_pay_summary_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->api_v1_pay_summary_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PayRequestDto**](../../models/PayRequestDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v1_pay_summary_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#api_v1_pay_summary_post.ApiResponseFor400) | Bad request
500 | [ApiResponseFor500](#api_v1_pay_summary_post.ApiResponseFor500) | Unexpected Error

#### api_v1_pay_summary_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SummaryPaymentDto**](../../models/SummaryPaymentDto.md) |  | 


#### api_v1_pay_summary_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v1_pay_summary_post.ApiResponseFor500
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

# **api_v1_pay_uuid_summary_get**
<a id="api_v1_pay_uuid_summary_get"></a>
> SummaryPaymentDto api_v1_pay_uuid_summary_get()

Get Payment

Retrieves details of a specific payment using the UUID of the payment.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import payments_api
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
from openapi_client.model.summary_payment_dto import SummaryPaymentDto
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
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "5C8D8D78-366A-4AFB-B658-A64CE543C5DB",
    }
    try:
        # Get Payment
        api_response = api_instance.api_v1_pay_uuid_summary_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->api_v1_pay_uuid_summary_get: %s\n" % e)
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
str,  | str,  |  | if omitted the server will use the default value of "5C8D8D78-366A-4AFB-B658-A64CE543C5DB"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v1_pay_uuid_summary_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#api_v1_pay_uuid_summary_get.ApiResponseFor400) | Bad request
500 | [ApiResponseFor500](#api_v1_pay_uuid_summary_get.ApiResponseFor500) | Unexpected Error

#### api_v1_pay_uuid_summary_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SummaryPaymentDto**](../../models/SummaryPaymentDto.md) |  | 


#### api_v1_pay_uuid_summary_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v1_pay_uuid_summary_get.ApiResponseFor500
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

# **api_v1_pay_validate_put**
<a id="api_v1_pay_validate_put"></a>
> api_v1_pay_validate_put(pay_out_detail_dto)

Validate Address

Validates that a crypto address is correct.  Use this endpoint to validate that an address exists, is correctly formatted, and includes all the required data. This endpoint can help prevent your end users losing funds when submitting a payout.

### Example

```python
import openapi_client
from openapi_client.apis.tags import payments_api
from openapi_client.model.client_validation_error_dto import ClientValidationErrorDto
from openapi_client.model.pay_out_detail_dto import PayOutDetailDto
from openapi_client.model.server_error_dto import ServerErrorDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.bvnk.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.sandbox.bvnk.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    body = PayOutDetailDto(
        code="crypto",
        currency="ETH",
        address="0xb794f5ea0ba39494ce839613fffba74279579268",
        tag="",
        protocol="ERC20",
    )
    try:
        # Validate Address
        api_response = api_instance.api_v1_pay_validate_put(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->api_v1_pay_validate_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PayOutDetailDto**](../../models/PayOutDetailDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_v1_pay_validate_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#api_v1_pay_validate_put.ApiResponseFor400) | Bad request
500 | [ApiResponseFor500](#api_v1_pay_validate_put.ApiResponseFor500) | Unexpected Error

#### api_v1_pay_validate_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_v1_pay_validate_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClientValidationErrorDto**](../../models/ClientValidationErrorDto.md) |  | 


#### api_v1_pay_validate_put.ApiResponseFor500
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

