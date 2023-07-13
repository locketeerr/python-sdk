# openapi_client.model.crypto_address_dto.CryptoAddressDto

Payment address details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payment address details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  | Address to withdrawal funds to | [optional] 
**tag** | str,  | str,  | This is a payment destination tag. This fields isn&#x27;t null when the paidCurrency.currency value is XRP | [optional] 
**protocol** | str,  | str,  | protocol behind a currency (ERC20 or TRC20) | [optional] 
**uri** | str,  | str,  | The destination address URI for QR code | [optional] 
**[alternatives](#alternatives)** | list, tuple,  | tuple,  | List of non-default addresses for other tokens | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# alternatives

List of non-default addresses for other tokens

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of non-default addresses for other tokens | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AlternativeAddress**](AlternativeAddress.md) | [**AlternativeAddress**](AlternativeAddress.md) | [**AlternativeAddress**](AlternativeAddress.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

