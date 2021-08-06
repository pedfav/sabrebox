
from enum import Enum
from informations.weather_local import Weather
from informations.crypto import Crypto
from informations.ip import Ip
from informations.day_percentage import DayPercentage
from informations.weather_sa import WeatherSa


class Informations(Enum):
  WEATHER = Weather()
  BTC = Crypto()
  IP = Ip()
  DAY = DayPercentage()
  SA = WeatherSa() 

while(True):
  for info in Informations:
    info.value.get(3)
