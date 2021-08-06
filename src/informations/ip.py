import socket
import time

from datetime import datetime
from helpers.lcd import lcd_write

class Ip:

  def get(self, sleep):

    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))

      lcd_write("IP", s.getsockname()[0])
      print(f"IP={s.getsockname()[0]}")
    except Exception as e:
      lcd_write("IP", "#.#.#.#")

    time.sleep(sleep)
