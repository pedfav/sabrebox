import socket
import time

from helpers.lcd import lcd_write

class Ip:

  def get(self, sleep):

    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))

      lcd_write("IP", s.getsockname()[0])
      print(f"IP={s.getsockname()[0]}")
      time.sleep(sleep)
    except Exception as e:
      print(f"Error on Ip: {e}")
