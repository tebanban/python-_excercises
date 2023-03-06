from datetime import date, timedelta, datetime

date_1 = datetime.strptime("2023-05-05", '%Y-%m-%d')
print(date_1)  # 👉️ 2023-09-07

date_2 = date_1 + timedelta(days= 90)

delta= date_2 - date_1

print(delta.days)
days= []
for i in range(delta.days +1):
     days= date_1 + timedelta(days = i)
     print(days)