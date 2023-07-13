import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_currency_crypto import ApiCurrencyCrypto
from openapi_client.apis.paths.api_currency_fiat import ApiCurrencyFiat
from openapi_client.apis.paths.api_currency_deposit import ApiCurrencyDeposit
from openapi_client.apis.paths.api_v1_merchant import ApiV1Merchant
from openapi_client.apis.paths.api_v1_pay_summary import ApiV1PaySummary
from openapi_client.apis.paths.api_v1_pay_uuid_summary import ApiV1PayUuidSummary
from openapi_client.apis.paths.api_v1_pay_validate import ApiV1PayValidate
from openapi_client.apis.paths.api_v2_channel import ApiV2Channel
from openapi_client.apis.paths.api_v2_channel_uuid import ApiV2ChannelUuid
from openapi_client.apis.paths.api_v2_channel_payment_uuid import ApiV2ChannelPaymentUuid
from openapi_client.apis.paths.api_v2_channel_payment import ApiV2ChannelPayment
from openapi_client.apis.paths.api_wallet import ApiWallet
from openapi_client.apis.paths.api_wallet_id import ApiWalletId
from openapi_client.apis.paths.api_wallet_balances import ApiWalletBalances
from openapi_client.apis.paths.api_transaction_report import ApiTransactionReport
from openapi_client.apis.paths.api_v1_quote import ApiV1Quote
from openapi_client.apis.paths.api_v1_quote_accept_uuid import ApiV1QuoteAcceptUuid
from openapi_client.apis.paths.api_v1_quote_uuid import ApiV1QuoteUuid
from openapi_client.apis.paths.api_v1_quote_merchant_id import ApiV1QuoteMerchantId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_CURRENCY_CRYPTO: ApiCurrencyCrypto,
        PathValues.API_CURRENCY_FIAT: ApiCurrencyFiat,
        PathValues.API_CURRENCY_DEPOSIT: ApiCurrencyDeposit,
        PathValues.API_V1_MERCHANT: ApiV1Merchant,
        PathValues.API_V1_PAY_SUMMARY: ApiV1PaySummary,
        PathValues.API_V1_PAY_UUID_SUMMARY: ApiV1PayUuidSummary,
        PathValues.API_V1_PAY_VALIDATE: ApiV1PayValidate,
        PathValues.API_V2_CHANNEL: ApiV2Channel,
        PathValues.API_V2_CHANNEL_UUID: ApiV2ChannelUuid,
        PathValues.API_V2_CHANNEL_PAYMENT_UUID: ApiV2ChannelPaymentUuid,
        PathValues.API_V2_CHANNEL_PAYMENT: ApiV2ChannelPayment,
        PathValues.API_WALLET: ApiWallet,
        PathValues.API_WALLET_ID: ApiWalletId,
        PathValues.API_WALLET_BALANCES: ApiWalletBalances,
        PathValues.API_TRANSACTION_REPORT: ApiTransactionReport,
        PathValues.API_V1_QUOTE: ApiV1Quote,
        PathValues.API_V1_QUOTE_ACCEPT_UUID: ApiV1QuoteAcceptUuid,
        PathValues.API_V1_QUOTE_UUID: ApiV1QuoteUuid,
        PathValues.API_V1_QUOTE_MERCHANT_ID: ApiV1QuoteMerchantId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_CURRENCY_CRYPTO: ApiCurrencyCrypto,
        PathValues.API_CURRENCY_FIAT: ApiCurrencyFiat,
        PathValues.API_CURRENCY_DEPOSIT: ApiCurrencyDeposit,
        PathValues.API_V1_MERCHANT: ApiV1Merchant,
        PathValues.API_V1_PAY_SUMMARY: ApiV1PaySummary,
        PathValues.API_V1_PAY_UUID_SUMMARY: ApiV1PayUuidSummary,
        PathValues.API_V1_PAY_VALIDATE: ApiV1PayValidate,
        PathValues.API_V2_CHANNEL: ApiV2Channel,
        PathValues.API_V2_CHANNEL_UUID: ApiV2ChannelUuid,
        PathValues.API_V2_CHANNEL_PAYMENT_UUID: ApiV2ChannelPaymentUuid,
        PathValues.API_V2_CHANNEL_PAYMENT: ApiV2ChannelPayment,
        PathValues.API_WALLET: ApiWallet,
        PathValues.API_WALLET_ID: ApiWalletId,
        PathValues.API_WALLET_BALANCES: ApiWalletBalances,
        PathValues.API_TRANSACTION_REPORT: ApiTransactionReport,
        PathValues.API_V1_QUOTE: ApiV1Quote,
        PathValues.API_V1_QUOTE_ACCEPT_UUID: ApiV1QuoteAcceptUuid,
        PathValues.API_V1_QUOTE_UUID: ApiV1QuoteUuid,
        PathValues.API_V1_QUOTE_MERCHANT_ID: ApiV1QuoteMerchantId,
    }
)
