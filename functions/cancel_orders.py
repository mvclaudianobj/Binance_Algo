class cancelOrders:
    def __init__(self, binance_futures):
        self.binance_futures = binance_futures

    def cancel_one_order(self, orderId, symbol):
        """

        :param orderId: order ID, str
        :param symbol: symbol, str
        :return:
        """
        return self.binance_futures.cancel_order(id=orderId, symbol=symbol)

    # def cancel_all_orders(self, symbol):
    #     return self.binance_futures.cancel_order(symbol=symbol)
    #
    # def cancel_some_orders(self, orderIds, symbol):
    #     return self.binance_futures.cancel_order(id=orderIds, symbol=symbol)
