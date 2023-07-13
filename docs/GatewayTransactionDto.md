# GatewayTransactionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **int** |  | [optional] 
**date_confirmed** | **int** |  | [optional] 
**hash** | **str** | Transaction hash | [optional] 
**amount** | **float** | payment amount | [optional] 
**risk** | **object** |  | [optional] 
**network_fee_currency** | **str** | currency acronym | [optional] 
**network_fee_amount** | **float** | payment amount | [optional] 
**sources** | **list[str]** | list of source addresses (only applicable if payment in) | [optional] 
**display_rate** | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**exchange_rate** | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

