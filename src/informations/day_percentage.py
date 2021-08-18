import time as dwight
from datetime import datetime, date, time
from helpers.lcd import lcd_write

class DayPercentage:

  def get(self):
    day_start = datetime.combine(date.today(), time())
    now = datetime.now()
    duration = now - day_start

    day_percentage = round((duration.total_seconds() * 100) / 86400, 2)

    print(f"Day percentage = {day_percentage}%");
    return [now.strftime("%d/%m/%Y %H:%M"), f"{day_percentage}% gone"]
