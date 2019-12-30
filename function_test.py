import functions
import json
from API_Info import api_key


def main():
    binance = functions.Info(key=api_key.key, secret=api_key.secret)
    Order = binance.creatOrder("BTC/USDT")
    cancelOrder = binance.cancelOrder()

    # 指し値注文
    # print(Order.limit_order(amount=0.01, side="BUY", price=7100))

    # 成行注文
    # print(Order.market_order("BUY", 0.01))

    # 逆指値注文
    # print(Order.stop_limit_order("buy", 0.01, 7601, 7600))

    # 利益確定成行注文
    # print(Order.take_profit_market_order("sell", 0.01, 7800))

    # 逆指値成行注文
    # print(Order.stop_market_order("sell", 0.01, 7000, workingType="MARK_PRICE"))

    # 一つの注文をキャンセルする
    # print(cancelOrder.cancel_one_order("468168615", "BTC/USDT"))
    
    # ccxtのメソッドを使いたい場合のサンプル
    # 使えるUSDTの残高を確認する (ccxtを使う場合)
    # print(binance.binance_ccxt.fetch_balance()["info"]["assets"][1]["marginBalance"])

    # 使えるUSDTの残高を確認する (再定義した関数を使う場合)
    # print(binance.get_Margin_Balance())



if __name__ == '__main__':
    main()
