# 继承
# 写一个人类类
# 再写一个学生类
# 学生类继承人类的属性和方法
# 学生类拥有自身的属性和方法

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def like(self):
        return "%s今年已经%d岁了，还是比较喜欢砍树！" % (self.name,self.age)

p=Person("光头强",20)
print(p.like())
class student(Person):
    def __init__(self,name,age, course):
        Person .__init__(self,name,age)
        self.course=course
    def print_like(self):
        print(self.like())
    def like(self):
        return "%s今年已经%d岁了，现在%d期学习知识，比较喜欢学习和运动！" % (self.name,self.age,self.course)
p=student("小米",18,38)
print(p.like())


























