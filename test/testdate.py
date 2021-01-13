from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
d = today - relativedelta(months=1)

first_day = date(d.year, d.month, 1)
print(first_day.strftime("%Y-%m-%d"))
#returns first date of the previous month - datetime.date(2019, 7, 1)

last_day = date(today.year, today.month, 1) - relativedelta(days=1)
print(last_day.strftime("%Y-%m-%d"))