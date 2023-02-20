import random as r
import time

sp=[]
for i in range(800000):
    sp.append(r.randint(1000000000000000000,18446744073709551616))
with open('j870_09.in','w',encoding='utf-8') as k:
    for i in sp:
        k.write(str(i)+'\n')

t=time.time()
ts=[]
for a in sp:
    b=0
    c=18446744073709551616
    while c>a:c>>=2
    while c:
        if a>=b+c:
            a-=b+c
            b=(b>>1)+c
        else:b>>=1
        c>>=2
    ts.append(b)
print('特殊方法')
print('共計耗時: %.2f 秒'%(time.time()-t))

t=time.time()
tc=[]
for a in sp:
    tc.append(int(a**.5))
print('普通方法')
print('共計耗時: %.2f 秒'%(time.time()-t))

print(ts==tc)

with open('j870_09.out','w',encoding='utf-8') as k:
    for i in ts:
        k.write(str(i)+'\n')