# 1. 读取一个txt文件，文件内容为
# 姓名， 邮箱
# abc，123@163.com
# xyz，456@163.com
#
# 得到结果并写入新文件中：
# abc的邮箱为123@163.com
# xyz的邮箱为456@163.com
# f=open("test.txt",'r',encoding='utf-8')
# data=f.read()
# print(data)
# #

with open("test.txt",'r',encoding='utf-8') as f:
    datas=f.readlines()
    print(datas)

with open("test2.txt",'w',encoding='utf-8') as f:
    for data in datas[1:]:
        tmp_data=data.split(',')
        f.write("%s的邮箱为%s" % (tuple(data.split(','))))
        f.flush()



