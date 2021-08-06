
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
  IP = Ip()
  DAY = DayPercentage()
  SA = WeatherSa() 

while(True):
  gpio.output(12,gpio.HIGH)
  time.sleep(1)
  gpio.output(12,gpio.HIGH)
  for info in Informations:  
    info.value.get(3)
