from okex_api_spot import *

api_key = '<your api key>'
secret_key = 'your secret key'
passphrase = '<your passphrase>'
fund_password = '<your fund password>'


############# Usage #############

okex = Okex(api_key, secret_key, passphrase, fund_password)

### Wallet ###

print(okex.currencies())
print(okex.wallet())
print(okex.wallet('LSK'))
print(okex.withdrawal_fee())
print(okex.withdrawal_fee('ETH'))
print(okex.withdrawal_history())
print(okex.withdrawal_history('ETH'))
print(okex.ledger())
print(okex.deposit_address('ETH'))
print(okex.deposit_history())
print(okex.deposit_history('ETH'))

### Trading Spot ###

print(okex.spot_account())
print(okex.spot_account('ETH'))
print(okex.spot_ledger('ETH'))
print(okex.spot_ledger('ETH', limit='2'))
#print(okex.place_limit_buy_order('LSK/USDT', '4', '1'))
#print(okex.place_limit_sell_order('LSK/USDT', '3', '1'))
#print(okex.place_market_buy_order('LSK/USDT', '1'))
#print(okex.place_market_sell_order('LSK/USDT', '1'))
print(okex.cancel_order(1648986843587584, 'LSK/USDT'))
print(okex.get_order_list('all', 'LSK/USDT'))
print(okex.get_all_open_orders())
print(okex.get_all_open_orders('LSK/USDT'))
print(okex.get_order_details(1648986843587584, 'LSK/USDT'))
print(okex.get_transaction_details(1648986843587584, 'LSK/USDT'))
print(okex.get_markets_details())
print(okex.get_orderbook('LSK/USDT'))
print(okex.get_orderbook('LSK/USDT', size='10'))
print(okex.get_orderbook('LSK/USDT', depth='0.0001'))
print(okex.get_ticker())
print(okex.get_ticker('LSK/USDT'))
print(okex.get_trades_details('LSK/jUSDT'))
print(okex.get_trades_details('LSK/USDT', limit='2'))
print(okex.get_candles('LSK/USDT', TimeFrame.H4))
start_time = datetime.datetime.now() - datetime.timedelta(seconds=3600)
end_time = datetime.datetime.now()
print(okex.get_candles('LSK/USDT', TimeFrame.M1, start_time, end_time))
