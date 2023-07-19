<a id="__pageTop"></a>
# openapi_client.apis.tags.merchant_ids_api.MerchantIDsApi

All URIs are relative to *https://api.sandbox.bvnk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_id_create**](#merchant_id_create) | **post** /api/v1/merchant | Create Merchant ID
[**merchant_id_list**](#merchant_id_list) | **get** /api/v1/merchant | List Merchant IDs

# **merchant_id_create**
<a id="merchant_id_create"></a>
> SummaryPaymentDto merchant_id_create()

Create Merchant ID

Generate a Merchant ID for your account to process pay-ins and pay-outs through our API.  A Merchant ID is essential as it designates the account wallet where incoming pay-ins will be settled. For instance, if a Merchant ID is associated with a EUR wallet ID, any incoming USDT payment will be automatically converted to EUR and deposited in the designated EUR wallet.  Vice versa, any outgoing USDT payment will be automatically converted and withdrawn from the designated EUR wallet.  For further information, please visit https://docs.bvnk.com/docs/creating-your-first-merchant to learn more about creating your first Merchant ID.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import merchant_ids_api
from openapi_client.model.summary_payment_dto import SummaryPaymentDto
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
    api_instance = merchant_ids_api.MerchantIDsApi(api_client)

    # example passing only optional values
    body = dict(
        display_name="Test Merchant Name",
        webhook_url="https://www.URL.com/to/send/webhooks/to",
        wallet=dict(
            id="501098",
        ),
    )
    try:
        # Create Merchant ID
        api_response = api_instance.merchant_id_create(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MerchantIDsApi->merchant_id_create: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[wallet](#wallet)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**displayName** | str,  | str,  | The name of the merchant that will be displayed on the payments page | if omitted the server will use the default value of "Test Merchant Name"
**webhookUrl** | str,  | str,  | The URL that will recieve the webhooks | [optional] if omitted the server will use the default value of "https://www.URL.com/to/send/webhooks/to"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# wallet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The ID of the wallet to link to the merchant ID | [optional] if omitted the server will use the default value of "501098"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#merchant_id_create.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#merchant_id_create.ApiResponseFor400) | Bad Request

#### merchant_id_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SummaryPaymentDto**](../../models/SummaryPaymentDto.md) |  | 


#### merchant_id_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **merchant_id_list**
<a id="merchant_id_list"></a>
> [Merchant] merchant_id_list()

List Merchant IDs

Retrieves merchant IDs setup on your account.

### Example

* Api Key Authentication (Hawk):
```python
import openapi_client
from openapi_client.apis.tags import merchant_ids_api
from openapi_client.model.merchant import Merchant
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
    api_instance = merchant_ids_api.MerchantIDsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Merchant IDs
        api_response = api_instance.merchant_id_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MerchantIDsApi->merchant_id_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#merchant_id_list.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#merchant_id_list.ApiResponseFor400) | Bad Request

#### merchant_id_list.ApiResponseFor200
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

#### merchant_id_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Hawk](../../../README.md#Hawk)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

