# openapi_client.model.quote_request.QuoteRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fromWallet** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 3598236
**payInMethod** | str,  | str,  |  | if omitted the server will use the default value of "wallet"
**useMinimum** | bool,  | BoolClass,  |  | if omitted the server will use the default value of False
**amountIn** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10
**from** | str,  | str,  |  | if omitted the server will use the default value of "EUR"
**to** | str,  | str,  |  | if omitted the server will use the default value of "USDC"
**payOutMethod** | str,  | str,  |  | if omitted the server will use the default value of "wallet"
**useMaximum** | bool,  | BoolClass,  |  | if omitted the server will use the default value of False
**toWallet** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 3598514
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

