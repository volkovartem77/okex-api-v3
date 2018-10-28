# okex-api-v3
Python wrapper for okex api v3 Spot
> Full rest api https://www.okex.com/docs/en/

### Usage
```
from okex_api_spot import *
okex = Okex('<your_api_key>', '<your_secret_key>', '<your_pass_phrase>', '<your_fund_password>')

get_tickers = okex.get_ticker()
```
Json response (get_tickers)
```
{
  'best_ask': '0.06772422',
  'best_bid': '0.0676666',
  'instrument_id': 'BCH-BTC',
  'product_id': 'BCH-BTC',
  'last': '0.06773899',
  'ask': '0.06772422',
  'bid': '0.0676666',
  'open_24h': '0.06768605',
  'high_24h': '0.06807742',
  'low_24h': '0.06745257',
  'base_volume_24h': '29429',
  'timestamp': '2018-10-28T14:36:22.110Z',
  'quote_volume_24h': '1992'
},
{
  'best_ask': '0.00803306',
  'best_bid': '0.0080282',
  'instrument_id': 'LTC-BTC',
  'product_id': 'LTC-BTC',
  'last': '0.00803005',
  'ask': '0.00803306',
  'bid': '0.0080282',
  'open_24h': '0.00802884',
  'high_24h': '0.00806864',
  'low_24h': '0.00801004',
  'base_volume_24h': '459527',
  'timestamp': '2018-10-28T14:36:22.110Z',
  'quote_volume_24h': '3691'
}
...
```
