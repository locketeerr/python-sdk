# openapi_client.model.pay_request_dto.PayRequestDto

DTO required to create a payment in or a payment out

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DTO required to create a payment in or a payment out | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | Your payment reference ID. Feel free to submit any ID to tie the payment to your customer | if omitted the server will use the default value of "myUniqueRef333"
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | payment amount | if omitted the server will use the default value of 223.05
**merchantId** | str,  | str,  | Your Merchant ID. You can find it on the Merchant Details page in your account | if omitted the server will use the default value of "5C8D8D78-366A-4AFB-B658-A64CE543C5DB"
**currency** | str,  | str,  | currency acronym | if omitted the server will use the default value of "EUR"
**type** | [**DirectionDto**](DirectionDto.md) | [**DirectionDto**](DirectionDto.md) |  | 
**expiryMinutes** | decimal.Decimal, int,  | decimal.Decimal,  | time period after which payment expires | [optional] if omitted the server will use the default value of 20
**returnUrl** | str,  | str,  | URL that the customer will be redirected to if they click a &#x27;Back to Merchant&#x27; button on the payment web page | [optional] if omitted the server will use the default value of "https://my-shop.com/payment-complete?ref=xyz"
**payInDetails** | [**PayInDetailDto**](PayInDetailDto.md) | [**PayInDetailDto**](PayInDetailDto.md) |  | [optional] 
**payOutDetails** | [**PayOutDetailDto**](PayOutDetailDto.md) | [**PayOutDetailDto**](PayOutDetailDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

