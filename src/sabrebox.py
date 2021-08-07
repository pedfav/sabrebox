
import time
import RPi.GPIO as gpio

from enum import Enum
from informations.weather_local import Weather
from informations.crypto import Crypto
from informations.ip import Ip
from informations.day_percentage import DayPercentage
from informations.weather_sa import WeatherSa
from helpers.lcd import lcd_write

gpio.setmode(gpio.BOARD)

gpio.setup(22, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(12, gpio.OUT)

class Informations(Enum):
  WEATHER = Weather()
  BTC = Crypto()
  DAY = DayPercentage()
  SA = WeatherSa()

def print_time(number_of_times):
  for x in range(number_of_times):
    if(gpio.input(22) == 1):
      gpio.output(12,gpio.HIGH)
      Ip().get(3)
      gpio.output(12,gpio.LOW)
    time.sleep(0.5)

while True:
  for info in Informations:
    first_line, second_line = info.value.get()

    if first_line is not None and second_line is not None:
      lcd_write(first_line, second_line)
      print_time(6)
