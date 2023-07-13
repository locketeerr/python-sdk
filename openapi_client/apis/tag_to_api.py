import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.currencies_api import CurrenciesApi
from openapi_client.apis.tags.merchant_ids_api import MerchantIDsApi
from openapi_client.apis.tags.payments_api import PaymentsApi
from openapi_client.apis.tags.channels_api import ChannelsApi
from openapi_client.apis.tags.wallets_api import WalletsApi
from openapi_client.apis.tags.trading_and_conversions_api import TradingAndConversionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.MERCHANT_IDS: MerchantIDsApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.CHANNELS: ChannelsApi,
        TagValues.WALLETS: WalletsApi,
        TagValues.TRADING_AND_CONVERSIONS: TradingAndConversionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CURRENCIES: CurrenciesApi,
        TagValues.MERCHANT_IDS: MerchantIDsApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.CHANNELS: ChannelsApi,
        TagValues.WALLETS: WalletsApi,
        TagValues.TRADING_AND_CONVERSIONS: TradingAndConversionsApi,
    }
)
