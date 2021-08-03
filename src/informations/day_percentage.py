import time as dwight
from datetime import datetime, date, time

class DayPercentage:

  def get(self, sleep, lcd):
    day_start = datetime.combine(date.today(), time())
    now = datetime.now()
    duration = now - day_start

    day_percentage = round((duration.total_seconds() * 100) / 86400, 2)

    lcd.clear()
    lcd.write_string(now.strftime("%d/%m/%Y %H:%M"))
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"{day_percentage}% gone")
    print(f"Day percentage = {day_percentage}%");
    dwight.sleep(sleep)
