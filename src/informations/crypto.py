
import requests
import time

from helpers.lcd import lcd_write

class Crypto:

  def get(self, sleep):
    try:  
      response_btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      if response_btc.status_code == 200:
        data = response_btc.json()
        btc = data["bpi"]["USD"]["rate"]

      response_eth = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice')
      if response_eth == 200:
        data = response_eth.json()
        eth = data["result"]["ethusd"]

      lcd_write(f"BTC - ${btc}", f"BTC - ${eth}")
      time.sleep(sleep)
    except Exception as e:
      print(f"Error on crypto: {e}")
