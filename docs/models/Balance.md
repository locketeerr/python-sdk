# openapi_client.model.balance.Balance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) | [**Currency**](Currency.md) |  | [optional] 
**walletId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**available** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**reserved** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**convertedAvailable** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**convertedReserved** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**total** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

