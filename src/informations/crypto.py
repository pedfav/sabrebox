
import requests
import time

from helpers.lcd import lcd_write

class Crypto:

  def get(self):
    try:
      eth, btc = '**'
      response_btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      if response_btc.status_code == 200:
        data_btc = response_btc.json()
        btc = data_btc["bpi"]["USD"]["rate"]

      response_eth = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice')
      if response_btc.status_code == 200:
        data_eth = response_eth.json()
        eth = data_eth["result"]["ethusd"]

      print(f"BTC - ${btc} ETH - ${eth}")
      return f"BTC - ${btc}", f"ETH - ${eth}"
    except Exception as e:
      print(f"Error on crypto: {e}")
      return None, None
