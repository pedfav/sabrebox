
import time
import RPi.GPIO as gpio

from enum import Enum
from informations.weather_local import Weather
from informations.crypto import Crypto
from informations.ip import Ip
from informations.day_percentage import DayPercentage
from informations.weather_sa import WeatherSa

gpio.setmode(gpio.BOARD)

gpio.setup(22, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(12, gpio.OUT)

class Informations(Enum):
  WEATHER = Weather()
  BTC = Crypto()
  DAY = DayPercentage()
  SA = WeatherSa()

while(True):
  for info in Informations:
    if(gpio.input(22) == 1):
      Ip().get(3)
    gpio.output(12,gpio.HIGH)
    info.value.get(3)
    gpio.output(12,gpio.LOW)
    time.sleep(1)

