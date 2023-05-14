import requests
import json
from mytoken import keys

class APIException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: float):
        if quote == base:
            raise APIException(f'Невозможно перевести валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        url = f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}'
        r = requests.get(url)
        data = json.loads(r.content)

        if base_ticker not in data:
            raise APIException(f'Не удалось получить курс {quote} к {base}.')

        total_base = data[base_ticker] * amount

        return total_base

