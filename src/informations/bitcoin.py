
import requests
import time

from datetime import datetime

class Bitcoin:

  def get(self, sleep, lcd):
    try:  
      response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      data = response.json()
      btc = data["bpi"]["USD"]["rate"]
    except Exception as e:
      btc = "###########"

    lcd.clear()
    lcd.write_string("BTC")
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"${btc}")
    print(f"BTC=${btc}")
    time.sleep(sleep)
