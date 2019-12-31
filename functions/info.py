# -*- coding: utf-8 -*-
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
        print(message)
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

    def fetch_orders(self, orderID, symbol):
        return self.binance_ccxt.fetch_order(id=orderID, symbol=symbol)

    def moving_average(self, symbol, period, ma_period, method="C", delta=0):
        method_lst = ["O", "H", "L", "C"]
        method_dict = {"O": 1, "H": 2, "L": 3, "C": 4}
        if method not in method_lst:
            print("INCORRECT METHOD!!!")
            exit()

        sum_price = 0
        ohlcv_lst = self.binance_ccxt.fetch_ohlcv(symbol, timeframe=period, limit=ma_period + 1 + delta)

        for i in range(len(ohlcv_lst) - (1 + delta)):
            sum_price += ohlcv_lst[i][method_dict[method]]

        return round(sum_price / ma_period, 3)
