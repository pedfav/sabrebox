
import time
import Adafruit_DHT

from helpers.lcd import lcd_write


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class Weather:

  def get(self, sleep):
    try:
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

      if humidity is not None and temperature is not None:
        lcd_write(f"Temp - {round(temperature, 2)}C", f"Hum  - {round(humidity, 2)}%")
        print(f"Temperature={round(temperature, 2)} - Humidity={round(humidity, 2)}")
      else:
        lcd_write("DHT22 not workin", "")
        print("DHT22 not workin")
    except Exception as e:
      lcd_write("DHT22 not workin", "")
      print("DHT22 not workin")

    time.sleep(sleep)

