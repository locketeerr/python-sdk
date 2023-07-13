# openapi_client.model.merchant_channel_request.MerchantChannelRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | An external reference for the channel that your customer will see. | if omitted the server will use the default value of "c1b933d5-3354-4f83-a05f-0b53f1be85f2"
**merchantId** | str,  | str,  | The merchant ID that you are creating the channel on. | if omitted the server will use the default value of "0a12a214-1619-43fa-9be1-0029f6a440a0"
**payCurrency** | str,  | str,  | Cryptocurrency code that the channel will operate on. | if omitted the server will use the default value of "ETH"
**displayCurrency** | str,  | str,  | The currency which pricing will be displayed to the end user in (can be the same as payCurrency, or can be different). | if omitted the server will use the default value of "EUR"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

