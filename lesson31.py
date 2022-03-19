from datetime import date
from datetime import datetime
import locale

# today = date.today()
# print(today)  # 2022-03-19
# print(today.year)  # 2022
# print(today.month)  #3
# print(today.day)  #19
# print(datetime.now())

now = datetime.now()
# print(now.today())
# print(now.hour)
# print(datetime.now().minute)

# days = ['пн','вт','ср','чт','пт','сб','вс']
# print(days[now.weekday()])  #  сб
locale.setlocale(locale.LC_ALL, 'uk_UA')
print(now)
print(now.strftime('%a'))
print(now.strftime('%A'))

print(f'Дата: {now.strftime("%A, %d %b %Y")}')
print(f'Час: {now.strftime("%H:%M")}')