# -*- coding: utf-8 -*-
class creatOrders:
    def __init__(self, binance_ccxt, symbol):
        self.symbol = symbol
        self.binance_ccxt = binance_ccxt

    def limit_order(self, side, amount, price, params={}):
        """

        :param side: "buy" or "sell", str
        :param amount: quantity, float
        :param price: limit price, float
        :param params: {}, json
        :return:
        """
        return self.binance_ccxt.create_order(symbol=self.symbol, type="LIMIT", side=side, amount=amount,
                                              price=price, params=params)

    def market_order(self, side, amount, params={}):
        """

        :param side: "buy" or "sell", str
        :param amount: quantity, float
        :param params: {}, json
        :return:
        """
        return self.binance_ccxt.create_order(symbol=self.symbol, type="MARKET", side=side, amount=amount,
                                              params=params)

    def stop_limit_order(self, side, amount, price, triggerPrice, workingType=None):
        """

        :param side: "buy" or "sell", str
        :param amount: quantity, float
        :param price: stop limit price, float
        :param triggerPrice: trigger price, float
        :return:
        """
        if workingType == "MARK_PRICE":
            return self.binance_ccxt.create_order(symbol=self.symbol, type="STOP", side=side, amount=amount,
                                                  price=price, params={"stopPrice": triggerPrice,
                                                                       "workingType": workingType})
        else:
            return self.binance_ccxt.create_order(symbol=self.symbol, type="STOP", side=side, amount=amount,
                                                  price=price, params={"stopPrice": triggerPrice})

    # def take_profit_limit_order(self, side, amount, price, triggerPrice):
    #     return self.binance_ccxt.create_order(symbol=self.symbol, type="TAKE_PROFIT", side=side, amount=amount,
    #                                              price=price, params={"stopPrice": triggerPrice})

    def stop_market_order(self, side, amount, triggerPrice, workingType=None):
        """

        :param side: "buy" or "sell", str
        :param amount: quantity, float
        :param triggerPrice: trigger price, float
        :return:
        """
        if workingType == "MARK_PRICE":
            return self.binance_ccxt.create_order(symbol=self.symbol, type="STOP_MARKET", side=side, amount=amount,
                                                  params={"stopPrice": triggerPrice,
                                                          "workingType": workingType})
        else:
            return self.binance_ccxt.create_order(symbol=self.symbol, type="STOP_MARKET", side=side, amount=amount,
                                                  params={"stopPrice": triggerPrice})

    def take_profit_market_order(self, side, amount, triggerPrice, workingType=None):
        """

        :param side: "buy" or "sell", str
        :param amount: quantity, float
        :param triggerPrice: trigger price, float
        :return:
        """
        if workingType == "MARK_PRICE":
            return self.binance_ccxt.create_order(symbol=self.symbol, type="TAKE_PROFIT_MARKET", side=side,
                                                  amount=amount, params={"stopPrice": triggerPrice,
                                                                         "workingType": workingType})
        else:
            return self.binance_ccxt.create_order(symbol=self.symbol, type="TAKE_PROFIT_MARKET", side=side,
                                                  amount=amount, params={"stopPrice": triggerPrice})
