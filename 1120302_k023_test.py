import random as r

s1='k023_09.in'
s2='k023_09.out'

t=[]
with open(s1,'w',encoding='utf-8') as g:
    for ssh in range(7):   #測資數
        b=[]
        for i in range(10):
            b.append(str(r.randint(-10,100)))
        for i in range(800000):    #每筆資料量
            k=r.randint(1,10)
            if k<=5:b.append(str(r.randint(-5000,10000)))
            elif k<=7:b.append('+')
            elif k<=9:b.append('D')
            else:b.append('C')
        for i in b:
            g.write(i+' ')
        g.write('\n')
    
        a=[]
        for i in b:
            if i=='+':a.append(a[-1]+a[-2])
            elif i=='D':a.append(a[-1]*2)
            elif i=='C':a.pop()
            else:a.append(int(i))
        t.append(sum(a))

with open(s2,'w',encoding='utf-8') as g:
    for i in t:
        g.write(str(i)+'\n')