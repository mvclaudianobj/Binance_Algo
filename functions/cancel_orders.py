# -*- coding: utf-8 -*-
class cancelOrders:
    def __init__(self, binance_ccxt):
        self.binance_ccxt = binance_ccxt

    def cancel_one_order(self, orderId, symbol):
        """

        :param orderId: order ID, str
        :param symbol: symbol, str
        :return:
        """
        return self.binance_ccxt.cancel_order(id=orderId, symbol=symbol)
