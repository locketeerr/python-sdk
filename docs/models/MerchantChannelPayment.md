# openapi_client.model.merchant_channel_payment.MerchantChannelPayment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**channelId** | str,  | str,  |  | [optional] 
**merchantId** | str,  | str,  |  | [optional] 
**merchantDisplayName** | str,  | str,  |  | [optional] 
**reference** | str,  | str,  |  | [optional] 
**dateCreated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 64 bit integer
**lastUpdated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0value must be a 64 bit integer
**status** | str,  | str,  |  | [optional] must be one of ["DETECTED", "COMPLETE", "UNKNOWN", ] 
**uuid** | str,  | str,  |  | [optional] 
**hash** | str,  | str,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**tag** | str,  | str,  |  | [optional] 
**paidCurrency** | str,  | str,  |  | [optional] 
**displayCurrency** | str,  | str,  |  | [optional] 
**walletCurrency** | str,  | str,  |  | [optional] 
**feeCurrency** | str,  | str,  |  | [optional] 
**paidAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**displayAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**walletAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**feeAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**exchangeRate** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**displayRate** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**risk** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**[sources](#sources)** | list, tuple,  | tuple,  |  | [optional] 
**networkFee** | [**NetworkFee**](NetworkFee.md) | [**NetworkFee**](NetworkFee.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

