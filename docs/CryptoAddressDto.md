# CryptoAddressDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address to withdrawal funds to | [optional] 
**tag** | **str** | This is a payment destination tag. This fields isn&#x27;t null when the paidCurrency.currency value is XRP | [optional] 
**protocol** | **str** | protocol behind a currency (ERC20 or TRC20) | [optional] 
**uri** | **str** | The destination address URI for QR code | [optional] 
**alternatives** | [**list[AlternativeAddress]**](AlternativeAddress.md) | List of non-default addresses for other tokens | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

