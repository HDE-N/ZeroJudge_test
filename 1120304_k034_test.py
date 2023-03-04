import random as r

def sk(b):
    if b[-1]=='0':return 'Y'
    else:return str(b[-1])

s1='k034_09.in'
s2='k034_09.out'

sp=[]
with open(s1,'w',encoding='utf-8') as k:
    for g in range(800000):
        n=r.randint(2,9)
        p=''
        p+=str(r.randint(1,n-1))
        for i in range(30):      #位數
            p+=str(r.randint(0,n-1))
        if r.randint(0,10)==0:p+=str('0')
        k.write('%d %s\n'%(n,p))
        sp.append(sk(p))

with open(s2,'w',encoding='utf-8') as k:
    for i in sp:
        k.write(i+'\n')