# openapi_client.model.pay_amounts_dto.PayAmountsDto

Contains the type of currency, and amount to be paid and received

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains the type of currency, and amount to be paid and received | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currency** | str,  | str,  | currency acronym | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | amount to be paid | [optional] 
**actual** | decimal.Decimal, int, float,  | decimal.Decimal,  | actual amount paid/ received | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

