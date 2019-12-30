from functions import create_orders
from functions import cancel_orders
import ccxt
import requests


class Info:
    def __init__(self, key, secret, line_notify_token=None):
        self.key = key
        self.secret = secret
        self.line_notify_token = line_notify_token
        self.binance_ccxt = ccxt.binance({
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

    def line_notify(self, message, pic=False, path=None):
        if self.line_notify_token != None:
            line_notify_api = 'https://notify-api.line.me/api/notify'
            message = "\n{}\n".format(message)
            payload = {'message': message}
            if pic == False:
                headers = {'Authorization': 'Bearer ' + self.line_notify_token}
                requests.post(line_notify_api, data=payload, headers=headers)
            else:
                files = {"imageFile": open(path, "rb")}
                headers = {'Authorization': 'Bearer ' + self.line_notify_token}
                requests.post(line_notify_api, data=payload, headers=headers, files=files)
        else:
            return "NO LINE NOTIFY TOKEN."

    def creatOrder(self, symbol):
        return create_orders.creatOrders(self.binance_ccxt, symbol=symbol)

    def cancelOrder(self):
        return cancel_orders.cancelOrders(self.binance_ccxt)

    def get_Margin_Balance(self):
        return float(self.binance_ccxt.fetch_balance()["info"]["assets"][1]["marginBalance"])
