import socket
import time

from datetime import datetime

class Ip:

  def get(self, sleep, lcd):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    lcd.clear()
    lcd.write_string(now)
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"IP={s.getsockname()[0]}")
    print(f"IP={s.getsockname()[0]}")

    time.sleep(sleep)
