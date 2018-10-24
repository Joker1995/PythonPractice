#encoding=utf-8
print '''
列表a = [11,22,24,29,30,32]
1 把28插入到列表的末端
'''
a = [11,22,24,29,30,32]
print 'code :a.append(28)'
a.append(28)
print a
print '2 在元素29后面插入元素57'
a = [11,22,24,29,30,32]
print 'code :a.insert(4,57)'
a.insert(4,57)
print a
print '3 把元素11修改成6'
a = [11,22,24,29,30,32]
print 'code :a[0]=11'
a[0]=6
print a
print '4 删除元素32'
a = [11,22,24,29,30,32]
print 'del a[5]'
del a[5]
print a
print '5 对列表从小到大排序'
a = [11,22,24,29,30,32]
print 'code :sorted(a)'
print sorted(a)

print '''
列表b = [1,2,3,4,5]
1 用2种方法输出下面的结果：
[1,2,3,4,5,6,7,8]
'''
b = [1,2,3,4,5]
print 'code 1):b.extend([6,7,8])'
b.extend([6,7,8])
print b
b = [1,2,3,4,5]
print 'code 2):b.append(6);b.append(7);b.append(8);'
b.append(6);b.append(7);b.append(8);
print b
b=[1,2,3,4,5]
print '2 用列表的2种方法返回结果：[5,4]'
print 'code 1):b[-1:2:-1]'
print b[-1:2:-1]
print 'code 2:)a=[0,0];a[0]=b.pop();a[1]=b.pop();'
a=[0,0];a[0]=b.pop();a[1]=b.pop();
print a
print '3 判断2是否在列表里'
b = [1,2,3,4,5]
print 'code :b.__contains__(2)'
print b.__contains__(2)
