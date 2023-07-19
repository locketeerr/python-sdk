# openapi_client.model.summary_payment_dto.SummaryPaymentDto

Contains all the information about a summary payment object

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains all the information about a summary payment object | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uuid** | str,  | str,  | unique identifier for the merchant payment | [optional] 
**merchantDisplayName** | str,  | str,  | display name for the merchant payment | [optional] 
**merchantId** | str,  | str,  | Your Merchant ID. You can find it on the Merchant Details page in your account | [optional] 
**dateCreated** | decimal.Decimal, int,  | decimal.Decimal,  | Currently this is a long - can it be changed? Date and times are encoded into UNIX epoch timestamps | [optional] value must be a 64 bit integer
**expiryDate** | decimal.Decimal, int,  | decimal.Decimal,  | Date and times are encoded into UNIX epoch timestamps | [optional] value must be a 64 bit integer
**quoteExpiryDate** | decimal.Decimal, int,  | decimal.Decimal,  | Date and times are encoded into UNIX epoch timestamps | [optional] value must be a 64 bit integer
**acceptanceExpiryDate** | decimal.Decimal, int,  | decimal.Decimal,  | Date and times are encoded into UNIX epoch timestamps | [optional] value must be a 64 bit integer
**quoteStatus** | str,  | str,  |  | [optional] 
**reference** | str,  | str,  | Your payment reference ID. Feel free to submit any ID to tie the payment to your customer | [optional] 
**type** | [**DirectionDto**](DirectionDto.md) | [**DirectionDto**](DirectionDto.md) |  | [optional] 
**subType** | str,  | str,  | Payment sub type | [optional] must be one of ["merchantPayIn", "merchantPayOut", "merchantRefund", ] if omitted the server will use the default value of "merchantPayIn"
**status** | [**PaymentStatusDto**](PaymentStatusDto.md) | [**PaymentStatusDto**](PaymentStatusDto.md) |  | [optional] 
**displayCurrency** | [**PayAmountsDto**](PayAmountsDto.md) | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**walletCurrency** | [**PayAmountsDto**](PayAmountsDto.md) | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**paidCurrency** | [**PayAmountsDto**](PayAmountsDto.md) | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**feeCurrency** | [**PayAmountsDto**](PayAmountsDto.md) | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**displayRate** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**exchangeRate** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**address** | [**CryptoAddressDto**](CryptoAddressDto.md) | [**CryptoAddressDto**](CryptoAddressDto.md) |  | [optional] 
**returnUrl** | str,  | str,  | URL that the customer will be redirected to if they click a \&quot;Back to Merchant\&quot; button on the payment web page | [optional] 
**redirectUrl** | str,  | str,  | URL to the payment page that you can redirect your customers to | [optional] 
**[transactions](#transactions)** | list, tuple,  | tuple,  |  | [optional] 
**[refund](#refund)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The payment this object is a refund of. This should reference the pay in that this refund was created for | [optional] 
**[refunds](#refunds)** | list, tuple,  | tuple,  | Refunds that have been requested for this payment. This should reference the refund payout for this pay in | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GatewayTransactionDto**](GatewayTransactionDto.md) | [**GatewayTransactionDto**](GatewayTransactionDto.md) | [**GatewayTransactionDto**](GatewayTransactionDto.md) |  | 

# refund

The payment this object is a refund of. This should reference the pay in that this refund was created for

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payment this object is a refund of. This should reference the pay in that this refund was created for | 

# refunds

Refunds that have been requested for this payment. This should reference the refund payout for this pay in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Refunds that have been requested for this payment. This should reference the refund payout for this pay in | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

