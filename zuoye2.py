# 元素分类
# 有如下值集合 [11,22,33,77,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个 key 中，将小于 66 的值保存至第二个 key 的值中。
# 即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}

lst=[11,22,33,44,55,66,77,88,99,90]  #给这个集合设一个列表变量
dct={"k":[],"k2":[]}   #先定义一个字典，因为字典中一个键只能有一个值，所以得把多个元素组成一个列表
for i in lst:  #循环lst列表中的所有元素，
    if i>66:    #如果有大于66的元素时
        dct["k"].append(i)   #当循环到大于66时就追加为字典中K的值
    elif i<66:
       dct["k2"].append(i)   #当循环到小于66时就追加到K2值

print(dct)   #打印出追加后的字典



# a={'a':1,'b':2}
# print(a['a'])
# 打印出字典中的元素

