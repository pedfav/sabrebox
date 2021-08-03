import time

class Message:

  def get(self, sleep, lcd):
    message = '#FODAC'
    lcd.clear()
    lcd.write_string(message)
    print(message);
    dwight.sleep(sleep)
