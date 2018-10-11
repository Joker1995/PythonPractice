#coding=utf-8
print '1. a = [1,2,3,4,5,333,11,44],输出下面的结果：[4,5,333]'
a=[1,2,3,4,5,333,11,44]
print 'code: a[3:5]'
print a[3:6]
##########################
print '2. a = [1,2,3],b = [4,5,6],用2个方法输出下面结果：[1,2,3,4,5,6]'
a=[1,2,3]
b=[4,5,6]
print 'code 1):a+b'
print a+b
print 'code 2):a.extend(b)'
a.extend(b)
print a
##########################
print '3. 用列表推导式生成100内的大于20的偶数'
print 'code : print [x for x in range(0,100,2) if x>20]'
print [x for x in range(0,100,2) if x>20]
##########################
print '4. 已知：元组 a = (1,2,3) 利用list方法，输出下面的结果：a=[1,2,3]'
a=(1,2,3)
print 'code :list(a)'
print list(a)
##########################
print '5. 输出结果：[1 love python,2 love python,3 love python,.... 10 love python]'
print 'code :["%s love python" for x in range(1,10)]'
print ['%s love python' %x for x in range(1,10)]
##########################
print '6. 输出结果：[(0,0),(0,2),(2,0),(2,2)]'
print 'code :[(x,y) for x in range(0,4,2) for y in range(0,4,2)]'
print [(x,y) for x in range(0,4,2) for y in range(0,4,2)]
##########################
print '7. a = [1,2,3]  b = a[:] del a .b的值是什么'
a=[1,2,3]
b=a[:]
del a
print b+',原因:引用复制'
