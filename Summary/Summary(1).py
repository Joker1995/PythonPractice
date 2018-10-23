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
