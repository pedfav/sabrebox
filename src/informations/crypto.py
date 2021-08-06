
import requests
import time

from helpers.lcd import lcd_write

class Crypto:

  def get(self, sleep):
    try:
      response_btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      data_btc = response_btc.json()
      btc = data_btc["bpi"]["USD"]["rate"]

      response_eth = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice')
      data_eth = response_eth.json()
      eth = data_eth["result"]["ethusd"]

      lcd_write(f"BTC - ${btc}", f"BTC - ${eth}")
      time.sleep(sleep)
    except Exception as e:
      print(f"Error on crypto: {e}")
