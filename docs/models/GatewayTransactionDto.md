# openapi_client.model.gateway_transaction_dto.GatewayTransactionDto

Specify details about transaction (onchain or offchain) linked to the payment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specify details about transaction (onchain or offchain) linked to the payment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dateCreated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**dateConfirmed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**hash** | str,  | str,  | Transaction hash | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | payment amount | [optional] 
**[risk](#risk)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**networkFeeCurrency** | str,  | str,  | currency acronym | [optional] 
**networkFeeAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | payment amount | [optional] 
**[sources](#sources)** | list, tuple,  | tuple,  | list of source addresses (only applicable if payment in) | [optional] 
**displayRate** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**exchangeRate** | [**ExchangeRateDto**](ExchangeRateDto.md) | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# risk

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# sources

list of source addresses (only applicable if payment in)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | list of source addresses (only applicable if payment in) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

