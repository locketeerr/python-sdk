# PayRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Your Merchant ID. You can find it on the Merchant Details page in your account | [default to '5C8D8D78-366A-4AFB-B658-A64CE543C5DB']
**amount** | **float** | payment amount | [default to 223.05]
**expiry_minutes** | **int** | time period after which payment expires | [optional] [default to 20]
**currency** | **str** | currency acronym | [default to 'EUR']
**return_url** | **str** | URL that the customer will be redirected to if they click a &#x27;Back to Merchant&#x27; button on the payment web page | [optional] [default to 'https://my-shop.com/payment-complete?ref=xyz']
**reference** | **str** | Your payment reference ID. Feel free to submit any ID to tie the payment to your customer | [default to 'myUniqueRef333']
**type** | [**DirectionDto**](DirectionDto.md) |  | 
**pay_in_details** | [**PayInDetailDto**](PayInDetailDto.md) |  | [optional] 
**pay_out_details** | [**PayOutDetailDto**](PayOutDetailDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

