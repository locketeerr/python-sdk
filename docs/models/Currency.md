# openapi_client.model.currency.Currency

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**depositFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**fiat** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**icon** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**name** | str,  | str,  |  | [optional] 
**options** | [**CurrencyOptions**](CurrencyOptions.md) | [**CurrencyOptions**](CurrencyOptions.md) |  | [optional] 
**pricePrecision** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 5value must be a 32 bit integer
**[protocols](#protocols)** | list, tuple,  | tuple,  |  | [optional] 
**quantityPrecision** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 5value must be a 32 bit integer
**supportsDeposits** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**supportsWithdrawals** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**withdrawalFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[withdrawalParameters](#withdrawalParameters)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CurrencyProtocol**](CurrencyProtocol.md) | [**CurrencyProtocol**](CurrencyProtocol.md) | [**CurrencyProtocol**](CurrencyProtocol.md) |  | 

# withdrawalParameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExternalCurrencyWithdrawalParameter**](ExternalCurrencyWithdrawalParameter.md) | [**ExternalCurrencyWithdrawalParameter**](ExternalCurrencyWithdrawalParameter.md) | [**ExternalCurrencyWithdrawalParameter**](ExternalCurrencyWithdrawalParameter.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

