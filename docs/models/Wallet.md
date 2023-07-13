# openapi_client.model.wallet.Wallet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  |  | [optional] 
**[alternatives](#alternatives)** | list, tuple,  | tuple,  |  | [optional] 
**approxAvailable** | str,  | str,  |  | [optional] 
**approxBalance** | str,  | str,  |  | [optional] 
**available** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**balance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**convertedAvailable** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**currency** | [**Currency**](Currency.md) | [**Currency**](Currency.md) |  | [optional] 
**custodianWallet** | bool,  | BoolClass,  |  | [optional] 
**depositFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**description** | str,  | str,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**isEmoney** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**lookup** | str,  | str,  |  | [optional] 
**protocol** | str,  | str,  |  | [optional] 
**supportsDeposits** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**supportsThirdParty** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**supportsWithdrawals** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**withdrawalFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# alternatives

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

