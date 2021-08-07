
import time
import Adafruit_DHT

from helpers.lcd import lcd_write


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class Weather:

  def get(self, sleep):
    try:
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

      print(f"Temperature={round(temperature, 2)} - Humidity={round(humidity, 2)}")
      return f"Temp - {round(temperature, 2)}C", f"Hum  - {round(humidity, 2)}%"
     
    except Exception as e:
      print(f"Error on DHT: {e}")
      return None, None
