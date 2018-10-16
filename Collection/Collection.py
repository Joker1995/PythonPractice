#coding=utf-8
print '''
1. 集合a = set(["a","b","c"])
    1)添加字符串'jay'到集合a里
    2)集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的并集
    3)集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的差集
'''
a=set(["a","b","c"])
print '1) code :a.add("jay")'
a.add("jay")
print a
b=set(['b','e','f','g'])
print '2) code 1:a&b'
print a | b
print '2) code 2:result=list(set(a).union(set(b)))'
result=list(set(a).union(set(b)))
print result
print '3) code 1:a&b'
print a&b
print '''3) code 2:
for x in a:
    if x in b:
        result.append(x)
'''
result=[]
for x in a:
    if x in b:
        result.append(x)
print result
