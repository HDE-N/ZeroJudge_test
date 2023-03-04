import random as r

def sk(n,m,p):
    n=int(n)
    tp=0
    tm=0
    lp=len(p)
    lm=len(m)
    for i in range(lp):tp+=int(p[i])*n**(lp-i-1)
    for i in range(lm):tm+=int(m[i])*n**(lm-i-1)
    g=tp%tm
    if g==0:g=tp//tm
    s=0
    p=''
    while g>=(n**s):s+=1
    s-=1
    while s>=0:
        p+=str(g//n**s)
        g%=n**s
        s-=1
    return p

s1='k035_09.in'
s2='k035_09.out'

sp=[]
with open(s1,'w',encoding='utf-8') as k:
    for g in range(100000):
        n=r.randint(2,9)
        m=''
        for i in range(2):
            m+=str(r.randint(1,n-1))
        p=''
        for i in range(15):
            p+=str(r.randint(1,n-1))
        k.write('%d %s %s\n'%(n,m,p))
        sp.append(sk(n,m,p))

with open(s2,'w',encoding='utf-8') as k:
    for i in sp:
        k.write(i+'\n')