# -*- coding: utf-8 -*-
import sys
import os

sys.path.append('./..')
import functions
import time
from API_Info import api_key
from datetime import datetime
import json


def main(param):
    global binance
    try:
        print("======= Strategy: Moving Average =======")
        binance = functions.Info(key=api_key.key, secret=api_key.secret,
                                 line_notify_token=api_key.line_notify_api_token)
        Order = binance.creatOrder("BTC/USDT")

        ######################################################################
        pair = param["pair"]
        lot = param["lot"]
        long_term = param["long_term"]
        short_term = param["short_term"]

        if param["order_close"] != "auto":
            stop_loss = param["order_close"]["stop_loss"]
            take_profit = param["order_close"]["take_profit"]

        period_lst = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w"]
        period_dict = {"1m": 60000, "3m": 180000, "5m": 300000, "15m": 900000,
                       "30m": 1800000, "1h": 3600000, "2h": 7200000, "4h": 14400000,
                       "6h": 21600000, "8h": 21600000, "12h": 43200000, "1d": 86400000,
                       "3d": 259200000, "1w": 604800000}

        if param["period"] not in period_lst:
            print("INCORRECT PERIOD!!!")
            exit()
        period = param["period"]
        ######################################################################
        print("======= {} =======".format("Param"))
        binance.line_notify(str(json.dumps(param, indent=4)))
        short_term_ma = binance.moving_average(pair, period, short_term)
        long_term_ma = binance.moving_average(pair, period, long_term)
        print("======= {} =======".format("MA"))
        print("short_term_ma: ", short_term_ma)
        print("long_term_ma: ", long_term_ma)

        print("======= {} =======".format("Account Balance"))
        binance.line_notify(binance.get_Margin_Balance())

        print("======= {} =======".format("Loop Start"))

        while True:
            if int(datetime.now().strftime('%s')) * 1000 % 60000 == 0:
                print("======= {} =======".format("Looping"))
            if int(datetime.now().strftime('%s')) * 1000 % 300000 == 0:
                binance.line_notify("======= {} =======".format("Now in 1st. Loop"))
            if int(datetime.now().strftime('%s')) * 1000 % period_dict[period] == 0:
                print("======= {} =======".format(period))
                time.sleep(5)
                if long_term_ma < short_term_ma:
                    print("======= {} =======".format("formar MA"))
                    print("formar short_term_ma: ", short_term_ma)
                    print("formar long_term_ma: ", long_term_ma)
                    short_term_ma = binance.moving_average(pair, period, short_term)
                    long_term_ma = binance.moving_average(pair, period, long_term)
                    print("======= {} =======".format("MA"))
                    print("short_term_ma: ", short_term_ma)
                    print("long_term_ma: ", long_term_ma)
                    if long_term_ma <= short_term_ma:
                        pass
                    # Dead Cross
                    else:
                        print("======= {} =======".format("New Sell Order"))
                        new_sell_order = Order.market_order("sell", lot)
                        binance.line_notify(str(new_sell_order["info"]))
                        if param["order_close"] != "auto":
                            print("======= {} =======".format("New Stop Order"))
                            binance.line_notify(str(Order.stop_market_order("buy", lot,
                                                                            float(binance.fetch_orders(
                                                                                new_sell_order["info"]["orderId"],
                                                                                pair)[
                                                                                      "info"][
                                                                                      "avgPrice"]) + stop_loss)[
                                                        "info"]))

                            print("======= {} =======".format("New Stop Order"))
                            binance.line_notify(str(Order.take_profit_market_order("buy", lot,
                                                                                   float(binance.fetch_orders(
                                                                                       new_sell_order["info"][
                                                                                           "orderId"],
                                                                                       pair)["info"][
                                                                                             "avgPrice"]) - take_profit)[
                                                        "info"]))
                        else:
                            judge_ma_period = param["judge_ma_period"]
                            after = binance.moving_average(pair, period, judge_ma_period)
                            before = binance.moving_average(pair, period, judge_ma_period, delta=1)
                            slope = after > before
                            print("======= {} =======".format("2nd. Loop Started"))
                            while not slope:
                                if int(datetime.now().strftime('%s')) * 1000 % 60000 == 0:
                                    print("======= {} =======".format("2nd. Looping"))
                                if int(datetime.now().strftime('%s')) * 1000 % 300000 == 0:
                                    binance.line_notify("======= {} =======".format("Now in 2nd. Loop"))
                                if int(datetime.now().strftime('%s')) * 1000 % period_dict[period] == 0:
                                    print("======= {} =======".format("2nd. " + period))
                                    time.sleep(5)
                                    after = binance.moving_average(pair, period, judge_ma_period)
                                    before = binance.moving_average(pair, period, judge_ma_period, delta=1)
                                    slope = after < before
                                    if slope:
                                        if ((before - after) * 100 / before) > param["order_close_per"]:
                                            print("======= {} =======".format("New Close Buy Order"))
                                            close_buy_order = Order.market_order("buy", lot)
                                            binance.line_notify(str(close_buy_order["info"]))

                                            print("======= {} =======".format("Account Balance"))
                                            binance.line_notify(binance.get_Margin_Balance())
                                            break
                                        else:
                                            pass

                elif long_term_ma > short_term_ma:
                    print("======= {} =======".format("formar MA"))
                    print("formar short_term_ma: ", short_term_ma)
                    print("formar long_term_ma: ", long_term_ma)
                    short_term_ma = binance.moving_average(pair, period, short_term)
                    long_term_ma = binance.moving_average(pair, period, long_term)
                    print("======= {} =======".format("MA"))
                    print("short_term_ma: ", short_term_ma)
                    print("long_term_ma: ", long_term_ma)
                    if long_term_ma >= short_term_ma:
                        pass
                    # Gold Cross
                    else:
                        print("======= {} =======".format("New Buy Order"))
                        new_buy_order = Order.market_order("buy", lot)
                        binance.line_notify(str(new_buy_order["info"]))
                        if param["order_close"] != "auto":
                            print("======= {} =======".format("New Stop Order"))
                            binance.line_notify(str(Order.stop_market_order("sell", lot,
                                                                            float(binance.fetch_orders(
                                                                                new_buy_order["info"]["orderId"], pair)[
                                                                                      "info"][
                                                                                      "avgPrice"]) - stop_loss)[
                                                        "info"]))
                            print("======= {} =======".format("New Stop Order"))
                            binance.line_notify(str(Order.take_profit_market_order("sell", lot,
                                                                                   float(binance.fetch_orders(
                                                                                       new_buy_order["info"]["orderId"],
                                                                                       pair)["info"][
                                                                                             "avgPrice"]) + take_profit)[
                                                        "info"]))
                        else:
                            judge_ma_period = param["judge_ma_period"]
                            after = binance.moving_average(pair, period, judge_ma_period)
                            before = binance.moving_average(pair, period, judge_ma_period, delta=1)
                            slope = after < before
                            while not slope:
                                if int(datetime.now().strftime('%s')) * 1000 % 60000 == 0:
                                    print("======= {} =======".format("2nd. Looping"))
                                if int(datetime.now().strftime('%s')) * 1000 % 300000 == 0:
                                    binance.line_notify("======= {} =======".format("Now in 2nd. Loop"))
                                if int(datetime.now().strftime('%s')) * 1000 % period_dict[period] == 0:
                                    print("======= {} =======".format("2nd. " + period))
                                    time.sleep(5)
                                    after = binance.moving_average(pair, period, judge_ma_period)
                                    before = binance.moving_average(pair, period, judge_ma_period, delta=1)
                                    slope = after > before
                                    if slope:
                                        if ((after - before) * 100 / before) > param["order_close_per"]:
                                            print("======= {} =======".format("New Close Sell Order"))
                                            close_sell_order = Order.market_order("sell", lot)
                                            binance.line_notify(str(close_sell_order["info"]))

                                            print("======= {} =======".format("Account Balance"))
                                            binance.line_notify(binance.get_Margin_Balance())
                                            break
                                        else:
                                            pass

    except Exception as e:
        binance.line_notify("ERROR: \n" + str(e))


if __name__ == '__main__':
    # param = {
    #     "pair": "BTC/USDT",
    #     "lot": 0.1,
    #     "long_term": 25,
    #     "short_term": 10,
    #     "order_close": "auto",  # 自動でオーダークローズ
    #     # "order_close": {"stop_loss": 30, # 手動でオーダークローズ
    #     #                 "take_profit": 60},
    #     "judge_ma_period": 7,
    #     "order_close_per": 0.02,
    #     "period": "5m",
    # }

    with open('./moving_average.json') as f:
        param = json.load(f)

    main(param)
