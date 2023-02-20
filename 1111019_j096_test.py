import random as r

s=[]
for i in range(1000000):
    b=r.randint(0,100)
    s.append(b)
ss=''
for i in s:ss+='%s '%i
with open('j096_09.in','w',encoding='utf-8') as k:
    k.write(ss)

sk=''
a=[1,1]
for i in range(2,101):
    a.append(a[i-1]+a[i-2])
for i in s:sk+='%s '%a[i]
with open('j096_09.out','w',encoding='utf-8') as k:
    k.write(sk)