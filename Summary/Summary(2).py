#encoding=utf-8
print '''已知字典：
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
2.1 迭代字典，输出结果：
('a', 'haha')
('c', 'hehe')
('b', 'python')
('f', 'xiaoming')'''
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
print '''code:
itemList=ainfo.items()
for item in itemList:
    print item
result:'''
itemList=ainfo.items()
for item in itemList:
    print item
print '''
2.2 用2种方法输出结果：
a
c
b
f
code 1):
keyList=ainfo.keys()
for item in itemList:
    print item
result:'''
keyList=ainfo.keys()
for item in keyList:
    print item
print '''code 2):
keyList=ainfo.keys()
for item in itemList:
    print item
result:'''
for key in ainfo:
    print key
print '2.3 写出查找字典里面值等于"haha"的key的代码'
print 'code :list(ainfo.keys())[list(ainfo.values()).index("haha")]'
print list(ainfo.keys())[list(ainfo.values()).index("haha")]
