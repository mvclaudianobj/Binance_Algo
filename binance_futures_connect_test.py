import ccxt
import json
from API_Info import api_key


def main():
    binance_futures = ccxt.binance({
        'apiKey': api_key.key,
        'secret': api_key.secret,
        'enableRateLimit': True,
        'option': {'defaultMarket': 'futures'},
        'urls': {
            'api': {
                'public': 'https://fapi.binance.com/fapi/v1',
                'private': 'https://fapi.binance.com/fapi/v1',
            }, }
    })

    # 取引ペア詳細の一覧
    print(json.dumps(binance_futures.load_markets(), indent=4))

    # 新規注文
    print(binance_futures.create_order("BTC/USDT", "LIMIT", "BUY", 0.01, 7100))
    # {'info': {'orderId': 467051443, 'symbol': 'BTCUSDT', 'status': 'NEW', 'clientOrderId': 'oYw35DTndBBxPEBqxTVUcm',
    #           'price': '7100', 'avgPrice': '0.00000', 'origQty': '0.010', 'executedQty': '0', 'cumQty': '0',
    #           'cumQuote': '0', 'timeInForce': 'GTC', 'type': 'LIMIT', 'reduceOnly': False, 'side': 'BUY',
    #           'stopPrice': '0', 'workingType': 'CONTRACT_PRICE', 'origType': 'LIMIT', 'updateTime': 1577654973723},
    #  'id': '467051443', 'timestamp': None, 'datetime': None, 'lastTradeTimestamp': None, 'symbol': 'BTC/USDT',
    #  'type': 'limit', 'side': 'buy', 'price': 7100.0, 'amount': 0.01, 'cost': 0.0, 'average': None, 'filled': 0.0,
    #  'remaining': 0.01, 'status': 'open', 'fee': None, 'trades': None}


if __name__ == '__main__':
    main()
