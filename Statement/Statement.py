#encoding=utf-8
print '用while语句的2种方法输出数字：1到10'
print '''code 1):
i=1
while i<11:
    print i
    i+=1
result:
'''
i=1
while i<11:
    print i
    i+=1
print 'end'
print '''code 2):
i=1
while True:
    print i
    i+=1
    if i>10:
        break
result:'''
i=1
while True:
    print i
    i+=1
    if i>10:
        break
print '用for语句和continue 输出结果：1 3 5 7 9'
print '''
code :
    for x in range(1,10):
        if x%2==1:
            print x
        else:
            continue
result:'''
for x in range(1,10):
    if x%2==1:
        print x
    else:
        continue
print '''
a = [1,2,3,4,5,6]
1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，
    如果不存在的话,输出字符串'not find'
'''
print '''code :
isFined=False
for x in a:
    if x===8:
        isFined=True
if isFined:
    print 'find'
else:
    print 'not find'
result:'''
a = [1,2,3,4,5,6]
isFined=False
for x in a:
    if x==8:
        isFined=True
if isFined:
    print 'find'
else:
    print 'not find'
print '用while语句操作上面的列表a，输出下面结果：[2,3,4,5,6,7]'
print '''code:
b=[]
i=0
len=a.__len__()
while i<len:
    b.append(a[i]+1)
    i+=1
result'''
b=[]
i=0
len=a.__len__()
while i<len:
    b.append(a[i]+1)
    i+=1
print b
