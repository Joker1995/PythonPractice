#encoding=utf-8
import time
from datetime import datetime
from datetime import timedelta
import calendar
import os
import pickle
import random
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

print('''2. 用os模块的方法完成ping www.baidu.com 操作
code :
os.system("ping -c 3 www.baidu.com")''')
os.system("ping -c 3 www.baidu.com")

print('''3. 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：
dirpwd路径下所有文件不重复的扩展名，如果有2个".py"的扩展名，则返回一个".py"
code :
def ext_name(dir):
    result=[]
    if os.path.isdir(dir):
        listDir=os.listdir(dir)
        for f in listDir:
            if os.path.isfile(f):
                result.append(os.path.splitext(f)[1])
            else:
                ext_name(f)
    else:
        result.append(os.path.splitext(dir)[1])
    result=set(result)
    return result
print(ext_name('/home/joker/code/python'))''')
def ext_name(dir):
    result=[]
    if os.path.isdir(dir):
        listDir=os.listdir(dir)
        for f in listDir:
            if os.path.isfile(f):
                result.append(os.path.splitext(f)[1])
            else:
                ext_name(f)
    else:
        result.append(os.path.splitext(dir)[1])
    result=set(result)
    return result
print(ext_name('/home/joker/code/python'))

print('''4. 定义一个函数xulie(dirname,info)
参数：dirname:路径名，info:需要序列化的数据，功能：将info数据序列化存储到dirname路径下随机的文件里
code :
def xulie(dirname,info):
    if os.path.exists(dirname):
        return 'dir not found'
    a=pickle.dumps(info)#以字节对象形式返回封装的对象，不需要写入文件中
    filename=''
    for i in range(10):
        filename=filename+random.choice('abcedfghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890')
    filepath=os.path.join(dirname,filename)
    f=open(filepath,'wb+')
    f.write(a)
    f.close()
xulie('/home/joker/code/python/Module','12345')''')
def xulie(dirname,info):
    if not os.path.exists(dirname):
        return 'dir not found'
    a=pickle.dumps(info)#以字节对象形式返回封装的对象，不需要写入文件中
    filename=''
    for i in range(10):
        filename=filename+random.choice('abcedfghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890')
    filepath=os.path.join(dirname,filename)
    f=open(filepath,'wb+')
    f.write(a)
    f.close()
xulie('/home/joker/code/python/Module/','12345')
