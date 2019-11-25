# 草莓15元一斤，火龙果3元一个，香蕉2元一斤，刚好花完200元，每种至少有一个/斤，有多少种可能，并列举出来

c=15
h=3
x=2
sum=200
count = 0
for i in range(1,sum//c+1):
    for j in range(1,sum//h+1):
        for k in range(1,sum//x+1):
            if sum == c*i+h*j+k*x:
                count = count + 1
                print(i,j,k)
print(count)






