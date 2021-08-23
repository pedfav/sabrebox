
import requests


class Currency:

  def get(self):
    try:
      btc = self.get_btc()
      eth = self.get_eth()
      usd_euro = self.get_usd_euro()

      currencies = [btc,eth] + usd_euro

      print(currencies)
      return currencies
    except Exception as e:
      print(f"Error on crypto: {e}")
      return []
  
  def get_btc(self):
    try:
      response_btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

      if response_btc.status_code == 200:
        data_btc = response_btc.json()
        btc = data_btc["bpi"]["USD"]["rate"]
        return f"BTC - ${self.round(btc)}"

      return "BTC - Not found"
    except Exception:
      return "BTC - Not found"
  
  def get_eth(self):
    try:
      response_eth = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice')

      if response_eth.status_code == 200:
        data_eth = response_eth.json()
        eth = data_eth["result"]["ethusd"]
        return f"ETH - ${self.round(eth)}"

      return "ETH - Not found"
    except Exception:
      return "ETH - Not found"

  def get_usd_euro(self):
    try:
      response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')

      if response.status_code == 200:
        data_usd_euro = response.json()
        usd = data_usd_euro["USDBRL"]["ask"]
        euro = data_usd_euro["EURBRL"]["ask"]
        return [f"USD - R${self.round(usd)}", f"EUR - R${self.round(euro)}"]

      return ["USD - Not found", "EUR - Not found"]
    except Exception:
      return ["USD - Not found", "EUR - Not found"]

  def round_two(self, number):
    return round(float(number), 2)
