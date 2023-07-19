# openapi_client.model.currency_fiat.CurrencyFiat

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**depositFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**fiat** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**icon** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**name** | str,  | str,  |  | [optional] 
**[options](#options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**pricePrecision** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 2value must be a 32 bit integer
**[protocols](#protocols)** | list, tuple,  | tuple,  |  | [optional] 
**quantityPrecision** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 2value must be a 32 bit integer
**supportsDeposits** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**supportsWithdrawals** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**withdrawalFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[withdrawalParameters](#withdrawalParameters)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# withdrawalParameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

