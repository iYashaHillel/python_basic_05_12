import requests

date = input('Enter your date (e.g. 01.01.2023): ')
url = f'https://api.privatbank.ua/p24api/exchange_rates?date={date}'

resp = requests.get(url)
data = resp.json()

currency = input('Enter currency code: ')

currency_item = next(filter(lambda x: x['currency'] == currency, data['exchangeRate']))
print(currency_item)

# for rate in data['exchangeRate']:
#     print(f'Currency: {rate["currency"]}\nSale: {rate["saleRateNB"]}\nBuy: {rate["purchaseRateNB"]}\n')
