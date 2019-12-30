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

    def judge_ma_slope(self, side, symbol, period, ma_period, method="C"):
        method_lst = ["O", "H", "L", "C"]
        method_dict = {"O": 1, "H": 2, "L": 3, "C": 4}
        if method not in method_lst:
            print("INCORRECT METHOD!!!")
            exit()

        ohlcv_lst = self.binance_ccxt.fetch_ohlcv(symbol, timeframe=period, limit=ma_period + 2)
        if side == "sell":
            if ohlcv_lst[0] > ohlcv_lst[len(ohlcv_lst) - 2]:
                return {"slope": True,
                        "var_slope": (ohlcv_lst[0] - ohlcv_lst[len(ohlcv_lst) - 2][method_dict[method]]) / ma_period}
            else:
                return {"slope": False}
        else:
            if ohlcv_lst[0] < ohlcv_lst[len(ohlcv_lst) - 2]:
                return {"slope": True,
                        "var_slope": (ohlcv_lst[len(ohlcv_lst) - 2][method_dict[method]] - ohlcv_lst[0]) / ma_period}
            else:
                return {"slope": False}

    def moving_average(self, symbol, period, ma_period, method="C"):
        method_lst = ["O", "H", "L", "C"]
        method_dict = {"O": 1, "H": 2, "L": 3, "C": 4}
        if method not in method_lst:
            print("INCORRECT METHOD!!!")
            exit()

        sum_price = 0
        ohlcv_lst = self.binance_ccxt.fetch_ohlcv(symbol, timeframe=period, limit=ma_period + 1)

        for i in range(len(ohlcv_lst) - 1):
            sum_price += ohlcv_lst[i][method_dict[method]]

        return round(sum_price / ma_period, 3)

    # def last_updated_time(self, symbol, period, ma_period):
    #     ohlcv_lst = self.binance_ccxt.fetch_ohlcv(symbol, timeframe=period, limit=ma_period + 1)
    #     return ohlcv_lst[len(ohlcv_lst) - 1][0]
