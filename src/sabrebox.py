import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD
from enum import Enum
from informations.weather import Weather
from informations.bitcoin import Bitcoin
from informations.ip import Ip
from informations.day_percentage import DayPercentage
from informations.message import Message

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

class Informations(Enum):
  WEATHER = Weather()
  BTC = Bitcoin()
  IP = Ip()
  DAY = DayPercentage()
  MESSAGE = Message()

while(True):
  for info in Informations:
    info.value.get(4, lcd)
