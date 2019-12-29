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
    print(json.dumps(binance_futures.load_markets(), indent=4))



if __name__ == '__main__':
    main()
