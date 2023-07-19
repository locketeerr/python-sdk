# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_CURRENCY_CRYPTO = "/api/currency/crypto"
    API_CURRENCY_FIAT = "/api/currency/fiat"
    API_CURRENCY_DEPOSIT = "/api/currency/deposit"
    API_V1_MERCHANT = "/api/v1/merchant"
    API_V1_PAY_SUMMARY = "/api/v1/pay/summary"
    API_V1_PAY_UUID_SUMMARY = "/api/v1/pay/{uuid}/summary"
    API_V1_PAY_VALIDATE = "/api/v1/pay/validate"
    API_V2_CHANNEL = "/api/v2/channel"
    API_V2_CHANNEL_UUID = "/api/v2/channel/{uuid}"
    API_V2_CHANNEL_PAYMENT_UUID = "/api/v2/channel/payment/{uuid}"
    API_V2_CHANNEL_PAYMENT = "/api/v2/channel/payment"
    API_WALLET = "/api/wallet"
    API_WALLET_ID = "/api/wallet/{id}"
    API_WALLET_BALANCES = "/api/wallet/balances"
    API_TRANSACTION_REPORT = "/api/transaction/report"
    API_V1_QUOTE = "/api/v1/quote"
    API_V1_QUOTE_ACCEPT_UUID = "/api/v1/quote/accept/{uuid}"
    API_V1_QUOTE_UUID = "/api/v1/quote/{uuid}"
    API_V1_QUOTE_MERCHANT_ID = "/api/v1/quote/{merchantId}"
