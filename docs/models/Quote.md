# openapi_client.model.quote.Quote

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**amountIn** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**amountDue** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**amountOut** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**quoteStatus** | str,  | str,  |  | [optional] must be one of ["ESTIMATE", "TEMPLATE", "PENDING", "ACCEPTED", "PAYMENT_IN_RECEIVED", "PAYMENT_IN_SEEN", "PAYMENT_IN_FAILED", "FRAUD_CHECK_PENDING", "FRAUD_CHECK_FAILED", "PAYMENT_OUT_PENDING", "PAYMENT_OUT_PROCESSED", "PAYMENT_OUT_USED", "COMPLETED", "CONVERSION_FAILED", "PAYMENT_OUT_FAILED", "LOCKED", "REFUNDED", ] 
**paymentStatus** | str,  | str,  |  | [optional] must be one of ["PENDING", "SEEN", "SUCCESS", "CANCELLED", "FAILED", "FRAUD_PENDING", "FRAUD_PENDING_MANUAL_REVIEW", "FRAUD_FAILED", "REFUND_PENDING", "REFUNDED", "MANUAL_SUCCESS", "REFUND_FAILED", ] 
**acceptanceExpiryDate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**acceptanceDate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**paymentExpiryDate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**paymentReceiptDate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[payInLegs](#payInLegs)** | list, tuple,  | tuple,  |  | [optional] 
**payInMethod** | [**PayInMethod**](PayInMethod.md) | [**PayInMethod**](PayInMethod.md) |  | [optional] 
**payOutMethod** | [**PayOutMethod**](PayOutMethod.md) | [**PayOutMethod**](PayOutMethod.md) |  | [optional] 
**uuid** | str,  | str,  |  | [optional] 
**payOutInstruction** | [**PayOutInstruction**](PayOutInstruction.md) | [**PayOutInstruction**](PayOutInstruction.md) |  | [optional] 
**payInInstruction** | [**PayInInstruction**](PayInInstruction.md) | [**PayInInstruction**](PayInInstruction.md) |  | [optional] 
**usePayInMethod** | [**AccountMethod**](AccountMethod.md) | [**AccountMethod**](AccountMethod.md) |  | [optional] 
**usePayOutMethod** | [**AccountMethod**](AccountMethod.md) | [**AccountMethod**](AccountMethod.md) |  | [optional] 
**fee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**processingFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["FIXED", "MARKET", ] 
**netPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**grossPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**amountInGross** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**amountInNet** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**fees** | [**Fees**](Fees.md) | [**Fees**](Fees.md) |  | [optional] 
**dateCreated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**lastUpdated** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# payInLegs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentLeg**](PaymentLeg.md) | [**PaymentLeg**](PaymentLeg.md) | [**PaymentLeg**](PaymentLeg.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

