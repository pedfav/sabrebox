import calendar
from datetime import datetime, date, time
from helpers.lcd import lcd_write

class Time:

  def get(self):
    now = datetime.now()
    day_percentage = self.get_day_percentage(now)
    year_percentage = self.get_month_percentage(now)
    month_percentage = self.get_year_percentage()

    to_print = [now.strftime("%d/%m/%Y %H:%M"), day_percentage, month_percentage, year_percentage]
    
    print(to_print)
    return to_print

  def get_day_percentage(self, now):
    day_start = datetime.combine(date.today(), time())
    duration_day = now - day_start
    day_percentage = round((duration_day.total_seconds() * 100) / 86400, 2)
    return 'Day = {}%'.format(day_percentage)

  def get_month_percentage(self, now):
    today = date.today()
    month_start = date(date.today().year, date.today().month, 1)
    duration_month = today - month_start
    month_percentage = round(((duration_month.days + 1) * 100) / calendar.monthrange(now.year, now.month)[1], 2)
    return 'Month = {}%'.format(month_percentage)

  def get_year_percentage(self):
    today = date.today()
    year_start = date(date.today().year, 1, 1)
    duration_year = today - year_start
    year_percentage = round(((duration_year.days + 1) * 100) / 365, 2)
    return 'Year = {}%'.format(year_percentage)
