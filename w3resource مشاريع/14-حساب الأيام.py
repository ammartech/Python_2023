from datetime import date

date_1=date(2014,5,6)
date_2=date(2015,6,3)

delta_date=date_2-date_1

days_cal = delta_date.days

print("الأيام",days_cal)
