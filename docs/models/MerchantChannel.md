# openapi_client.model.merchant_channel.MerchantChannel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**dateCreated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**lastUpdated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**merchantId** | str,  | str,  |  | [optional] 
**walletCurrency** | str,  | str,  |  | [optional] 
**displayCurrency** | str,  | str,  |  | [optional] 
**payCurrency** | str,  | str,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**tag** | str,  | str,  |  | [optional] 
**protocol** | str,  | str,  |  | [optional] 
**reference** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["OPEN", "CLOSED", ] 
**uuid** | str,  | str,  |  | [optional] 
**redirectUrl** | str,  | str,  |  | [optional] 
**uri** | str,  | str,  |  | [optional] 
**[alternatives](#alternatives)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# alternatives

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AlternativeAddress**](AlternativeAddress.md) | [**AlternativeAddress**](AlternativeAddress.md) | [**AlternativeAddress**](AlternativeAddress.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

