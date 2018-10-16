#coding=utf-8
print '1. 已知元组a = (1,2,3),用2种方法输出实现结果：(5,2,3)'
a=(1,2,3)
print 'code 1):b=list(a);b[0]=5;a=tuple(b)'
b=list(a)
b[0]=5
b=tuple(b)
print b
print 'code 2):b=[ x for x in a];b[0]=5;b=tuple(b)'
b=[ x for x in a]
b[0]=5
b=tuple(b)
print b
print '2. 判断2是否在元组(1,2,3)里'
print 'code :a.__contains__(2)'
print a.__contains__(2)
