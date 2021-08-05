import requests
import time

from datetime import datetime

class Ethereum:

  def get(self, sleep, lcd):
    try:  
      response = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice')
      data = response.json()
      eth = data["result"]["ethusd"]
    except Exception as e:
      eth = "###########"

    lcd.clear()
    lcd.write_string("ETH")
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"${eth}")
    print(f"eth=${eth}")
    time.sleep(sleep)
