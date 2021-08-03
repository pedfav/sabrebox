
import time
import Adafruit_DHT

from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


class Weather:

  def get(self, sleep, lcd):
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    lcd.clear()

    if humidity is not None and temperature is not None:
      lcd.write_string(now)
      lcd.cursor_pos=(1,0)
      lcd.write_string(f"T={round(temperature, 2)} - H={round(humidity, 2)}")
      print(f"Time={now} - Temperature={round(temperature, 2)} - Humidity={round(humidity, 2)}")
    else:
      lcd.write_string("DHT22 not workin")
      print("DHT22 not workin")

    time.sleep(sleep)

