
import RPi.GPIO as gpio

from enum import Enum
from informations.weather_local import Weather
from informations.crypto import Crypto
from informations.ip import Ip
from informations.day_percentage import DayPercentage
from informations.weather_sa import WeatherSa

gpio.setmode(gpio.BCM)

gpio.setup(25, gpio.IN, pull_up_down = gpio.PUD_DOWN)

class Informations(Enum):
  WEATHER = Weather()
  BTC = Crypto()
  IP = Ip()
  DAY = DayPercentage()
  SA = WeatherSa() 

while(True):
  for info in Informations:
    if(gpio.input(23) == 1):
      print('kkkkk')    
    info.value.get(3)
