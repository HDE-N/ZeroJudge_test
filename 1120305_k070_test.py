import random as r

s1='k070_08.in'
s2='k070_08.out'

sp=[]
b=100        #資料筆數
ls=1000       #List長度

with open(s1,'w',encoding='utf-8') as k:
    for ssh in range(b):       
        nums=[]
        for i in range(ls):
            p=r.randint(1,ls)
            nums.append(p)
            k.write(str(p)+' ')
        k.write('\n')
        ss=0
        for i in nums:
            if nums.count(i)==1:ss+=i
        sp.append(ss)

with open(s2,'w',encoding='utf-8') as k:
    for i in sp:
        k.write(str(i)+'\n')