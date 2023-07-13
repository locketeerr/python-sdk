# SummaryPaymentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | unique identifier for the merchant payment | [optional] 
**merchant_display_name** | **str** | display name for the merchant payment | [optional] 
**merchant_id** | **str** | Your Merchant ID. You can find it on the Merchant Details page in your account | [optional] 
**date_created** | **int** | Currently this is a long - can it be changed? Date and times are encoded into UNIX epoch timestamps | [optional] 
**expiry_date** | **int** | Date and times are encoded into UNIX epoch timestamps | [optional] 
**quote_expiry_date** | **int** | Date and times are encoded into UNIX epoch timestamps | [optional] 
**acceptance_expiry_date** | **int** | Date and times are encoded into UNIX epoch timestamps | [optional] 
**quote_status** | **str** |  | [optional] 
**reference** | **str** | Your payment reference ID. Feel free to submit any ID to tie the payment to your customer | [optional] 
**type** | [**DirectionDto**](DirectionDto.md) |  | [optional] 
**sub_type** | **str** | Payment sub type | [optional] [default to 'merchantPayIn']
**status** | [**PaymentStatusDto**](PaymentStatusDto.md) |  | [optional] 
**display_currency** | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**wallet_currency** | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**paid_currency** | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**fee_currency** | [**PayAmountsDto**](PayAmountsDto.md) |  | [optional] 
**display_rate** | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**exchange_rate** | [**ExchangeRateDto**](ExchangeRateDto.md) |  | [optional] 
**address** | [**CryptoAddressDto**](CryptoAddressDto.md) |  | [optional] 
**return_url** | **str** | URL that the customer will be redirected to if they click a \&quot;Back to Merchant\&quot; button on the payment web page | [optional] 
**redirect_url** | **str** | URL to the payment page that you can redirect your customers to | [optional] 
**transactions** | [**list[GatewayTransactionDto]**](GatewayTransactionDto.md) |  | [optional] 
**refund** | **object** | The payment this object is a refund of. This should reference the pay in that this refund was created for | [optional] 
**refunds** | **list[object]** | Refunds that have been requested for this payment. This should reference the refund payout for this pay in | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

