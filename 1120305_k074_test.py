import random as r

s1='k074_09.in'
s2='k074_09.out'

sp=[]
with open(s1,'w',encoding='utf-8') as k:
    for i in range(250000):
        x,y=r.randint(100,10000),r.randint(100,10000)
        k.write(str(x)+' '+str(y)+'\n')
        a=x^y
        ss=0
        while a!=0:
            a&=a-1
            ss+=1
        sp.append(ss)

with open(s2,'w',encoding='utf-8') as k:
    for i in sp:
        k.write(str(i)+'\n')