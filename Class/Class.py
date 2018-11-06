#encoding=utf-8
print('''1. 定义一个学生类。有下面的类属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int

写好类以后，可以定义2个同学测试下:
zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100
code :
class student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return self.score
stu1=student('zhangming',20,[69,88,100])
result:''')
class student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        if isinstance(self.score,list):
            return max(self.score)
stu1=student('zhangming',20,[69,88,100])
print(stu1.get_name())
print(stu1.get_age())
print(stu1.get_course())
print('''2. 定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
    del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
    get_dict(key)
3 返回键组成的列表：返回类型;(list)
    get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
    update_dict({要合并的字典})
code :
class dictclass(object):
    def __init__(self,map):
        self.map=map
    def get_dict(self,key):
        if self.map.get(key)==None:
            return 'not found'
        else:
            return self.map.get(key)
    def del_dict(self,key):
        self.map.pop(key)
    def get_key(self):
        return list(self.map.keys())
    def update_dict(self,map):
        self.map.update(map)
    def get_content(self):
        return self.map
dict=dictclass({'name':111,'age':22})
dict.del_dict('age')
print(dict.get_content())
print(dict.get_dict('name'))
print(dict.get_key())
dict.update_dict({'age':33})
print(dict.get_content())
result:''')
class dictclass(object):
    def __init__(self,map):
        self.map=map
    def get_dict(self,key):
        if self.map.get(key)==None:
            return 'not found'
        else:
            return self.map.get(key)
    def del_dict(self,key):
        self.map.pop(key)
    def get_key(self):
        return list(self.map.keys())
    def update_dict(self,map):
        self.map.update(map)
    def get_content(self):
        return self.map
dict=dictclass({'name':111,'age':22})
dict.del_dict('age')
print(dict.get_content())
print(dict.get_dict('name'))
print(dict.get_key())
dict.update_dict({'age':33})
print(dict.get_content())
