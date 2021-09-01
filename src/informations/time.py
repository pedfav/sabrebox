import calendar
from datetime import datetime, date, time

DAY_IN_SECONDS = 86400

class Time:

  def get(self):
    now = datetime.now()
    day_percentage = self.get_day_percentage(now)
    month_percentage = self.get_month_percentage(now)
    year_percentage = self.get_year_percentage(now)

    to_print = [now.strftime("%d/%m/%Y %H:%M"), day_percentage, month_percentage, year_percentage]
    
    print(to_print)
    return to_print

  def get_day_percentage(self, now):
    duration_day = self.get_duration_today(now)
    day_percentage = round((duration_day * 100) / 86400, 2)
    return 'Day   - {}%'.format(day_percentage)

  def get_month_percentage(self, now):
    duration_day = self.get_duration_today(now)
    today = date.today()
    month_start = date(date.today().year, date.today().month, 1)
    duration_month = today - month_start
    month_percentage = round((((duration_month.days * DAY_IN_SECONDS) + duration_day) * 100) / (calendar.monthrange(now.year, now.month)[1] * DAY_IN_SECONDS), 2)
    return 'Month - {}%'.format(month_percentage)

  def get_year_percentage(self, now):
    duration_day = self.get_duration_today(now)
    today = date.today()
    year_start = date(date.today().year, 1, 1)
    duration_year = today - year_start
    year_percentage = round((((duration_year.days * DAY_IN_SECONDS) + duration_day) * 100) / (self.total_days_year(today) * DAY_IN_SECONDS), 2)
    return 'Year  - {}%'.format(year_percentage)

  def get_duration_today(self, now):
    day_start = datetime.combine(date.today(), time())
    return (now - day_start).total_seconds()
  
  def total_days_year(self, today):
    if calendar.isleap(today.year):
      return 366
    else:
      return 365
