from functions import create_orders
from functions import cancel_orders
import ccxt


class Info:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.binance_futures = ccxt.binance({
            'apiKey': self.key,
            'secret': self.secret,
            'enableRateLimit': True,
            'option': {'defaultMarket': 'futures'},
            'urls': {
                'api': {
                    'public': 'https://fapi.binance.com/fapi/v1',
                    'private': 'https://fapi.binance.com/fapi/v1',
                }, }
        })

    def creatOrder(self, symbol):
        return create_orders.creatOrders(self.binance_futures, symbol=symbol)

    def cancelOrder(self):
        return cancel_orders.cancelOrders(self.binance_futures)
