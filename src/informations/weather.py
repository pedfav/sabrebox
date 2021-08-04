
import time
import Adafruit_DHT

from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
#DHT_PIN = 4
DHT_PIN = 7

class Weather:

  def get(self, sleep, lcd):
    try:
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
      lcd.clear()

      if humidity is not None and temperature is not None:
        lcd.write_string(f"Temp - {round(temperature, 2)}C")
        lcd.cursor_pos=(1,0)
        lcd.write_string(f"Hum  - {round(humidity, 2)}%")
        print(f"Temperature={round(temperature, 2)} - Humidity={round(humidity, 2)}")
      else:
        lcd.write_string("DHT22 not workin")
        print("DHT22 not workin")
    except Exception as e:
      lcd.write_string("DHT22 not workin")
      print("DHT22 not workin")

    time.sleep(sleep)

