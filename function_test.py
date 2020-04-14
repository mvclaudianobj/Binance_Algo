# -- coding: utf-8 --
import functions
import json
import API_Info


def main():
    api_key = API_Info.api_key()
    binance = functions.Info(key=api_key.key, secret=api_key.secret, line_notify_token=api_key.line_notify_api_token)
    Order = binance.creatOrder("BTC/USDT")
    cancelOrder = binance.cancelOrder()

    # 指し値注文
    # print(Order.limit_order(amount=0.001, side="BUY", price=6500))

    # 成行注文
    # print(Order.market_order(side="SELL", amount=0.001))

    # 逆指値注文
    # print(Order.stop_limit_order(side="buy", amount=0.001, price=7601, triggerPrice=7600))

    # 利益確定成行注文
    # print(Order.take_profit_market_order(side="buy", amount=0.01, triggerPrice=6300))

    # 逆指値成行注文
    # print(Order.stop_market_order(side="buy", amount=0.001, triggerPrice=6000, workingType="MARK_PRICE"))

    # 一つの注文をキャンセルする
    # print(cancelOrder.cancel_one_order(orderId="2631948567", symbol="BTC/USDT"))
    
    # ccxtのメソッドを使いたい場合のサンプル
    # 使えるUSDTの残高を確認する (ccxtを使う場合)
    # print(binance.binance_ccxt.fetch_balance()["info"]["assets"][1]["marginBalance"])

    # 使えるUSDTの残高を確認する (再定義した関数を使う場合)
    # print(binance.get_Margin_Balance())

    # LINE Notify通知
    # binance.line_notify("Hello, wolrd.")



if __name__ == '__main__':
    main()
