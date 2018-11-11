#encoding=utf-8
import time
from datetime import datetime
from datetime import timedelta
import calendar
print('''
1.1 用time模块获取当前的时间戳.
code :
time.time()
result :''')
print(time.time())
print('''
1.2 用datetime获取当前的日期，例如：2013-03-29
code :
datetime.strftime("%Y-%m-%D")''')
datetime.strftime(datetime.now(),'%Y-%m-%d')
print('''
1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27
code :
def months(dt,months):#这里的months 参数传入的是正数表示往后 ，负数表示往前
    month = dt.month - 1 + months
    year = int(dt.year + month / 12)
    month = month % 12 + 1
    day = min(dt.day,calendar.monthrange(year,month)[1])
    dt = dt.replace(year=year, month=month, day=day)
    return datetime.strftime(dt.replace(year=year, month=month, day=day),'%Y-%m-%d')
nowDay=datetime.now()
print(months(nowDay,-1))
''')
def months(dt,months):#这里的months 参数传入的是正数表示往后 ，负数表示往前
    month = dt.month - 1 + months
    year = int(dt.year + month / 12)
    month = month % 12 + 1
    day = min(dt.day,calendar.monthrange(year,month)[1])
    dt = dt.replace(year=year, month=month, day=day)
    return datetime.strftime(dt.replace(year=year, month=month, day=day),'%Y-%m-%d')
nowDay=datetime.now()
print(months(nowDay,-1))
