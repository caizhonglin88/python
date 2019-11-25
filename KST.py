
# 8.实现对列表li=[18,56,24,21,33]的冒泡排序。
# li=[18,56,24,21,33]
# for i in range(len(li)-1):
#         for j in range((len(li)-1)-i):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
# print(li)

# y=int(input('请输入一个数：'))
# if y>0:
#     print('y>0')
# elif y==0:
#     print('y==0')
# else:
#     print('y<0')

# i=10
# while i > 0:
#     print('hello world ! %s'  %i)
#     i=i-1
# else:
#     print('结束！')  #else是可以省略的，最终都会执行

# for i in [1,2,3,4,5]:
#     print(i)  #for后面跟变量名i  循环里面的所有数

# for i in 'hello world':
#     print(i) #循环字符串中所有元素结果为：h e l l o    w o r l d

# for i in range(1,10,2):
#     print(i)  #循环从1开始到9结束，每次循环加2，结果为1,3,5,7,9

# for i in range(1,5):
#     print(i)
#     if i == 2:
#         print('我准备出来了！')
#         break  #当循环到等于2时就跳出本次循环 ；可控制

# for i in range(1,5):#表示循环从1开始 到4结束
#     if i == 2:
#         continue
#     print(i) #如果当循环到2时结束本次循环，继续下一次循环关键字‘continue’

# def add(a1,a2):
#     return '%d+%d=%d' % (a1,a2,a1+a2)#
# print(add(5,6))

# def add(a1,a2):#定义函数
#     print('%d+%d=%d' % (a1,a2,a1+a2))#定义函数中的语句块
# add(3,4) #最后在调用函数具体赋值

# def type_para(t):
#     print(type(t))
# type_para(2)  #判断数据类型函数

# def nub(a,b):
#     q=a/b
#     r=a-b  #定义语句块
#     return  q,r  #存起来调用时返回给调用者
# q=nub(15,10) #调用函数具体赋值
# r=nub(20,10)
# print(q,r)  #多重赋值调用

# def func(name,score): #定义一个参数
#     return ('%s的成绩是%d分，确实很优秀！' % (name,score)) #将结果返回给调用者
# print(func('光头强',90)) #调用函数

#  #调用函数def func(name,score):
# #     print('%s的成绩是%d分，确实很优秀！' % (name,score))#打印出结果给调用者
# # func('小米',15)

def yusuan(*args):#可变参数常用单词代号*args
    sum=0
    for n in args:#循环可变参数的值
        sum=sum+n
    return sum
a=yusuan(1,2,3,4,5,6)#赋值一个变量a在打印它
print(a)
# print(yusuan(1,2,3,4,5,6))#直接调用函数

