import socket
import time

from datetime import datetime

class Ip:

  def get(self, sleep, lcd):
    lcd.clear()

    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))

      lcd.write_string("IP")
      lcd.cursor_pos=(1,0)
      lcd.write_string(s.getsockname()[0])
      print(f"IP={s.getsockname()[0]}")
    except Exception as e:
      lcd.write_string("IP")
      lcd.cursor_pos=(1,0)
      lcd.write_string("#.#.#.#")

    time.sleep(sleep)
