
import requests
import time

from datetime import datetime

class Bitcoin:

  def get(self, sleep, lcd):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc = data["bpi"]["USD"]["rate"]

    lcd.clear()
    lcd.write_string(now)
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"BTC={btc}")
    print(f"BTC={btc}")
    time.sleep(sleep)
